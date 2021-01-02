from cmds import *

def WriteLuckFunctions():
    luckAttributeCmd = Format(attribute, target = targetNewLvl, attribute = "generic.luck")
    levelName = "llevel"
    numLevels = 20
    lines = []
    for newLvl in range(numLevels+1):
        newMCLuck = round(newLvl/4,2)
        lines.append(Format(luckAttributeCmd, levelName = levelName, newLvl = newLvl, attrivalue = "{:.2f}".format(newMCLuck)))

    with open("luck_level_system.mcfunction", 'w') as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    WriteLuckFunctions()
