from easy import rounds
from cmds import *
import sys
from importlib import import_module

try:
    difficulty = sys.argv[1].replace(".py","")
except:
    print("Please provide an arena round file.")
    exit(0)

mod = import_module(difficulty)

try:

    rounds = mod.rounds
except:
    print("Could not import 'rounds' from module.")
    exit(0)

BuildRounds(difficulty,rounds)
