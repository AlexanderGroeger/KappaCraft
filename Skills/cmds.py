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
attribute = "attribute @p[___target] minecraft:___attribute base set ___attrivalue"
scoreboard = "scoreboard players ___score_mode @a[___target] ___scoreboard ___score_value"
playsound = "playsound minecraft:___sound master @a ~ ~ ~ 1 ___pitch"
targetNearby = "distance=.01..40"
targetExpOldLvl = "scores={___scoreExp=___exp..,___levelName=___oldLvl}"
targetOldLvl = "scores={___levelName=___oldLvl}"
targetNewLvl = "scores={___levelName=___newLvl}"

branchCmd = executeIf + "function serverfunctions:___system_levels/___system_lvl____oldLvl"

heartNotificationCmd = tellraw + """["",{"text":"You got an extra heart!","bold":true,"color":"red"}]"""
heartScoreboardCmd = Format(scoreboard, score_mode = "add", scoreboard = "hlevel", score_value = "1")

luckNotificationCmd = tellraw + """["",{"text":"Luck Level Up!","bold":true,"color":"blue"}]"""
luckScoreboardCmd = Format(scoreboard, score_mode = "add", scoreboard = "llevel", score_value = "1")

soundLevelUpCmd = executeAt + Format(playsound, sound = "entity.player.levelup", pitch = "1.2")

levelNotificationCmd = tellraw + """["",{"text":"___levelTypeName Level Up!","bold":true,"color":"gold"},{"text":" Level ___oldLvl","color":"dark_gray"},{"text":" -> ","color":"gray"},{"text":"Level ___newLvl","bold":true,"color":"white"}"""
levelAnnouncementCmd = executeAt + Format(tellraw, target = targetNearby) + """{"text":"","color":"gold","extra":[{"selector":"@a[___target]"},{"text":" is now ___levelTypeName Level ___newLvl"}]}"""
levelMaxAnnouncementCmd = executeAt + Format(tellraw, target = "") + """{"text":"Congratulate ","color":"gold","extra":[{"selector":"@a[___target]"},{"text":" for reaching the max ___levelTypeName Level ___newLvl!"}]}"""
levelScoreboardCmd = scoreboard

awardTextCmds = {
    "Walk Speed": """,{"text":"\\nWalk Speed","bold":true,"color":"yellow"},{"text":" ___oldSpeed%","color":"gray"},{"text":" -> ","color":"gray"},{"text":"___newSpeed%","bold":true,"color":"white"}]""",
    "Attack Damage": """,{"text":"\\nAttack Damage","bold":true,"color":"yellow"},{"text":" ___oldAttack","color":"gray"},{"text":" -> ","color":"gray"},{"text":"___newAttack","bold":true,"color":"white"}]""",
    "Attack Speed": """,{"text":"\\nAttack Speed","bold":true,"color":"yellow"},{"text":" ___oldSpeed","color":"gray"},{"text":" -> ","color":"gray"},{"text":"___newSpeed","bold":true,"color":"white"}]""",
}

resetMoved = "scoreboard players set @a moved 0"
resetDamage = "scoreboard players set @a didmeleedamage 0"
