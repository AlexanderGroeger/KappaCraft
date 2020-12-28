import sys
import os
import json

class SafeDict(dict):
    def __missing__(self, key):
        return key

def Format(s,**kwargs):
    d = SafeDict(kwargs)
    for key, value in d.items():
        s = s.replace("___"+key,str(value))
    return s

executeIf = "execute if entity @a[___target] run "
executeAt = "execute at @a[___target] run "
tellraw = "tellraw @a[___target] "
attribute = "attribute @a[___target,limit=1] minecraft:___attribute base set ___attrivalue"
scoreboard = "scoreboard players ___score_mode @a[___target] ___scoreboard ___score_value"
playsound = "playsound minecraft:___sound master @a ~ ~ ~ 1 ___pitch"
targetNearby = "distance=.01..40"
targetExpOldLvl = "scores={___scoreExp=___exp..,___levelName=___oldLvl}"
targetOldLvl = "scores={___levelName=___oldLvl}"
targetNewLvl = "scores={___levelName=___newLvl}"

branchCmd = executeIf + "function serverfunctions:___mode_levels/___mode_lvl____oldLvl"

heartNotificationCmd = executeIf + tellraw + """["",{"text":"You got an extra heart!","bold":true,"color":"red"}]"""
heartScoreboardCmd = executeIf + Format(scoreboard, score_mode = "add", scoreboard = "hlevel", score_value = "1")

luckNotificationCmd = executeIf + tellraw + """["",{"text":"Luck Level Up!","bold":true,"color":"blue"}]"""
luckScoreboardCmd = executeIf + Format(scoreboard, score_mode = "add", scoreboard = "llevel", score_value = "1")

soundLevelUpCmd = executeIf + executeAt + Format(playsound, sound = "entity.player.levelup", pitch = "1.2")

levelNotificationCmd = executeIf + tellraw + """["",{"text":"___levelTypeName Level Up!","bold":true,"color":"gold"},{"text":" Level ___oldLvl","color":"dark_gray"},{"text":" -> ","color":"gray"},{"text":"Level ___newLvl","bold":true,"color":"white"}"""
levelAnnouncementCmd = executeAt + Format(tellraw, target = targetNearby) + """{"text":"","color":"gold","extra":[{"selector":"@a[___target]"},{"text":" is now ___levelTypeName Level ___newLvl"}]}"""
levelMaxAnnouncementCmd = executeAt + Format(tellraw, target = "") + """{"text":"Congratulate ","color":"gold","extra":[{"selector":"@a[___target]"},{"text":" for reaching the max ___levelTypeName Level ___newLvl!"}]}"""
levelScoreboardCmd = executeIf + scoreboard

meleeInitialCmds = [
    executeIf + Format(attribute, attribute = "generic.attack_speed", attribute_value = "3.8"),
    executeIf + Format(attribute, attribute = "generic.attack_damage", attribute_value = "-2"),
]

awardTextCmds = {
    "Walk Speed": """,{"text":"\\nWalk Speed","bold":true,"color":"yellow"},{"text":" ___oldSpeed%","color":"gray"},{"text":" -> ","color":"gray"},{"text":"___newSpeed%","bold":true,"color":"white"}]""",
    "Attack Damage": """,{"text":"\\nAttack Damage","bold":true,"color":"yellow"},{"text":" ___oldAttack","color":"gray"},{"text":" -> ","color":"gray"},{"text":"___newAttack","bold":true,"color":"white"}]""",
    "Attack Speed": """,{"text":"\\nAttack Speed","bold":true,"color":"yellow"},{"text":" ___oldSpeed","color":"gray"},{"text":" -> ","color":"gray"},{"text":"___newSpeed","bold":true,"color":"white"}]""",
}


