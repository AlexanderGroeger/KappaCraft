import os

class SafeDict(dict):
    def __missing__(self, key):
        return key

def Format(s,**kwargs):
    d = SafeDict(kwargs)
    for key, value in d.items():
        s = s.replace("___"+key+"___",str(value))
    return s

necessaryTags = {
    "All": "PersistenceRequired:1,Team:Mob",
    "zombie": "DrownedConversionTime:99999999,InWaterTime:-999999"
}

effectIds = {
    "speed": 1,
    "slowness": 2,
    "haste": 3,
    "mining_fatigue": 4,
    "strength": 5,
    "instant_health": 6,
    "instant_damage": 7,
    "jump_boost": 8,
    "nausea": 9,
    "regeneration": 10,
    "resistance": 11,
    "fire_resistance": 12,
    "water_breathing": 13,
    "invisibility": 14,
    "blindness": 15,
    "night_vision": 16,
    "hunger": 17,
    "weakness": 18,
    "posion": 19,
    "wither": 20,
    "heath_boost": 21,
    "absorbtion": 22,
    "saturation": 23,
    "glowing": 24,
    "levitation": 25,
    "luck": 26,
    "unluck": 27,
    "slow_falling": 28,
    "conduit_power": 29,
    "dolphins_grace": 30,
    "bad_omen": 31,
    "hero_of_the_village": 32,
}

handDrops = "HandDropChances:[0F,0F]"
armorDrops = "ArmorDropChances:[0F,0F,0F,0F]"
nbtTags = "___handitems___,___handdrops___,"

roundCmd = "execute if score #arena round matches ___roundNum___ run ___func___"
timeMatchCmd = "execute if score #arena timer matches ___time___ run ___func___"
startMatchCmd = "execute if score #arena start matches 2.. run ___func___"
resetStartCmd = "scoreboard players set #arena start 1"
roundMatchCmd = "execute if score #arena round matches ___roundNum___ run ___func___"
spawnsMatchCmd = "execute if score #arena spawns_left matches 2..___count___ run ___func___"
decrementspawnsMatchCmd = "scoreboard players remove #arena spawns_left 1"
decrementTimerCmd = "scoreboard players remove #arena timer 1"
setSpawnCountCmd = "scoreboard players set #arena spawns_left ___count___"
setFinishedSpawnsCmd = "scoreboard players set #arena finished_spawns 2"
setTimerCmd = "scoreboard players set #arena timer ___time___"
repeatCmd = "function arena:rounds/round___roundNum___/wave___waveNum___"
roundCmd = "function arena:rounds/round___roundNum___/waves"
summonCmd = "execute at @e[tag=spawn,limit=1,sort=random] run summon minecraft:___mob___ ~ ~-109.9 ~ ___nbt___"
defaultTime = 600*20 + 1
path = "rounds"

def BuildRounds(filename, startingRound, rounds):

    def SpawnRound():
        nonlocal roundNum, round

        def SpawnWave():

            nonlocal loot, roundFolder, waveNum, wave

            if wave.get("loot"):
                loot = wave["loot"]

            cmds = []
            for mob in wave["mobs"]:
                count = mob["count"]+1 if mob.get("count") else 1+1
                cmds.append(Format(spawnsMatchCmd, count = count, func = Summon(mob, loot)))

            cmds.append(decrementspawnsMatchCmd)
            cmds.append(Format(spawnsMatchCmd, count = "", func = Format(repeatCmd, roundNum = roundNum, waveNum = waveNum)))

            with open(os.path.join(path,roundFolder,"wave{}.mcfunction".format(waveNum)), "w") as f:
                f.write("\n".join(cmds))

        roundFolder = "round"+str(roundNum)
        try:
            os.mkdir(os.path.join(path,roundFolder))
            for file in os.listdir(os.path.join(path,roundFolder)):
                os.remove(os.path.join(path,roundFolder,file))
        except:
            pass

        cmds = []

        for waveNum, wave in enumerate(round["waves"]):
            maxMobCount = max([mob["count"] if mob.get("count") else 1 for mob in wave["mobs"]]) + 1
            timer = totalTime - wave["delay"] * 20
            cmds.append(Format(timeMatchCmd, time = timer, func = Format(setSpawnCountCmd, count = maxMobCount)))
            cmds.append(Format(timeMatchCmd, time = timer, func = Format(repeatCmd, roundNum = roundNum, waveNum = waveNum)))
            SpawnWave()

        cmds.append(Format(timeMatchCmd, time = timer, func = setFinishedSpawnsCmd))

        with open(os.path.join(path,roundFolder,"waves.mcfunction"),"w") as f:
            f.write("\n".join(cmds))

    cmds = []
    for roundNum, round in enumerate(rounds):
        roundNum += startingRound
        print("round", roundNum)
        bonus = round["bonus"]
        loot = round.get("loot")
        totalTime = 20*round["time"] + 1 if round.get("time") else defaultTime

        cmds.append(Format(startMatchCmd, func = Format(roundMatchCmd, roundNum = roundNum, func = Format(setTimerCmd, time = totalTime))))
        cmds.append(Format(Format(roundMatchCmd, func = roundCmd), roundNum = roundNum))
        SpawnRound()

    # cmds.append(Format(timeMatchCmd, time = "1..", func = decrementTimerCmd))
    # cmds.append(Format(startMatchCmd, func = Format(resetStartCmd)))

    with open(os.path.join(path,filename+"_rounds.mcfunction"),"w") as f:
        f.write("\n".join(cmds))


