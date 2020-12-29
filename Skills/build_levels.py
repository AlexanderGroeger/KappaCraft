import sys
from os import remove
from shutil import rmtree
import json
from cmds import *
from health import WriteHealthFunctions
from luck import WriteLuckFunctions
from melee import WriteMeleeFunctions
from sprint import WriteSprintFunctions

def Build(system):
    if system == "melee":
        WriteMeleeFunctions()
    elif system == "sprint":
        WriteSprintFunctions()
    elif system == "luck":
        WriteLuckFunctions()
    elif system == "health":
        WriteHealthFunctions()


systems = ["melee", "sprint", "luck", "health"]
try:
    system = sys.argv[1]
    if not (system == "all" or system == "clean" or system in systems):
        raise Exception
except:
    print("Please specify a system to create.\nPick from {}. To build all, specify all. To remove system files, specify clean.".format(", ".join(systems)))
    exit(0)

if system == "all":
    for system in systems:
        Build(system)
elif system == "clean":
    for system in systems:
        try:
            remove(system+"_level_system.mcfunction")
            rmtree(system+"_levels")
        except:
            pass

else:
    Build(system)
