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

def NBSToFunctions(songPath):

    if not songPath.endswith(".nbs"):
        sys.exit("File is not an nbs file.")
        return

    songName = os.path.basename(songPath).replace(".nbs", "").replace(" ","_").replace("'","").lower()

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

        # songName
        _ = ReadString()

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
                        notes.append((tick,layer,instrument,key,volume))
                else:
                    if instrument in range(vanillaInstrumentCount) and key in range(33,58):
                        notes.append((tick,layer,instrument,key))

        f.close()
        return notes, songLength, songName, songTempo

    def OutputFunction(noteList):

        playFunction = "execute at @a[scores={{{_scoreboard}={_tickTimer}}}] run playsound minecraft:block.note_block.{_noteInstrument} player @a[distance=..40] ~ ~ ~ {_noteVolume} {_notePitch:.4f}\n"
        branchFunction = "execute at @a[scores={{{_scoreboard}={_startTick}..{_endTick}}},limit=1] run function songs:trees/{_songName}/{_function}\n"

        def OutputFunctionTree():

            if os.path.isdir(os.path.join(outputSongTreePath,songName)):
                rmtree(os.path.join(outputSongTreePath,songName))
            os.mkdir(os.path.join(outputSongTreePath,songName))

            notesPerTick = {}
            ticks = [int(t) for t in np.unique([tickPos for (tickPos, notes) in noteList])]
            numTicks = len(ticks)
            for tick in ticks:
                notesPerTick[tick] = [notes for (tickPos, notes) in noteList if tickPos == tick]

            with open(os.path.join(outputSongPath,"sfx_{}.mcfunction".format(songName)),"w") as func:
                func.write(branchFunction.format(
                    _scoreboard = timerScoreboard,
                    _startTick = 1 + AdjustWithTempo(ticks[0],songTempo),
                    _endTick = 1 + AdjustWithTempo(ticks[-1],songTempo),
                    _songName = songName,
                    _function = "branch_{}-{}".format(1 + AdjustWithTempo(ticks[0],songTempo),1 + AdjustWithTempo(ticks[-1],songTempo)),)
                )

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

                adjustedStartTick = AdjustWithTempo(startTick,songTempo) + 1
                adjustedEndTick = AdjustWithTempo(endTick,songTempo) + 1
                adjustedLowmidTick = AdjustWithTempo(lowmidTick,songTempo) + 1
                adjustedHighmidTick = AdjustWithTempo(highmidTick,songTempo) + 1

                with open(os.path.join(outputSongTreePath,songName,"branch_{}-{}.mcfunction".format(adjustedStartTick,adjustedEndTick)),"w") as func:
                    if lowmid == start:
                        for ns in notesPerTick[startTick]:
                            for note in ns:
                                if len(note) == 4:
                                    layer, instrument, key, volume = note
                                elif len(note) == 3:
                                    layer, instrument, key = note
                                    volume = 1
                                func.write(playFunction.format(_scoreboard = timerScoreboard,_tickTimer=adjustedLowmidTick,_noteInstrument=instruments[instrument],_noteVolume = volume * 0.015, _notePitch=KeyToPitch(key)))
                    else:
                        func.write(branchFunction.format(
                            _scoreboard = timerScoreboard,
                            _startTick = adjustedStartTick,
                            _endTick = adjustedLowmidTick,
                            _songName = songName,
                            _function = "branch_{}-{}".format(adjustedStartTick,adjustedLowmidTick),)
                        )
                    if highmid == end:
                        for ns in notesPerTick[endTick]:
                            for note in ns:
                                if len(note) == 4:
                                    layer, instrument, key, volume = note
                                elif len(note) == 3:
                                    layer, instrument, key = note
                                    volume = 1
                                func.write(playFunction.format(_scoreboard = timerScoreboard,_tickTimer=adjustedHighmidTick,_noteInstrument=instruments[instrument],_noteVolume = volume * 0.015,_notePitch=KeyToPitch(key)))
                    else:
                        func.write(branchFunction.format(
                            _scoreboard = timerScoreboard,
                            _startTick = adjustedHighmidTick,
                            _endTick = adjustedEndTick,
                            _songName = songName,
                            _function = "branch_{}-{}".format(adjustedHighmidTick,adjustedEndTick),)
                        )

                if lowmid != start:
                    writeBranch(start,lowmid)

                if highmid != end:
                    writeBranch(highmid,end)

            writeBranch(0,numTicks-1)

        OutputFunctionTree()

    try:
        f = open(songPath,"rb")
        print("file loaded")
    except:
        sys.exit("Failed to open",songPath)

    notes, songLength, songName, songTempo = ReadNBSFile()
    notes = [(pos,[note[1:] for note in noteList]) for (pos,noteList) in groupby(notes,key=lambda n: n[0])]

    OutputFunction(notes)
    print("Complete!")

import sys

try:
    timerScoreboard = sys.argv[2]
except:
    timerScoreboard = "timer"

NBSToFunctions(sys.argv[1])
