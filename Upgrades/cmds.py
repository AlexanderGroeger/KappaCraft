class SafeDict(dict):
    def __missing__(self, key):
        return key

def Format(s,**kwargs):
    d = SafeDict(kwargs)
    for key, value in d.items():
        s = s.replace("___"+key,str(value))
    return s

enchantmentTemplate = """{id:"minecraft:___enchantment",lvl:___levels}"""
main = """execute at @p[nbt={SelectedItem:{id:"minecraft:___item",tag:{Enchantments:[___enchantments]}}},nbt={Inventory:[{Slot:-106b,id:"minecraft:___item",tag:{Enchantments:[___enchantments]}}]},scores={upgrade=1..}] run scoreboard players set @p upgrading 1"""
upgrade = """replaceitem entity @p[scores={upgrading=1..,xpLevel=___levelsNeeded..}] weapon.mainhand minecraft:___item{Enchantments:[___enchantments]}"""
clear = "replaceitem entity @p[scores={upgrading=1..,xpLevel=___levelsNeeded..}] weapon.offhand minecraft:air"
removeLevels = "xp add @p[scores={upgrading=1..,xpLevel=___levelsNeeded..}] -___levelsNeeded levels"
failSound = "playsound minecraft:entity.villager.no master @p[scores={upgrading=1..,xpLevel=..___notEnoughLevels}] ~ ~ ~ 2"
failMsg = """tellraw @p[scores={upgrading=1..,xpLevel=..___notEnoughLevels}] {"text":"Not enough XP! This upgrade requires ___levelsNeeded levels.","bold":true,"color":"gray"}"""
end = "scoreboard players set @a ___scoreboard 0"
