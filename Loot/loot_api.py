import json

def Save(data,name):
    with open(name, 'w') as fp:
        json.dump(data, fp, indent=4)

def NewTable(pools = []):
    return {"pools": pools}

def NewPool(rolls = 1,bonusRolls = 1, conditions = [], entries = []):
    pool = {
        "rolls": rolls,
        "bonus_rolls": bonusRolls,
        "entries": entries
    }
    if conditions:
        pool["conditions"] = conditions
    return pool

def NewItem(weight, name, quality = 1, conditions = [], functions = []):
    item = {
        "type": "item",
        "weight": weight,
        "name": "minecraft:" + name,
        "quality": quality,
    }
    if conditions:
        item["conditions"] = conditions
    if functions:
        item["functions"] = functions
    return item

def NewCondition(condition, **kwargs):
    c = {"condition": condition}
    for name, value in kwargs.items():
        c[name] = value
    return c

def NewFunction(function, **kwargs):
    c = {"function": function}
    for name, value in kwargs.items():
        if name == "count":
            c[name] = NewRolls(value)
        else:
            c[name] = value
    return c

def NewRolls(rolls):
    if type(rolls) is list:
        if len(rolls) == 2:
            rolls = {"min": rolls[0], "max": rolls[1]}
        elif len(rolls) == 1:
            rolls = rolls[0]
        else:
            rolls = 0
    elif type(rolls) != int:
        rolls = 0
    return rolls

def GenerateTable(data, fname):
    pools = []
    for pool in data:
        rolls = NewRolls(pool["rolls"])
        bonusRolls = NewRolls(pool["bonus"])
        poolConds = []
        if "chance" in pool:
            poolConds.append(NewCondition(condition = "random_chance", chance = pool["chance"]))
        entries = []
        for entry in pool["items"]:
            name = ""
            weight = 0
            quality = 1
            conds = []
            funcs = []
            for key, value in entry.items():
                if key == "name":
                    name = value
                elif key == "weight":
                    weight = value
                elif key == "quality":
                    quality = value
                elif key == "chance":
                    conds.append(NewCondition(condition = "random_chance", chance = value))
                elif key == "count":
                    funcs.append(NewFunction(function = "set_count", count = value))
                elif key == "nbt":
                    funcs.append(NewFunction(function = "set_nbt", tag = value))
                elif key == "enchant_randomly":
                    funcs.append(NewFunction(function = "enchant_randomly"))
            entries.append(NewItem(weight,name,quality,conds,funcs))
        pools.append(NewPool(rolls,bonusRolls,poolConds,entries))
    Save(NewTable(pools),fname)
# Save(NewTable([NewPool(entries = [NewItem(weight = 1, name = "diamond", quality = 1, conditions = [NewCondition("random_chance",chance = .5)])])]), "test.json")
