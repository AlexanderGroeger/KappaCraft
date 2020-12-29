from cmds import *

def WriteHealthFunctions():
    maxHealthAttributeCmd = Format(executeIf + attribute, target = targetNewLvl, attribute = "generic.max_health")
    levelName = "hlevel"
    numLevels = 13
    lines = []
    for newLvl in range(numLevels+1):
        newMCHealth = 14+2*newLvl
        lines.append(Format(maxHealthAttributeCmd, levelName = levelName, newLvl = newLvl, attrivalue = newMCHealth))

    lines.append("scoreboard players set @a died 0")
    with open("health_level_system.mcfunction", 'w') as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    WriteHealthFunctions()
