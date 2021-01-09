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
except:
    for system in systems:
        Build(system)

if system == "clean":
    for system in systems:
        try:
            remove(system+"_level_system.mcfunction")
            rmtree(system+"_levels")
        except:
            pass
elif system in systems:
    Build(system)
