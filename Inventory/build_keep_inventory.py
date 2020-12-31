from cmds import *
from slots import slots

lines = []
for slotNum, slotName in slots.items():
    lines.append(Format(clear, slotNum = slotNum, slotName = slotName))
for slotNum, slotName in slots.items():
    lines.append(Format(vanishClear, slotNum = slotNum, slotName = slotName))    

with open("keep_inventory.mcfunction", 'w') as f:
    f.write("\n".join(lines))
