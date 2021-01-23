from cmds import *
import sys
from importlib import import_module

try:
    filename = sys.argv[1].replace(".py","")
except:
    print("Please provide an arena round file.")
    exit(0)

try:
    startingRound = int(sys.argv[2])
except:
    print("Please provide the first round number for this file. Examples: 1, 26, 51, 76")
    exit(0)
    
mod = import_module(filename)

try:
    rounds = mod.rounds
except:
    print("Could not import 'rounds' from module.")
    exit(0)

BuildRounds(filename,startingRound,rounds)
