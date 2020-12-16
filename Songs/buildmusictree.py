import os
import sys
from itertools import groupby
from shutil import rmtree
from math import ceil
from config import *
import numpy as np

if not os.path.isdir(outputSongTreePath):
    print("Output song tree path in config.py is not specified or is missing in the file system!")
    exit(0)

def firstGap(ls):
    if len(ls) == 0:
        return 1
    elif len(ls) == 1:
        return 1 + int(ls[0] == 1)
    ls.sort()
    for i in range(1,len(ls)):
        if int(ls[i]) - int(ls[i-1]) > 1:
            return int(ls[i-1])+1
    return len(ls) + 1

def NBSToFunctions(songPath):

    if not songPath.endswith(".nbs"):
        sys.exit("File is not an nbs file.")
        return

    instruments = [
        "harp","bass","basedrum","snare",
        "hat","guitar","flute","bell",
        "chime","xylophone","iron_xylophone",
        "cow_bell","didgeridoo","bit","banjo","pling"
    ]

    def AdjustWithTempo(tick,tempo):
        return round(tick * (20./tempo))

    def KeyToPitch(key):
        return 2 ** ( (key - 45) / 12.)

    def ReadInt(bits):
        bytes = int(bits/8)
        return int.from_bytes(f.read(bytes), byteorder='little')

    def ReadString():
        strlen = ReadInt(32)
        return "".join([chr(ReadInt(8)) for i in range(strlen)])

    def ReadNBSFile():

        songLength = ReadInt(16)

        # if the first 2 bytes are zeros, then we're using the new format
        newNBSFormat = (songLength == 0)

        if newNBSFormat:
            print("New NBS Format detected!")
            nbsVersion = ReadInt(8)
            print("nbsVersion",nbsVersion)
            vanillaInstrumentCount = ReadInt(8)
            print("vanillaInstrumentCount",vanillaInstrumentCount)
            songLength = ReadInt(16)
        else:
            print("Old NBS Format detected!")
            vanillaInstrumentCount = 16
        print("songLength",songLength)

        songLayers = ReadInt(16)
        print("songLayers",songLayers)

        songName = ReadString().replace(' ','_').lower()
        if len(songName) == "":
            print(songPath,"has no NBS song name!")
            exit(0)

        musicId = None
        songIds = []
        for filename in os.listdir(outputSongPath):
            if filename.endswith(".mcfunction"):
                filename = filename.replace(".mcfunction","")
                tokens = filename.split('_id')
                if len(tokens) == 2:
                    name, id = tokens
                    if name == songName:
                        musicId = int(id)
                        break
                    else:
                        songIds.append(int(id))

        if musicId is None:
            musicId = firstGap(songIds)

        print("songName",songName)
        songAuthor = ReadString()
        print("songAuthor",songAuthor)
        songComposer = ReadString()
        print("songComposer",songComposer)
        songDescription = ReadString()
        print("songDescription",songDescription)
        songTempo = ReadInt(16)/100.
        print("songTempo",songTempo)

        # Skip irrelevant info
        for i in range(3):
            ReadInt(8)
        for i in range(5):
            ReadInt(32)

        ReadString()

        if newNBSFormat:
            songLoop = ReadInt(8)
            songMaxLoops = ReadInt(8)
            songLoopStartTick = ReadInt(16)

        notes = []
        tick = -1
        jumps = 0
        layer = 0

        while True:

            jumps = ReadInt(16)
            if jumps == 0:
                break
            tick += jumps
            layer = -1

            while True:

                jumps = ReadInt(16)
                if jumps == 0:
                    break
                layer += jumps

                instrument = ReadInt(8)
                key = ReadInt(8)

                if newNBSFormat:
                    volume = ReadInt(8)
                    pan = ReadInt(8)
                    pitch = ReadInt(16)

                if instrument in range(vanillaInstrumentCount) and key in range(33,58):
                    notes.append((tick,layer,instrument,key))

        f.close()
        return notes, songLength, songName, songTempo, musicId

    def OutputFunction(noteList):

        timerAddFunction = "execute at @a[scores={{MusicID={_musicId}}}] run scoreboard players add @p timer 1\n"
        playFunction = "execute at @a[scores={{MusicID={_musicId},timer={_tickTimer}}}] run playsound minecraft:block.note_block.{_noteInstrument} record @p ~ ~ ~ 1 {_notePitch}\n"
        repeatFunction = "execute at @a[scores={{MusicID={_musicId},timer={_endTimer}}}] run scoreboard players set @p timer -1\n"
        branchFunction = "execute at @a[scores={{MusicID={_musicId},timer={_startTick}..{_endTick}}}] run function "+functionBranchPrefix+"/{_songName}/{_function}\n"

        def OutputFunctionTree():

            if os.path.isdir(os.path.join(outputSongTreePath,songName)):
                rmtree(os.path.join(outputSongTreePath,songName))
            os.mkdir(os.path.join(outputSongTreePath,songName))

            notesPerTick = {}
            ticks = [int(t) for t in np.unique([tickPos for (tickPos, notes) in noteList])]
            numTicks = len(ticks)
            for tick in ticks:
                notesPerTick[tick] = [notes for (tickPos, notes) in noteList if tickPos == tick]

            with open(os.path.join(outputSongPath,"{}_id{}.mcfunction".format(songName,musicId)),"w") as func:
                func.write(timerAddFunction.format(_musicId = musicId))
                func.write(branchFunction.format(
                    _musicId = musicId,
                    _startTick = AdjustWithTempo(ticks[0],songTempo),
                    _endTick = AdjustWithTempo(ticks[-1],songTempo),
                    _songName = songName,
                    _function = "branch_{}-{}".format(AdjustWithTempo(ticks[0],songTempo),AdjustWithTempo(ticks[-1],songTempo)),)
                )
                func.write(repeatFunction.format(_musicId=musicId,_endTimer=ceil(songLength*20./songTempo)))


            def writeBranch(start, end):
                if start == end:
                    return

                startTick = ticks[start]
                endTick = ticks[end]

                lowmid = start + int((end - start) / 2)
                lowmidTick = ticks[lowmid]

                if (end - start) % 2 == 1:
                    highmid = start + ceil((end - start) / 2)
                else:
                    highmid = lowmid + 1
                highmidTick = ticks[highmid]

                adjustedStartTick = AdjustWithTempo(startTick,songTempo)
                adjustedEndTick = AdjustWithTempo(endTick,songTempo)
                adjustedLowmidTick = AdjustWithTempo(lowmidTick,songTempo)
                adjustedHighmidTick = AdjustWithTempo(highmidTick,songTempo)

                with open(os.path.join(outputSongTreePath,songName,"branch_{}-{}.mcfunction".format(adjustedStartTick,adjustedEndTick)),"w") as func:
                    if lowmid == start:
                        for note in notesPerTick[startTick]:
                            layer, instrument, key = note[0]
                            func.write(playFunction.format(_musicId=musicId,_tickTimer=adjustedLowmidTick,_noteInstrument=instruments[instrument],_notePitch=KeyToPitch(key)))
                    else:
                        func.write(branchFunction.format(
                            _musicId= musicId,
                            _startTick = adjustedStartTick,
                            _endTick = adjustedLowmidTick,
                            _songName = songName,
                            _function = "branch_{}-{}".format(adjustedStartTick,adjustedLowmidTick),)
                        )
                    if highmid == end:
                        for note in notesPerTick[endTick]:
                            layer, instrument, key = note[0]
                            func.write(playFunction.format(_musicId=musicId,_tickTimer=adjustedHighmidTick,_noteInstrument=instruments[instrument],_notePitch=KeyToPitch(key)))
                    else:
                        func.write(branchFunction.format(
                            _musicId = musicId,
                            _startTick = adjustedHighmidTick,
                            _endTick = adjustedEndTick,
                            _songName = songName,
                            _function = "branch_{}-{}".format(adjustedHighmidTick,adjustedEndTick),)
                        )
                    # if endTick == songLength and startTick == ticks[-2]:
                    #     func.write(repeatFunction.format(_musicId=musicId,_endTimer=ceil(songLength*20./songTempo)))

                if lowmid != start:
                    writeBranch(start,lowmid)

                if highmid != end:
                    writeBranch(highmid,end)

            writeBranch(0,numTicks-1)

        OutputFunctionTree()

        print(musicId)

    try:
        f = open(songPath,"rb")
        print("file loaded")
    except:
        sys.exit("Failed to open",songPath)

    notes, songLength, songName, songTempo, musicId = ReadNBSFile()
    notes = [(pos,[note[1:] for note in noteList]) for (pos,noteList) in groupby(notes,key=lambda n: n[0])]

    OutputFunction(notes)
    print("Complete!")

import sys

NBSToFunctions(sys.argv[1])
