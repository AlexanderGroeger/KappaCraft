class SafeDict(dict):
    def __missing__(self, key):
        return key

def Format(s,**kwargs):
    d = SafeDict(kwargs)
    for key, value in d.items():
        s = s.replace("___"+key,str(value))
    return s


main = """execute at @p[nbt={SelectedItem:{id:"minecraft:___item",tag:{Enchantments:[{id:"minecraft:___enchantment",lvl:___oldLvls}]}}},nbt={Inventory:[{Slot:-106b,id:"minecraft:___item",tag:{Enchantments:[{id:"minecraft:___enchantment",lvl:___oldLvls}]}}]},scores={upgrade=1..,xpLevel=___levelsNeeded..}] run scoreboard players set @p upgrading 1"""
upgrade = """replaceitem entity @p[scores={upgrading=1..}] weapon.mainhand minecraft:___item{Enchantments:[{id:"minecraft:___enchantment",lvl:___newLvl}]}"""
clear = "replaceitem entity @p[scores={upgrading=1..}] weapon.offhand minecraft:air"
removeLevels = "xp add @p[scores={upgrading=1..}] -___levelsNeeded levels"
end = "scoreboard players set @a ___scoreboard 0"
