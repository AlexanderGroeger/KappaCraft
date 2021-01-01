from cmds import *
from slots import slots

lines = []
for slotNum, slotName in slots.items():
    shulkerTargeting = ",".join([Format(shulker, color = color+"_") for color in colors]+[Format(shulker, color = "")])
    lines.append(Format(Format(clear, shulkerTargeting = shulkerTargeting), slotNum = slotNum, slotName = slotName))
for slotNum, slotName in slots.items():
    lines.append(Format(vanishClear, slotNum = slotNum, slotName = slotName))

with open("keep_inventory.mcfunction", 'w') as f:
    f.write("\n".join(lines))
