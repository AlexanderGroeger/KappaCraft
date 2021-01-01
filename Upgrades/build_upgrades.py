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

        # requiredEnchantments = ",".join([
        #     Format(enchantmentTemplate, enchantment = enchantment, level = level)
        #     for enchantment, level in data.items() if enchantment != "cost" and enchantment != "attributes"
        # ])

        enchantments = data["enchantments"]
        enchantment = next(iter(enchantments))
        level = enchantments[enchantment]
        requiredEnchantment = "Enchantments:[{}]".format(Format(enchantmentTemplate, enchantment = enchantment, level = level))

        nextData = item[i+1]

        tags = []

        try:
            enchantments = "Enchantments:[{}]".format(",".join([
                Format(enchantmentTemplate, enchantment = enchantment, level = level)
                for enchantment, level in nextData["enchantments"].items()
            ]))
            tags.append(enchantments)
        except:
            pass

        try:
            attributes = nextData["attributes"]
            tags.append(attributes)
        except:
            attributes = ""

        if "unbreakable" in nextData:
            tags.append("Unbreakable:1")

        if "keep" in nextData:
            tags.append("Keep:1b")

        try:
            display = nextData["display"]
            tags.append(display)
        except:
            pass

        tags = ",".join(tags)

        lines.append(Format(main, item = name, enchantment = requiredEnchantment))
        lines.append(Format(upgrade, item = name, tags = tags, levelsNeeded = levelsNeeded))
        lines.append(Format(clear,levelsNeeded = levelsNeeded))

        if levelsNeeded > 0:
            lines.append(Format(failSound, notEnoughLevels = notEnoughLevels))
            lines.append(Format(failMsg, levelsNeeded = levelsNeeded, notEnoughLevels = notEnoughLevels))
            lines.append(Format(removeLevels, levelsNeeded = levelsNeeded))

        lines.append(Format(end, scoreboard = "upgrading"))

    # lines.append(Format(end, scoreboard = "upgrade"))

    with open(name+".mcfunction",'w') as f:
        f.write("\n".join(lines))
