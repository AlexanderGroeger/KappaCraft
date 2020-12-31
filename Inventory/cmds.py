class SafeDict(dict):
    def __missing__(self, key):
        return key

def Format(s,**kwargs):
    d = SafeDict(kwargs)
    for key, value in d.items():
        s = s.replace("___"+key+"___",str(value))
    return s

clear = """execute at @a[nbt=!{Inventory:[{id:"minecraft:shulker_box",Slot:___slotNum___b}]},scores={died=1}] run replaceitem entity @a[nbt=!{Inventory:[{Slot:___slotNum___b,tag:{Keep:1b}}]},scores={died=1,keepinventory=0}] ___slotName___ air"""
vanishClear = """replaceitem entity @a[nbt={Inventory:[{Slot:___slotNum___b,tag:{Enchantments:[{id:"minecraft:vanishing_curse",lvl:1s}]}}]}] ___slotName___ air"""
