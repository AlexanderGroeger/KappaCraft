class SafeDict(dict):
    def __missing__(self, key):
        return key

def Format(s,**kwargs):
    d = SafeDict(kwargs)
    for key, value in d.items():
        s = s.replace("___"+key+"___",str(value))
    return s

colors = ["white","orange","magenta","light_blue","yellow","lime","pink","gray","light_gray","cyan","purple","blue","brown","green","red","black"]
shulker = """nbt=!{Inventory:[{id:"minecraft:___color___shulker_box",Slot:___slotNum___b}]},scores={died=1}"""
clear = """execute at @a[] run replaceitem entity @a[nbt=!{Inventory:[{Slot:___slotNum___b,tag:{Keep:1b}}]},___shulkerTargeting___,scores={died=1,keepinventory=0}] ___slotName___ air"""
vanishClear = """replaceitem entity @a[nbt={Inventory:[{Slot:___slotNum___b,tag:{Enchantments:[{id:"minecraft:vanishing_curse",lvl:1s}]}}]}] ___slotName___ air"""
