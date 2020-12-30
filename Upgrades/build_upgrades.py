from cmds import *
from items import items

for item, data in items.items():
    enchantment = data["enchantment"]
    levels = data["levels"]
    cost = data["cost"]

    lines = []
    for i in range(len(levels)-1):
        lines.append(Format(main,item = item,enchantment = enchantment, oldLvl = levels[i], levelsNeeded = cost[i]))
        lines.append(Format(upgrade,item = item,enchantment = enchantment, newLvl = levels[i+1]))
        lines.append(clear)
        if cost[i] > 0:
            lines.append(Format(removeLevels,levelsNeeded = cost[i]))

        lines.append(Format(end, scoreboard = "upgrading"))

    # lines.append(Format(end, scoreboard = "upgrade"))

    with open(item+".mcfunction",'w') as f:
        f.write("\n".join(lines))
