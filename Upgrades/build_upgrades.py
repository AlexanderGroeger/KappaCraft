from cmds import *
from items import items

for name, item in items.items():

    lines = []

    for i in range(len(item)-1):
        data = item[i]
        levelsNeeded = data["cost"]
        if levelsNeeded == -1:
            continue

        notEnoughLevels = levelsNeeded - 1

        requiredEnchantments = ",".join([
            Format(enchantmentTemplate, enchantment = enchantment, level = level)
            for enchantment, level in data.items() if enchantment != "cost"
        ])

        nextData = item[i+1]

        enchantments = ",".join([
            Format(enchantmentTemplate, enchantment = enchantment, level = level)
            for enchantment, level in nextData.items() if enchantment != "cost"
        ])

        lines.append(Format(main, item = name, enchantments = requiredEnchantments))
        lines.append(Format(upgrade, item = name, enchantments = enchantments, levelsNeeded = levelsNeeded))
        lines.append(Format(clear,levelsNeeded = levelsNeeded))

        if levelsNeeded > 0:
            lines.append(Format(failSound, notEnoughLevels = notEnoughLevels))
            lines.append(Format(failMsg, levelsNeeded = levelsNeeded, notEnoughLevels = notEnoughLevels))
            lines.append(Format(removeLevels, levelsNeeded = levelsNeeded))

        lines.append(Format(end, scoreboard = "upgrading"))

    # lines.append(Format(end, scoreboard = "upgrade"))

    with open(name+".mcfunction",'w') as f:
        f.write("\n".join(lines))
