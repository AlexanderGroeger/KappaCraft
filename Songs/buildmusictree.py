import os
import sys
from itertools import groupby
from shutil import rmtree
from json import load, dump
from math import ceil
import numpy as np

songs = {}
if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)),"songs.json")):
    with open('songs.json', 'r') as jf:
        songs = load(jf)

def firstGap(ls):
    if len(ls) == 0:
        return "0"
    elif len(ls) == 1:
        return str(int(ls[0] == "0"))
    ls.sort()
    for i in range(1,len(ls)):
        if int(ls[i]) - int(ls[i-1]) > 1:
            return str(int(ls[i-1])+1)
    return str(len(ls))

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
            print("songLength",songLength)
        else:
            vanillaInstrumentCount = 16

        songLayers = ReadInt(16)
        print("songLayers",songLayers)

        songName = ReadString().replace(' ','_').lower()
        if len(songName) == "":
            print(songPath,"has no NBS song name!")
            exit(0)

        musicId = None
        if not songName in songs.values():
            musicId = firstGap(list(songs.keys()))
            songs[musicId] = songName
        else:
            for id, name in songs.items():
                if name == songName:
                    musicId = id

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
        branchFunction = "execute at @a[scores={{MusicID={_musicId},timer={_startTick}..{_endTick}}}] run function mcfunctions:songs:trees:{_songName}:{_function}\n"

        def OutputFunctionTree():

            if not os.path.isdir(os.path.join("trees",songName)):
                os.mkdir(os.path.join("trees",songName))
            else:
                for file in os.listdir(os.path.join("trees",songName)):
                    os.remove(os.path.join("trees",songName,file))

            notesPerTick = {}
            ticks = [int(t) for t in np.unique([tickPos for (tickPos, notes) in noteList])]
            numTicks = len(ticks)
            for tick in ticks:
                notesPerTick[tick] = [notes for (tickPos, notes) in noteList if tickPos == tick]

            def writeLeaf(tick):
                func = open(os.path.join("trees",songName,"tick_{}.mcfunction".format(tick)),"w")
                for note in notesPerTick[tick]:
                    layer, instrument, key = note[0]
                    func.write(playFunction.format(_musicId=musicId,_tickTimer=AdjustWithTempo(tick,songTempo),_noteInstrument=instruments[instrument],_notePitch=KeyToPitch(key)))
                if tick == songLength:
                    func.write(repeatFunction.format(_musicId=musicId,_endTimer=AdjustWithTempo(songLength,songTempo)))
                func.close()

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

                # lesserFunction = "branch_{}-{}".format(startTick,lowmidTick)
                # greaterFunction = "branch_{}-{}".format(highmidTick,endTick)
                #
                # if lowmid == start:
                #     # writeLeaf(startTick)
                #     lesserFunction = "tick_{}".format(startTick)
                #
                # if highmid == end:
                #     # writeLeaf(endTick)
                #     greaterFunction = "tick_{}".format(endTick)

                with open(os.path.join("trees",songName,"branch_{}-{}.mcfunction".format(AdjustWithTempo(startTick,songTempo),AdjustWithTempo(endTick,songTempo))),"w") as func:
                    if start == 0 and end == numTicks - 1:
                        func.write(timerAddFunction.format(_musicId = musicId))
                    if lowmid == start:
                        for note in notesPerTick[startTick]:
                            layer, instrument, key = note[0]
                            func.write(playFunction.format(_musicId=musicId,_tickTimer=AdjustWithTempo(lowmidTick,songTempo),_noteInstrument=instruments[instrument],_notePitch=KeyToPitch(key)))
                    else:
                        func.write(branchFunction.format(
                            _musicId= musicId,
                            _startTick = startTick,
                            _endTick = lowmidTick,
                            _songName = songName,
                            _function = "branch_{}-{}".format(AdjustWithTempo(startTick,songTempo),AdjustWithTempo(startTick,lowmidTick)),)
                        )
                    if highmid == end:
                        for note in notesPerTick[endTick]:
                            layer, instrument, key = note[0]
                            func.write(playFunction.format(_musicId=musicId,_tickTimer=AdjustWithTempo(highmidTick,songTempo),_noteInstrument=instruments[instrument],_notePitch=KeyToPitch(key)))
                    else:
                        func.write(branchFunction.format(
                            _musicId = musicId,
                            _startTick = highmidTick,
                            _endTick = endTick,
                            _songName = songName,
                            _function = "branch_{}-{}".format(AdjustWithTempo(highmidTick,songTempo),AdjustWithTempo(endTick,songTempo)),)
                        )
                    if endTick == songLength and startTick == ticks[-2]:
                        func.write(repeatFunction.format(_musicId=musicId,_endTimer=ceil(songLength*20./songTempo)))

                if lowmid != start:
                    writeBranch(start,lowmid)

                if highmid != end:
                    writeBranch(highmid,end)

            writeBranch(0,numTicks-1)

        OutputFunctionTree()

        print(musicId)
        with open('songs.json', 'w') as jf:
            dump(songs,jf,sort_keys = True)

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