def Attributes(data):

    modifiers = "Attributes:[___attributes___]"
    tags = []

    def Single(entry):
        attributeName, level = entry
        if attributeName == "generic.max_health":
            nonlocal tags
            tags.append("Health:{}f".format(level))
        return Format("{Name:\"___name___\",Base:___base___F}", name = attributeName, base = level)

    entries = [("generic.follow_range",400)]
    if type(data) is tuple:
        entries.append(data)
        # return Format(modifiers, Single(data))
    elif type(data) is list:
        entries += data

    tags.append(Format(modifiers, attributes = ",".join([Single(entry) for entry in entries])))
    return ",".join(tags)


def Enchants(data):

    enchantments = "Enchantments:[___enchants___]"

    def Single(entry):
        name, level = entry
        return Format("{id:___name___,lvl:___level___}", name = name, level = level)

    if type(data) is tuple:
        return Format(enchantments, enchants = Single(data))
    elif type(data) is list:
        return Format(enchantments, enchants = ",".join([Single(entry) for entry in data]))

def Effects(data):

    effects = "ActiveEffects:[___effects___]"

    def Single(entry):
        name, amplifier = entry[:2]
        if len(entry) == 3:
            duration = entry[2]
        else:
            duration = 100000
        return Format("{Id:___id___,Amplifier:___amplifier___,Duration:___duration___,Ambient:1}", id = effectIds[name], amplifier = amplifier, duration = duration)

    if type(data) is tuple:
        return Format(effects, effects = Single(data))
    elif type(data) is list:
        return Format(effects, effects = ",".join([Single(entry) for entry in data]))


def Item(data, slot = None):
    if type(data) is str:
        return Format("{id:___item___,Count:1}", item = data)
    elif type(data) is dict:
        tags = []
        # if data.get("attribute") is not None:
        #     tags.append(Attributes(data["attribute"], slot))
        if data.get("enchant") is not None:
            tags.append(Enchants(data["enchant"]))
        if len(tags) > 0:
            return Format("{id:___item___,Count:1,___tag___}", item = data["type"], tag = Format("tag:{___tags___}", tags = ",".join(tags)))
        else:
            return Format("{id:___item___,Count:1}", item = data["type"])

def Armor(data):
    armor = {"feet": {}, "legs": {}, "body": {}, "head": {}}
    for slot, item in data.items():
        armor[slot] = Item(item, slot)
    for slot, item in armor.items():
        if not item:
            armor[slot] = "{}"
    return Format("ArmorItems:[___armor___]", armor = ",".join(armor.values()))

def Weapons(data):
    if type(data) is str:
        return Format("HandItems:[___weapons___]", weapons = Item(data, "mainhand"))
    elif type(data) is dict:
        return Format("HandItems:[___weapons___]", weapons = ",".join([Item(item, slot) for slot, item in data.items()]))

def NBT(tags):
    return Format("{___tags___}", tags = ",".join(tags))

def Passengers(mobs, mobLoot):
    if type(mobs) is dict:
        return Format("Passengers:[___p___]", p = Summon(mobs,mobLoot,passenger = True))
    elif type(mobs) is list:
        return Format("Passengers:[___p___]", p = ",".join([Summon(mob,mobLoot,passenger = True) for mob in mobs]))

def Tags(tags):
    mobTags = ["\"arena\""]
    if type(tags) is str:
        mobTags.append("\"{}\"".format(tags))
    elif type(tags) is list:
        mobTags+=["\"{}\"".format(tag) for tag in tags]
    return Format("Tags:[___tags___]", tags = ",".join(mobTags))

def Summon(mob, mobLoot, passenger = False):

    mobType = mob["type"]
    mobCount = mob["count"] if mob.get("count") else 1
    if mob.get("loot"):
        mobLoot = mob["loot"]
    elif mobLoot is None:
        mobLoot = "minecraft:empty"
    mobNBT = mob.get("nbt")
    nbtTags = [handDrops,armorDrops,necessaryTags["All"],Format("DeathLootTable:\"___loot___\"", loot = mobLoot)]
    if mob.get("armor"):
        nbtTags.append(Armor(mob["armor"]))

    if mob.get("weapons"):
        nbtTags.append(Weapons(mob["weapons"]))

    if mob.get("effects"):
        nbtTags.append(Effects(mob["effects"]))

    if mob.get("attributes"):
        nbtTags.append(Attributes(mob["attributes"]))

    if necessaryTags.get(mobType) is not None:
        nbtTags.append(necessaryTags[mobType])

    if mobNBT:
        for nbt, value in mobNBT.items():
            nbtTags.append("{}:{}".format(nbt,value))
        if mobType == "zombie" and mobNBT.get("IsBaby") is None:
            nbtTags.append("IsBaby:0")

    if mob.get("passengers"):
        nbtTags.append(Passengers(mob["passengers"], mobLoot))

    nbtTags.append(Tags(mob.get("tags")))

    if passenger:
        nbtTags.append(Format("id:\"minecraft:___mob___\"",mob=mobType))
        return NBT(nbtTags)
    else:
        return Format(summonCmd, mob = mobType, nbt = NBT(nbtTags))
