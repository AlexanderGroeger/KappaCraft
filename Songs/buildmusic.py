import os
import sys
from itertools import groupby
from shutil import rmtree
from math import ceil
from config import outputSongPath

if not os.path.isdir(outputSongPath):
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
        return ceil(tick * (20/tempo))

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

                try:
                    splitIndex = filename.index('_')
                except:
                    continue

                try:
                    id = int(filename[:splitIndex])
                except:
                    continue
                name = filename[splitIndex+1:]

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
        playFunction = "execute at @a[scores={{MusicID={_musicId},timer={_tickTimer}}}] run playsound minecraft:block.note_block.{_noteInstrument} record @p ~ ~ ~ 1 {_notePitch:.4f}\n"
        repeatFunction = "execute at @a[scores={{MusicID={_musicId},timer={_endTimer}..}}] run scoreboard players set @p timer -1\n"

        # Generate function for playing the note and waiting
        with open(os.path.join(outputSongPath,"{}_{}.mcfunction".format(musicId,songName)),"w") as func:
            func.write(timerAddFunction.format(_musicId = musicId))
            for notePos, (tickPos, notes) in enumerate(noteList):
                for note in notes:
                    layer, instrument, key = note
                    func.write(playFunction.format(_musicId=musicId,_tickTimer=AdjustWithTempo(tickPos,songTempo),_noteInstrument=instruments[instrument],_notePitch=KeyToPitch(key)))
            func.write(repeatFunction.format(_musicId=musicId,_endTimer=ceil(songLength*20./songTempo)))

    try:
        f = open(songPath,"rb")
        print("file loaded")
    except:
        sys.exit("Failed to open",songPath)

    notes, songLength, songName, songTempo, musicId = ReadNBSFile()
    notes = [(pos,[note[1:] for note in noteList]) for (pos,noteList) in groupby(notes,key=lambda n: n[0])]

    OutputFunction(notes)
    print(musicId)
    print("Complete!")

import sys

NBSToFunctions(sys.argv[1])
