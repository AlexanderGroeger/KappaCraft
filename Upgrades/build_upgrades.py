from cmds import *

items = {
    "diamond_sword": {
        "enchantment": "sharpness",
        "levels": [1,2,3,4,5,7,10,15,25,40,65,100,250],
        "cost":   [0,0,0,0,1,2, 2, 2,10,30,40, 50, 0],
    },
    "netherite_sword": {
        "enchantment": "sharpness",
        "levels": [1,2,3,4,5,8,12,20,40,80,130,200,500],
        "cost":   [0,0,0,0,1,2, 2, 2,10,30,40, 50, 0],
    },
}


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
        
    lines.append(Format(end, scoreboard = "upgrade"))

    with open(item+".mcfunction",'w') as f:
        f.write("\n".join(lines))
