executeIf = "execute if entity @a[{_target}] run "
executeAt = "execute at @a[{_target}] run "
target = "scores={{sprint={_exp}..,slevel={_oldLvl}}}"
target_after = "scores={{slevel={_newLvl}}}"
target_nearby = "distance=.01..40"
tellraw = "tellraw @a[{_target}] "
attribute = "attribute @a[{_target},limit=1] minecraft:{_attribute} base set {_attribute_value}"
scoreboard = "scoreboard players {_score_mode} @a[{_target}] {_scoreboard} {_score_value}"
playsound = "playsound minecraft:{_sound} master @a ~ ~ ~ 1 {_pitch}"

cmds = [
    (executeIf+tellraw).format(_target = target)+"""["",{{"text":"Sprinting Level Up!","bold":true,"color":"gold"}},{{"text":" Level {_oldLvl}","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"Level {_newLvl}","bold":true,"color":"white"}},{{"text":"\\nWalk Speed","bold":true,"color":"yellow"}},{{"text":" {_oldSpeed:.1f}%","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"{_newSpeed:.1f}%","bold":true,"color":"white"}}]""",
    # """execute if entity @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] run tellraw @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] ["",{{"text":"Sprinting Level Up!","bold":true,"color":"gold"}},{{"text":" Level {_oldLvl}","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"Level {_newLvl}","bold":true,"color":"white"}},{{"text":"\\nWalk Speed","bold":true,"color":"yellow"}},{{"text":" {_oldSpeed:.1f}%","color":"dark_gray"}},{{"text":" -> ","color":"gray"}},{{"text":"{_newSpeed:.1f}%","bold":true,"color":"white"}}]""",
    (executeIf+attribute).format(_target = target)
    """execute if entity @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] run attribute @a[scores={{sprint={_exp}..,slevel={_oldLvl}}},limit=1] minecraft:generic.movement_speed base set {_newMCSpeed:.4f}""",
    """execute if entity @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] run execute at @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] run playsound minecraft:entity.player.levelup master @a ~ ~ ~ 1 1.2""",
    """execute at @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] run tellraw @a[distance=.01..40] {{"text":"","color":"gold","extra":[{{"selector":"@a[scores={{sprint={_exp}..,slevel={_oldLvl}}}]"}},{{"text":" is now Sprinting Level {_newLvl}"}}]}}""",
    """execute if entity @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] run tellraw @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] ["",{{"text":"Luck Level Up!","bold":true,"color":"blue"}}]""",
    """execute if entity @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] run scoreboard players add @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] llevel 1""",
    """execute if entity @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] run scoreboard players set @a[scores={{sprint={_exp}..,slevel={_oldLvl}}}] slevel {_newLvl}""",
]

num_levels = 50
max_sprint_boost_percent = 25
base_exp = 20000
exp_gain_percent = 12

def Build():
    lines = []
    totalExp = 0
    for oldLvl in range(num_levels):
        exp = int(base_exp*(1+(exp_gain_percent/100.))**oldLvl)
        totalExp+=exp
        newLvl = oldLvl + 1
        oldSpeed = (oldLvl)/num_levels*max_sprint_boost_percent
        newSpeed = (newLvl)/num_levels*max_sprint_boost_percent
        newMCSpeed = .1000 + newSpeed/1000
        for i, cmd in enumerate(cmds):
            if (i == 4 or i == 5) and newLvl % 5 != 0:
                continue
            lines.append(cmd.format(_oldLvl = oldLvl, _newLvl = newLvl, _exp = totalExp, _oldSpeed = oldSpeed, _newSpeed = newSpeed, _newMCSpeed = newMCSpeed))

    f = open("sprint_level_system.mcfunction", 'w')
    f.write("\n".join(lines))
    f.close()

Build()
