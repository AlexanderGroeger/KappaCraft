import sys
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

sprintSpeedAttributeCmd = executeIf + Format(attribute, attribute = "minecraft:generic.movement_speed", attribute_value = "___newMCSpeed")

meleeAttackSpeedAttributeCmd = executeIf + Format(attribute, attribute = "generic.attack_speed", attrivalue = "___newMCSpeed")
meleeAttackDamageAttributeCmd = executeIf + Format(attribute, attribute = "generic.attack_damage", attrivalue = "___newMCAttack")

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
#
# melee_cmds = [
#     (executeIf+tellraw).format(_target = targetMeleeExpLvl)+"""["",{{"text":"Melee Level Up!","bold":true,"color":"gold"}},{{"text":" Level {_oldLvl}","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"Level {_newLvl} \\n","bold":true,"color":"white"}},{{"text":"Attack Speed","bold":true,"color":"yellow"}},{{"text":" {_oldSpeed:.2f}","color":"dark_gray"}},{{"text":" ->","color":"gray"}},{{"text":" {_newSpeed:.2f}","bold":true,"color":"white"}}]""",
#     (executeIf+tellraw).format(_target = targetMeleeExpLvl)+"""["",{{"text":"Melee Level Up!","bold":true,"color":"gold"}},{{"text":" Level {_oldLvl}","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"Level {_newLvl} \\n","bold":true,"color":"white"}},{{"text":"Attack Damage","bold":true,"color":"yellow"}},{{"text":" {_oldAttack:.1f}","color":"dark_gray"}},{{"text":" ->","color":"gray"}},{{"text":" {_newAttack:.1f}","bold":true,"color":"white"}}]""",
#     (executeIf+tellraw).format(_target = targetMeleeExpLvl)+"""["",{{"text":"Luck Level Up!","bold":true,"color":"blue"}}]""",
#     (executeIf+scoreboard).format(_target = targetMeleeExpLvl, _score_mode = "add", _scoreboard = "llevel", _score_value = "1"),
#     (executeIf+tellraw).format(_target = targetMeleeExpLvl)+"""["",{{"text":"You got an extra heart!","bold":true,"color":"red"}}]""",
#     (executeIf+scoreboard).format(_target = targetMeleeExpLvl, _score_mode = "add", _scoreboard = "hlevel", _score_value = "1"),
#     (executeIf+executeAt+playsound).format(_target = targetMeleeExpLvl, _sound = "entity.player.levelup", _pitch = "1.2"),
#     (executeAt + tellraw.format(_target = targetNearby)).format(_target = targetMeleeExpLvl)  + """{{"text":"","color":"gold","extra":[{{"selector":"@a["""+targetMeleeExpLvl+"""]"}},{{"text":" is now Melee Level {_newLvl}"}}]}}""",
#     (executeAt).format(_target = targetMeleeExpLvl) + tellraw.format(_target = "") + """{{"text":"Congratulate ","color":"gold","extra":[{{"selector":"@a["""+targetMeleeExpLvl+"""]"}},{{"text":" for reaching the max Melee Level {_newLvl}!"}}]}}""",
#     (executeIf+scoreboard).format(_target = targetMeleeExpLvl, _score_mode = "set", _scoreboard = "mlevel", _score_value = "{_newLvl}"),
#     (executeIf+attribute).format(_target = targetMeleeAfter, _attribute = "generic.attack_speed", _attribute_value = "{_newMCSpeed:.2f}"),
#     (executeIf+attribute).format(_target = targetMeleeAfter, _attribute = "generic.attack_damage", _attribute_value = "{_newMCAttack:.1f}"),
# ]

def WriteSprintFunctions():
    pass

def WriteMeleeFunctions():

    funcName = mode+"_level_system.mcfunction"

    atkSpdIndex = [0,10]
    atkDmgIndex = [1,11]
    luckIndex = [2,3]
    heartIndex = [4,5]
    maxLvlIndex = [8]
    newLvlIndex = [7]

    num_levels = 50
    max_attack_speed_boost = .4
    max_attack_boost = 5
    base_exp = 1000
    exp_gain_percent = 9

    lines = []
    totalExp = 0
    for oldLvl in range(num_levels+1):
        newLvl = oldLvl + 1
        oldSpeed = (oldLvl)/num_levels*max_attack_speed_boost - .2
        newSpeed = (newLvl)/num_levels*max_attack_speed_boost - .2

        oldAttack = (newLvl-5)/num_levels*max_attack_boost - 2
        newAttack = (newLvl)/num_levels*max_attack_boost - 2

        newMCSpeed = 4 + newSpeed
        newMCAttack = newAttack

        lines.append(
            Format(
                meleeAttackSpeedAttributeCmd,
                target = Format(targetOldLvl, levelName = "mlevel", newLvl = oldLvl),
                newMCSpeed = "{:.3f}".format(round(newMCSpeed,3)),
                oldLvl = oldLvl,
            )
        )

        lines.append(
            Format(
                meleeAttackDamageAttributeCmd,
                target = Format(targetOldLvl, levelName = "mlevel", oldLvl = oldLvl),
                newMCAttack = "{:.1f}".format(round(newMCAttack,1)),
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


    with open(funcName, 'w') as f:
        f.write("\n".join(lines))

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

        lines = []
        targetLvlTransition = Format(
            targetExpOldLvl,
            scoreExp = "meleedamage",
            exp = totalExp,
            levelName = "mlevel",
            oldLvl = oldLvl,
        )
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

        # for i, cmd in enumerate(melee_cmds):
        #     if (i in maxLvlIndex+heartIndex) and newLvl != num_levels:
        #         continue
        #     if i in newLvlIndex and newLvl == num_levels:
        #         continue
        #     if (newLvl % 5 == 0):
        #         if newLvl != num_levels and i in atkSpdIndex:
        #             continue
        #     elif i in atkDmgIndex:
        #         continue
        #     if i in atkSpdIndex and newLvl == num_levels:
        #         continue
        #     if i in luckIndex and not (newLvl == int(num_levels/2) or newLvl == num_levels):
        #         continue
        #     # print(cmd)
        #     lines.append(cmd.format(_oldLvl = oldLvl, _newLvl = newLvl, _exp = totalExp, _oldSpeed = oldSpeed, _newSpeed = newSpeed, _newMCSpeed = newMCSpeed, _oldAttack = oldAttack, _newAttack = newAttack, _newMCAttack = newMCAttack))

        with open("melee_levels/melee_lvl_{_oldLvl}.mcfunction".format(_oldLvl = oldLvl), 'w') as f:
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
