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
    "All": "PersistenceRequired:1,Tags:[\"arena\"]",
    "zombie": "DrownedConversionTime:99999999,InWaterTime:-999999"
}

uuids = {
    "generic.attack_damage": "UUID:CB3F55D3-645C-4F38-A497-9C13A33DB5CF",
    "generic.attack_speed": "UUID:[I;-121015,10957,222854,-21914]",
    # "generic.armor": {
    #     "head": "UUID:2AD3F246-FEE1-4E67-B886-69FD380BB150",
    #     "body": "UUID:9F3D476D-C118-4544-8365-64846904B48E",
    #     "legs": "UUID:D8499B04-0E66-4726-AB29-64469D734E0D",
    #     "boots": "UUID:845DB27C-C624-495F-8C9F-6020A9A58B6B",
    # }, #"UUID:[I;-121015,10957,222854,-21914]",
    # "generic.armor_toughness": {
    #     "head": "UUID:2AD3F246-FEE1-4E67-B886-69FD380BB150",
    #     "body": "UUID:9F3D476D-C118-4544-8365-64846904B48E",
    #     "legs": "UUID:D8499B04-0E66-4726-AB29-64469D734E0D",
    #     "boots": "UUID:845DB27C-C624-495F-8C9F-6020A9A58B6B",
    # }
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

def BuildRounds(difficulty,rounds):

    startingRoundPerDifficulty = {"easy": 1, "normal": 26, "hard": 51, "impossible": 76}
    startingRound = startingRoundPerDifficulty[difficulty]

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
            waveNum += startingRound
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

    with open(os.path.join(path,difficulty+"_rounds.mcfunction"),"w") as f:
        f.write("\n".join(cmds))




def Attributes(data, slot = None):

    modifiers = "AttributeModifiers:[___attributes___]" if slot else "Attributes:[___attributes___]"

    def Single(entry):
        attributeName, level = entry
        if slot is not None:
            return Format("{AttributeName:\"___name___\",Amount:___level___,Operation:0,___uuid___,Slot:___slot___,Name:\"___attributeName___\"}", name = attributeName, level = level, uuid = uuids[attributeName], slot = slot)
        else:
            return Format("{Name:\"___name___\",Base:___base___F}", name = attributeName, base = level)

    entries = [("generic.follow_range",400)]
    if type(data) is tuple:
        entries.append(data)
        # return Format(modifiers, Single(data))
    elif type(data) is list:
        entries += data
    return Format(modifiers, attributes = ",".join([Single(entry) for entry in entries]))


def Enchants(data):

    enchantments = "Enchantments:[___enchants___]"

    def Single(entry):
        name, level = entry
        return Format("{id:___name___,lvl:___level___}", name = name, level = level)

    if type(data) is tuple:
        return Format(enchantments, Single(data))
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
        return Format("{Id:___effectId___,Amplifier:___amplifier___,Duration:___duration___,Ambient:1}", id = effectIds[name], amplifier = amplifier, duration = duration)

    if type(data) is tuple:
        return Format(effects, Single(data))
    elif type(data) is list:
        return Format(effects, effects = ",".join([Single(entry) for entry in data]))


def Item(data, slot = None):
    if type(data) is str:
        return Format("{id:___item___,Count:1}", item = data)
    elif type(data) is dict:
        tags = []
        if data.get("attribute") is not None:
            tags.append(Attributes(data["attribute"], slot))
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
    return Format("HandItems:[___weapons___]", weapons = ",".join([Item(item, slot) for slot, item in data.items()]))

def NBT(tags):
    return Format("{___tags___}", tags = ",".join(tags))

def Summon(mob, mobLoot):

    mobType = mob["type"]
    mobCount = mob["count"] if mob.get("count") else 1
    mobLoot = mob["loot"] if mob.get("loot") else mobLoot
    nbtTags = [handDrops,armorDrops,necessaryTags["All"],Format("DeathLootTable:\"___loot___\"", loot = mobLoot)]
    if mob.get("armor"):
        nbtTags.append(Armor(mob["armor"]))
    if mob.get("weapons"):
        nbtTags.append(Weapons(mob["weapons"]))
    if mob.get("effects"):
        nbtTags.append(Effects(mob["effects"]))
    if necessaryTags.get(mobType) is not None:
        nbtTags.append(necessaryTags[mobType])
    return Format(summonCmd, mob = mobType, nbt = NBT(nbtTags))
