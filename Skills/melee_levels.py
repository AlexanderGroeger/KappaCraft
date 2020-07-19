import sys

executeIf = "execute if entity @a[{_target}] run "
executeAt = "execute at @a[{_target}] run "
tellraw = "tellraw @a[{_target}] "
attribute = "attribute @a[{_target},limit=1] minecraft:{_attribute} base set {_attribute_value}"
scoreboard = "scoreboard players {_score_mode} @a[{_target}] {_scoreboard} {_score_value}"
playsound = "playsound minecraft:{_sound} master @a ~ ~ ~ 1 {_pitch}"
targetNearby = "distance=.01..40"

targetMeleeExpLvl = "scores={{meleedamage={_exp}..,mlevel={_oldLvl}}}"
targetMeleeLvl = "scores={{mlevel={_oldLvl}}}"
targetMeleeAfter = "scores={{mlevel={_newLvl}}}"

targetSprintExpLvl = "scores={{meleedamage={_exp}..,mlevel={_oldLvl}}}"
targetSprintLvl = "scores={{mlevel={_oldLvl}}}"
targetSprintAfter = "scores={{mlevel={_newLvl}}}"

sprint_cmds = [
    (executeIf+tellraw).format(_target = targetSprintExpLvl)+"""["",{{"text":"Sprinting Level Up!","bold":true,"color":"gold"}},{{"text":" Level {_oldLvl}","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"Level {_newLvl}","bold":true,"color":"white"}},{{"text":"\\nWalk Speed","bold":true,"color":"yellow"}},{{"text":" {_oldSpeed:.1f}%","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"{_newSpeed:.1f}%","bold":true,"color":"white"}}]""",
    (executeIf+tellraw).format(_target = targetSprintExpLvl)+"""["",{{"text":"Melee Level Up!","bold":true,"color":"gold"}},{{"text":" Level {_oldLvl}","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"Level {_newLvl} \\n","bold":true,"color":"white"}},{{"text":"Attack","bold":true,"color":"yellow"}},{{"text":" {_oldAttack:.1f}","color":"dark_gray"}},{{"text":" ->","color":"gray"}},{{"text":" {_newAttack:.1f}","bold":true,"color":"white"}}]""",
    (executeIf+tellraw).format(_target = targetSprintExpLvl)+"""["",{{"text":"Luck Level Up!","bold":true,"color":"blue"}}]""",
    (executeIf+scoreboard).format(_target = targetSprintExpLvl, _score_mode = "add", _scoreboard = "llevel", _score_value = "1"),
    (executeIf+tellraw).format(_target = targetSprintExpLvl)+"""["",{{"text":"You got an extra heart!","bold":true,"color":"red"}}]""",
    (executeIf+scoreboard).format(_target = targetSprintExpLvl, _score_mode = "add", _scoreboard = "hlevel", _score_value = "1"),
    (executeIf+executeAt+playsound).format(_target = targetSprintExpLvl, _sound = "entity.player.levelup", _pitch = "1.2"),
    (executeAt).format(_target = targetSprintExpLvl) + tellraw.format(_target = targetNearby) + """{{"text":"","color":"gold","extra":[{{"selector":"@a["""+targetSprintExpLvl+"""]"}},{{"text":" is now Sprinting Level {_newLvl}"}}]}}""",
    (executeAt).format(_target = targetSprintExpLvl) + tellraw.format(_target = "") + """{{"text":"Congratulate ","color":"gold","extra":[{{"selector":"@a["""+targetSprintExpLvl+"""]"}},{{"text":" for reaching the max Sprinting Level {_newLvl}!"}}]}}""",
    (executeIf+scoreboard).format(_target = targetSprintExpLvl, _score_mode = "set", _scoreboard = "slevel", _score_value = "{_newLvl}"),
    (executeIf+attribute).format(_target = targetSprintAfter, _attribute = "minecraft:generic.movement_speed", _attribute_value = "{_newMCSpeed:.4f}"),
]

