# KappaCraft
This is a repository for generating minecraft mcfunctions. Works for java version 1.16.4.

## Kappa Mart
Shop sign generation. Uses python dictionaries to create mcfunctions that modify signs into right-clickable purchase signs. Relies on the *Money* scoreboard. 
Documentation later...

## Skills
Documentation later...

## Loot
Documentation later...

## Songs
The songs module generates mcfunctions from note block studio files that can be played in-game. These songs are played in-game using two player scoreboards *timer* and *MusicID*. The *timer* scoreboard acts as a metronome. It keeps track of when to play notes. The *MusicId* scoreboard acts as a radio channel. It ensures only one selected song will be played for a given player. The value 0 for *MusicID* is reserved for no music.
Here's a quick overview of the files you'll be using.

**In-game Setup**

Create scoreboards *timer* and *MusicID* initialized to 0.

### *buildsong.py*

**Info**

This is an inefficient solution for playing songs with many notes.

**Input**

A note block studio file (new or old format) 
  
**Output**

An mcfunction with the naming scheme "MusicID_NameOfNoteBlockStudioSongFile". 
  
**Usage**

To generate the mcfunction in the current directory, run *python buildsong.py YourNoteBlockStudioFile.nbs*. Then place the mcfunction in the datapack's song folder and call the */reload* command to update the datapack. Next create a command-block in-game with the command *function datapack:songs/MusicID_NameOfSong*. Finally set the command block to repeat without needing redstone. That's it. You should be hearing the song you have made.


### **buildsongtree.py**
Creates a binary search tree of mcfunctions that 
Documentation later...
