slots = {
    "-106": "weapon.offhand",
    "103": "armor.head",
    "102": "armor.chest",
    "101": "armor.legs",
    "100": "armor.feet",
}

for i in range(9):
    slots[str(i)] = "hotbar."+str(i)

for i in range(9,36):
    slots[str(i)] = "inventory."+str(i-9)