# sprint_cmds = [
#     (executeIf+tellraw).format(_target = targetSprintExpLvl)+"""["",{{"text":"Sprinting Level Up!","bold":true,"color":"gold"}},{{"text":" Level {_oldLvl}","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"Level {_newLvl}","bold":true,"color":"white"}},{{"text":"\\nWalk Speed","bold":true,"color":"yellow"}},{{"text":" {_oldSpeed:.1f}%","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"{_newSpeed:.1f}%","bold":true,"color":"white"}}]""",
#     (executeIf+tellraw).format(_target = targetSprintExpLvl)+"""["",{{"text":"Melee Level Up!","bold":true,"color":"gold"}},{{"text":" Level {_oldLvl}","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"Level {_newLvl} \\n","bold":true,"color":"white"}},{{"text":"Attack","bold":true,"color":"yellow"}},{{"text":" {_oldAttack:.1f}","color":"dark_gray"}},{{"text":" ->","color":"gray"}},{{"text":" {_newAttack:.1f}","bold":true,"color":"white"}}]""",
#     (executeIf+tellraw).format(_target = targetSprintExpLvl)+"""["",{{"text":"Luck Level Up!","bold":true,"color":"blue"}}]""",
#     (executeIf+scoreboard).format(_target = targetSprintExpLvl, _score_mode = "add", _scoreboard = "llevel", _score_value = "1"),
#     (executeIf+scoreboard).format(_target = targetSprintExpLvl, _score_mode = "add", _scoreboard = "hlevel", _score_value = "1"),
#     (executeIf+executeAt+playsound).format(_target = targetSprintExpLvl, _sound = "entity.player.levelup", _pitch = "1.2"),
#     (executeAt).format(_target = targetSprintExpLvl) + tellraw.format(_target = targetNearby) + """{{"text":"","color":"gold","extra":[{{"selector":"@a["""+targetSprintExpLvl+"""]"}},{{"text":" is now Sprinting Level {_newLvl}"}}]}}""",
#     (executeAt).format(_target = targetSprintExpLvl) + tellraw.format(_target = "") + """{{"text":"Congratulate ","color":"gold","extra":[{{"selector":"@a["""+targetSprintExpLvl+"""]"}},{{"text":" for reaching the max Sprinting Level {_newLvl}!"}}]}}""",
#     (executeIf+scoreboard).format(_target = targetSprintExpLvl, _score_mode = "set", _scoreboard = "slevel", _score_value = "{_newLvl}"),
#     (executeIf+attribute).format(_target = targetSprintAfter, _attribute = "minecraft:generic.movement_speed", _attribute_value = "{_newMCSpeed:.4f}"),
# ]