melee_cmds = [
    (executeIf+tellraw).format(_target = targetMeleeExpLvl)+"""["",{{"text":"Melee Level Up!","bold":true,"color":"gold"}},{{"text":" Level {_oldLvl}","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"Level {_newLvl} \\n","bold":true,"color":"white"}},{{"text":"Attack Speed","bold":true,"color":"yellow"}},{{"text":" {_oldSpeed:.2f}","color":"dark_gray"}},{{"text":" ->","color":"gray"}},{{"text":" {_newSpeed:.2f}","bold":true,"color":"white"}}]""",
    (executeIf+tellraw).format(_target = targetMeleeExpLvl)+"""["",{{"text":"Melee Level Up!","bold":true,"color":"gold"}},{{"text":" Level {_oldLvl}","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"Level {_newLvl} \\n","bold":true,"color":"white"}},{{"text":"Attack","bold":true,"color":"yellow"}},{{"text":" {_oldAttack:.1f}","color":"dark_gray"}},{{"text":" ->","color":"gray"}},{{"text":" {_newAttack:.1f}","bold":true,"color":"white"}}]""",
    (executeIf+scoreboard).format(_target = targetMeleeExpLvl, _score_mode = "add", _scoreboard = "llevel", _score_value = "1"),
    (executeIf+tellraw).format(_target = targetMeleeExpLvl)+"""["",{{"text":"You got an extra heart!","bold":true,"color":"red"}}]""",
    (executeIf+scoreboard).format(_target = targetMeleeExpLvl, _score_mode = "add", _scoreboard = "hlevel", _score_value = "1"),
    (executeIf+executeAt+playsound).format(_target = targetMeleeExpLvl, _sound = "entity.player.levelup", _pitch = "1.2"),
    (executeAt + tellraw.format(_target = targetNearby)).format(_target = targetMeleeExpLvl)  + """{{"text":"","color":"gold","extra":[{{"selector":"@a["""+targetMeleeExpLvl+"""]"}},{{"text":" is now Melee Level {_newLvl}"}}]}}""",
    (executeAt).format(_target = targetMeleeExpLvl) + tellraw.format(_target = "") + """{{"text":"Congratulate ","color":"gold","extra":[{{"selector":"@a["""+targetMeleeExpLvl+"""]"}},{{"text":" for reaching the max Melee Level {_newLvl}!"}}]}}""",
    (executeIf+scoreboard).format(_target = targetMeleeExpLvl, _score_mode = "set", _scoreboard = "mlevel", _score_value = "{_newLvl}"),
    (executeIf+attribute).format(_target = targetMeleeAfter, _attribute = "generic.attack_speed", _attribute_value = "{_newMCSpeed:.2f}"),
    (executeIf+attribute).format(_target = targetMeleeAfter, _attribute = "generic.attack_damage", _attribute_value = "{_newMCAttack:.1f}"),

]

mode = sys.argv[1]
print(mode)
funcName = "melee_level_system.mcfunction"
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

def Build():

    lines = []

    # Initial stats for level 0
    lines.append((executeIf+attribute).format(_target = targetMeleeAfter.format(_newLvl = "0"), _attribute = "generic.attack_speed", _attribute_value = "-.2"))
    lines.append((executeIf+attribute).format(_target = targetMeleeAfter.format(_newLvl = "0"), _attribute = "generic.attack_damage", _attribute_value = "-2"))

    totalExp = 0
    for oldLvl in range(num_levels):
        exp = int(base_exp*(1+(exp_gain_percent/100.))**oldLvl)
        totalExp += exp
        lines.append((executeIf.format(_target = targetMeleeExpLvl)+"function serverfunctions:melee_levels/melee_lvl_{_oldLvl}.mcfunction").format(_exp = totalExp, _oldLvl = oldLvl))

    f = open(funcName, 'w')
    f.write("\n".join(lines))
    f.close()



    totalExp = 0

    for oldLvl in range(num_levels):

        exp = int(base_exp*(1+(exp_gain_percent/100.))**oldLvl)
        totalExp += exp
        newLvl = oldLvl + 1

        oldSpeed = (oldLvl)/num_levels*max_attack_speed_boost - .2
        newSpeed = (newLvl)/num_levels*max_attack_speed_boost - .2

        oldAttack = (newLvl-5)/num_levels*max_attack_boost - 2
        newAttack = (newLvl)/num_levels*max_attack_boost - 2

        newMCSpeed = 4 + newSpeed
        newMCAttack = newAttack

        f = open("melee_levels/melee_lvl_{}.mcfunction".format(oldLvl), 'w')
        lines = []
        for i, cmd in enumerate(melee_cmds):
            if (i in maxLvlIndex+heartIndex) and newLvl != num_levels:
                continue
            if i in newLvlIndex and newLvl == num_levels:
                continue
            if (newLvl % 5 == 0):
                if newLvl != num_levels and i in atkSpdIndex:
                    continue
            elif i in atkDmgIndex:
                continue
            if i in atkSpdIndex and newLvl == num_levels:
                continue
            if i in luckIndex and not (newLvl == int(num_levels/2) or newLvl == num_levels):
                continue
            # print(cmd)
            lines.append(cmd.format(_oldLvl = oldLvl, _newLvl = newLvl, _exp = totalExp, _oldSpeed = oldSpeed, _newSpeed = newSpeed, _newMCSpeed = newMCSpeed, _oldAttack = oldAttack, _newAttack = newAttack, _newMCAttack = newMCAttack))

        f.write("\n".join(lines))
        f.close()

Build()
