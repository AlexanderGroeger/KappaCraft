import os
import sys
from itertools import groupby
from shutil import rmtree
from songs import songs

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

        songLayers = ReadInt(16)
        print("songLayers",songLayers)
        songName = ReadString().replace(' ','_').lower()
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
        #
        # else:
        #
        #     while True:
        #
        #         jumps = ReadInt(16)
        #         if jumps == 0:
        #             break
        #
        #         tick += jumps
        #         layer = -1
        #
        #         while True:
        #
        #             jumps = ReadInt(16)
        #             if jumps == 0:
        #                 break
        #
        #             layer += jumps
        #             instrument = ReadInt(8)
        #             key = ReadInt(8)
        #
        #             if instrument in range(16) and key in range(33,58):
        #                 notes.append((tick,layer,instrument,key))

        f.close()
        return notes, songLength, songName, songTempo

    # def OutputFunction(noteList):
    #     # Clear out the directory for the song before writing function files to it.
    #     if os.path.isdir(songName):
    #         rmtree(songName)
    #     os.mkdir(songName)
    #
    #     waitFunction = ("execute at @a[scores={{MusicID={_musicId},tickposition={_tickPos}}}] run scoreboard players set @p[scores={{MusicID={_musicId},tickposition={_tickPos},timer={_nextTickTimer}}}] tickposition {_nextTickPos}\n"
    #                     +"execute at @a[scores={{MusicID={_musicId},tickposition={_tickPos},timer=..{_tickTimer}}}] run function {_songName}:{_tickPos}\n"
    #                     +"execute at @a[scores={{MusicID={_musicId},tickposition={_nextTickPos}}}] run function {_songName}:{_nextTickPos}\n")
    #
    #     noteFunction = "execute at @a[scores={{MusicID={_musicId},tickposition={_tickPos}}}] run scoreboard players set @p[scores={{MusicID={_musicId},tickposition={_tickPos}}}] position {_tickPos}\n"
    #
    #     playFunction = "execute at @a[scores={{MusicID={_musicId},tickposition={_tickPos}}}] run playsound minecraft:block.note_block.{_noteInstrument} master @p ~ ~ ~ 1 {_notePitch}\n"
    #
    #     quickSwapFunction = "execute at @a[scores={{MusicID={_musicId},position={_tickPos}}}] run function {_songName}:{_tickPos}\n"
    #
    #     musicId = songs[songName]
    #     lastTickPos = 0
    #     for notePos, (tickPos, notes) in enumerate(noteList):
    #         # Generate waits that occurred before this note
    #         # Note, will not run if the tickPos of the current note is exactly 1 more than the last
    #         # for newTickPos in range(lastTickPos+1,tickPos):
    #         # if lastTickPos>0:
    #         #     func = open(songName+"/"+str(lastTickPos+1)+".mcfunction","w")
    #         #     func.write(waitFunction.format(_musicId = musicId,_tickPos=lastTickPos+1,_nextTickPos=tickPos,_songName=songName,_tickTimer=tickPos-lastTickPos))
    #         #     func.close()
    #
    #         # Generate function for playing the note and waiting
    #         func = open(songName+"/"+str(notePos)+".mcfunction","w")
    #         func.write(noteFunction.format(_musicId = musicId,_tickPos=notePos))
    #         for note in notes:
    #             layer, instrument, key = note
    #             func.write(playFunction.format(_musicId = musicId,_tickPos=notePos,_noteInstrument=instruments[instrument],_notePitch=KeyToPitch(key)))
    #         func.write(waitFunction.format(_musicId = musicId,_tickPos=notePos,_nextTickPos=notePos+1,_songName=songName,_tickTimer=tickPos-lastTickPos,_nextTickTimer=tickPos-lastTickPos+1))
    #         func.close()
    #
    #         lastTickPos = tickPos
    #
    #     # Generate the tempo shift function
    #     if os.path.isfile(songName+"_tempo_shift.mcfunction"):
    #         os.remove(songName+"_tempo_shift.mcfunction")
    #     func = open(songName+"_tempo_shift.mcfunction","w")
    #     for tickPos in range(songLength):
    #         func.write(quickSwapFunction.format(_musicId = musicId,_tickPos=tickPos,_songName=songName+"Speed1"))
    #     func.close()

    def OutputFunction(noteList):

        timerAddFunction = "execute at @a[scores={MusicID=1..}] run scoreboard players add @p timer 1\n"
        playFunction = "execute at @a[scores={{MusicID={_musicId},timer={_tickTimer}}}] run playsound minecraft:block.note_block.{_noteInstrument} record @p ~ ~ ~ 1 {_notePitch}\n"
        repeatFunction = "execute at @a[scores={{MusicID={_musicId},timer={_endTimer}}}] run scoreboard players set @p timer 0\n"

        # quickSwapFunction = "execute at @a[scores={{MusicID={_musicId},position={_tickPos}}}] run function {_songName}:{_tickPos}\n"

        musicId = songs[songName]
        # Generate function for playing the note and waiting
        func = open(songName+".mcfunction","w")
        func.write(timerAddFunction)
        for notePos, (tickPos, notes) in enumerate(noteList):
            # Generate waits that occurred before this note
            # Note, will not run if the tickPos of the current note is exactly 1 more than the last
            # for newTickPos in range(lastTickPos+1,tickPos):
            # if lastTickPos>0:
            #     func = open(songName+"/"+str(lastTickPos+1)+".mcfunction","w")
            #     func.write(waitFunction.format(_musicId = musicId,_tickPos=lastTickPos+1,_nextTickPos=tickPos,_songName=songName,_tickTimer=tickPos-lastTickPos))
            #     func.close()


            for note in notes:
                layer, instrument, key = note
                func.write(playFunction.format(_musicId=musicId,_tickTimer=round(tickPos*20./songTempo),_noteInstrument=instruments[instrument],_notePitch=KeyToPitch(key)))

        func.write(repeatFunction.format(_musicId=musicId,_endTimer=songLength))
        func.close()

    try:
        f = open(songPath,"rb")
        print("file loaded")
    except:
        sys.exit("Failed to open",songPath)

    notes, songLength, songName, songTempo = ReadNBSFile()
    if not songName in songs:
        print("The song name for",songPath,"needs to be added to songs.py!")
        exit(0)

    # print(notes[:10])
    notes = [(pos,[note[1:] for note in noteList]) for (pos,noteList) in groupby(notes,key=lambda n: n[0])]
    # print(notes[:10])
    OutputFunction(notes)
    print("Complete!")

import sys

NBSToFunctions(sys.argv[1])