def WriteSprintFunctions():

    sprintSpeedAttributeCmd = executeIf + Format(attribute, attribute = "minecraft:generic.movement_speed", attrivalue = "___newMCSpeed")

    levelName = "slevel"
    expName = "sprint"
    num_levels = 50
    max_sprint_boost_percent = 25
    base_exp = 20000
    exp_gain_percent = 12

    lines = []
    totalExp = 0

    # Generate root of tree
    for oldLvl in range(num_levels+1):
        newLvl = oldLvl + 1
        oldSpeed = (oldLvl)/num_levels*max_sprint_boost_percent
        newSpeed = (newLvl)/num_levels*max_sprint_boost_percent
        oldMCSpeed = round(.1000 + oldSpeed/1000, 4)
        newMCSpeed = round(.1000 + newSpeed/1000, 4)

        lines.append(
            Format(
                sprintSpeedAttributeCmd,
                target = Format(targetOldLvl, levelName = "mlevel", newLvl = oldLvl),
                newMCSpeed = "{:.4f}".format(oldMCSpeed),
                oldLvl = oldLvl,
            )
        )

        if oldLvl < num_levels:
            exp = int(base_exp*(1+(exp_gain_percent/100.))**oldLvl)
            totalExp += exp
            lines.append(
                Format(
                    branchCmd,
                    target = targetExpOldLvl,
                    mode = mode,
                    scoreExp = expName,
                    levelName = levelName,
                    exp = totalExp,
                    oldLvl = oldLvl,
                )
            )


    lines.append("scoreboard players set @a moved 0")
    lines.append("scoreboard players set @a died 0")

    with open(mode+"_level_system.mcfunction", 'w') as f:
        f.write("\n".join(lines))


    # Generate Tree Branches
    totalExp = 0
    for oldLvl in range(num_levels):

        exp = int(base_exp*(1+(exp_gain_percent/100.))**oldLvl)
        totalExp += exp
        newLvl = oldLvl + 1

        awardType = "Walk Speed"

        oldSpeed = round((oldLvl)/num_levels*max_sprint_boost_percent,4)
        newSpeed = round((newLvl)/num_levels*max_sprint_boost_percent,4)
        newMCSpeed = round(.1000 + newSpeed/1000,4)

        targetLvlTransition = Format(
            targetExpOldLvl,
            scoreExp = expName,
            exp = totalExp,
            levelName = levelName,
            oldLvl = oldLvl,
        )

        lines = []

        # Determine which lines go where
        lines.append(levelNotificationCmd+awardTextCmds[awardType])
        if newLvl % 5 == 0:
            lines.append(luckNotificationCmd)
            lines.append(luckScoreboardCmd)
        if newLvl == num_levels:
            lines.append(heartNotificationCmd)
            lines.append(heartScoreboardCmd)
        lines.append(levelAnnouncementCmd)
        if newLvl == num_levels:
            lines.append(levelMaxAnnouncementCmd)
        lines.append(soundLevelUpCmd)
        lines.append(Format(levelScoreboardCmd, score_mode = "set", scoreboard = "slevel", score_value = newLvl))


        for i, line in enumerate(lines):
            lines[i] = Format(
                line,
                target = targetLvlTransition,
                oldLvl = oldLvl,
                newLvl = newLvl,
                levelName = levelName,
                levelTypeName = "Sprint",
                scoreExp = expName,
                exp = totalExp,
                oldSpeed = "{:.1f}".format(oldSpeed),
                newSpeed = "{:.1f}".format(newSpeed),
                newMCSpeed = "{:.4f}".format(newMCSpeed),
                awardText = awardTextCmds[awardType]
            )

        folder = mode+"_levels"
        if not os.path.isdir(folder):
            os.mkdir(folder)
        with open(os.path.join(folder,mode+"_lvl_{}.mcfunction".format(oldLvl)), 'w') as f:
            f.write("\n".join(lines))

def WriteMeleeFunctions():

    meleeAttackSpeedAttributeCmd = executeIf + Format(attribute, attribute = "generic.attack_speed", attrivalue = "___newMCSpeed")
    meleeAttackDamageAttributeCmd = executeIf + Format(attribute, attribute = "generic.attack_damage", attrivalue = "___newMCAttack")


    num_levels = 50
    max_attack_speed_boost = .4
    max_attack_boost = 5
    base_exp = 1000
    exp_gain_percent = 9

    lines = []
    totalExp = 0

    # Generate root of tree
    for oldLvl in range(num_levels+1):
        newLvl = oldLvl + 1
        oldSpeed = (oldLvl)/num_levels*max_attack_speed_boost - .2
        newSpeed = (newLvl)/num_levels*max_attack_speed_boost - .2

        oldAttack = round((newLvl-5)/num_levels*max_attack_boost - 2, 3)
        newAttack = round((newLvl)/num_levels*max_attack_boost - 2, 1)

        oldMCSpeed = 4 + oldSpeed
        oldMCAttack = oldAttack
        newMCSpeed = 4 + newSpeed
        newMCAttack = newAttack

        lines.append(
            Format(
                meleeAttackSpeedAttributeCmd,
                target = Format(targetOldLvl, levelName = "mlevel", newLvl = oldLvl),
                newMCSpeed = "{:.3f}".format(oldMCSpeed),
                oldLvl = oldLvl,
            )
        )

        lines.append(
            Format(
                meleeAttackDamageAttributeCmd,
                target = Format(targetOldLvl, levelName = "mlevel", oldLvl = oldLvl),
                newMCAttack = "{:.1f}".format(oldMCAttack),
                oldLvl = oldLvl,
            )
        )

        if oldLvl < num_levels:
            exp = int(base_exp*(1+(exp_gain_percent/100.))**oldLvl)
            totalExp += exp
            lines.append(
                Format(
                    branchCmd,
                    target = targetExpOldLvl,
                    mode = mode,
                    scoreExp = "meleedamage",
                    levelName = "mlevel",
                    exp = totalExp,
                    oldLvl = oldLvl,
                )
            )


    lines.append("scoreboard players set @a didmeleedamage 0")
    lines.append("scoreboard players set @a died 0")

    with open(mode+"_level_system.mcfunction", 'w') as f:
        f.write("\n".join(lines))


    # Generate Tree Branches
    totalExp = 0
    for oldLvl in range(num_levels):

        exp = int(base_exp*(1+(exp_gain_percent/100.))**oldLvl)
        totalExp += exp
        newLvl = oldLvl + 1

        if newLvl % 5:
            awardType = "Attack Speed"
        else:
            awardType = "Attack Damage"

        oldSpeed = (oldLvl)/num_levels*max_attack_speed_boost - .2
        newSpeed = (newLvl)/num_levels*max_attack_speed_boost - .2

        oldAttack = round((newLvl-5)/num_levels*max_attack_boost - 2, 3)
        newAttack = round((newLvl)/num_levels*max_attack_boost - 2, 1)

        newMCSpeed = 4 + newSpeed
        newMCAttack = newAttack

        targetLvlTransition = Format(
            targetExpOldLvl,
            scoreExp = "meleedamage",
            exp = totalExp,
            levelName = "mlevel",
            oldLvl = oldLvl,
        )

        lines = []

        # Determine which lines go where
        lines.append(levelNotificationCmd+awardTextCmds[awardType])
        if newLvl == num_levels or newLvl == int(num_levels/2):
            lines.append(luckNotificationCmd)
            lines.append(luckScoreboardCmd)
        if newLvl == num_levels:
            lines.append(heartNotificationCmd)
            lines.append(heartScoreboardCmd)
        lines.append(levelAnnouncementCmd)
        if newLvl == num_levels:
            lines.append(levelMaxAnnouncementCmd)
        lines.append(soundLevelUpCmd)
        lines.append(Format(levelScoreboardCmd, score_mode = "set", scoreboard = "mlevel", score_value = newLvl))


        for i, line in enumerate(lines):
            lines[i] = Format(
                line,
                target = targetLvlTransition,
                oldLvl = oldLvl,
                newLvl = newLvl,
                levelName = "mlevel",
                levelTypeName = "Melee",
                scoreExp = "meleedamage",
                exp = totalExp,
                oldSpeed = "{:.3f}".format(oldSpeed),
                newSpeed = "{:.3f}".format(newSpeed),
                newMCSpeed = "{:.3f}".format(newMCSpeed),
                oldAttack = "{:.1f}".format(oldAttack),
                newAttack = "{:.1f}".format(newAttack),
                newMCAttack = "{:.1f}".format(newMCAttack),
                awardText = awardTextCmds[awardType]
            )

        folder = mode+"_levels"
        if not os.path.isdir(folder):
            os.mkdir(folder)
        with open(os.path.join(folder,mode+"_lvl_{}.mcfunction".format(oldLvl)), 'w') as f:
            f.write("\n".join(lines))


def Build(mode):

    if mode == "melee":
        WriteMeleeFunctions()
    elif mode == "sprint":
        WriteSprintFunctions()


systems = ["melee", "sprint"]
try:
    mode = sys.argv[1]
    if not (mode == "all" or mode in systems):
        raise Exception
except:
    print("Please specify a system to create.\nPick from {}, all.".format(", ".join(systems)))
    exit(0)

if mode == "all":
    for system in systems:
        Build(system)
else:
    Build(mode)
