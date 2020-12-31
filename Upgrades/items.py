items = {

    "diamond_sword": (
        {"cost": 0, "enchantments": {"sharpness": 1}},
        {"cost": 0, "enchantments": {"sharpness": 2}},
        {"cost": 0, "enchantments": {"sharpness": 3}},
        {"cost": 0, "enchantments": {"sharpness": 4}},
        {"cost": 1, "enchantments": {"sharpness": 5}},
        {"cost": 2, "enchantments": {"sharpness": 7}},
        {"cost": 2, "enchantments": {"sharpness": 10, "knockback": 1,}},
        {"cost": 2, "enchantments": {"sharpness": 15, "knockback": 1, "fire_aspect": 1,}},
        {"cost": 10, "enchantments": {"sharpness": 25, "knockback": 1, "fire_aspect": 1, "looting": 1,}},
        {"cost": 25, "enchantments": {"sharpness": 40, "knockback": 1, "fire_aspect": 1, "looting": 1, "sweeping_edge": 1}},
        {"cost": 40, "enchantments": {"sharpness": 65, "knockback": 2, "fire_aspect": 2, "looting": 2, "sweeping_edge": 2}},
        {
            "cost": 50,
            "enchantments": {"sharpness": 100, "knockback": 2, "fire_aspect": 2, "looting": 3, "sweeping_edge": 3},
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Near-perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
        {
            "enchantments": {"sharpness": 250, "knockback": 2, "fire_aspect": 2, "looting": 3, "sweeping_edge": 3},
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
    ),

    "diamond_helmet": (
        {"cost": 2, "enchantments": {"protection": 1}},
        {"cost": 3, "enchantments": {"protection": 2}},
        {"cost": 4, "enchantments": {"protection": 3}},
        {"cost": 10, "enchantments": {"protection": 4}},
        {"cost": 25, "enchantments": {"protection": 5}},
        {"cost": 40, "enchantments": {"protection": 6, "blast_protection": 1, "projectile_protection": 1, "fire_protection": 1}},
        {"cost": 50, "enchantments": {"protection": 7, "blast_protection": 2, "projectile_protection": 2, "fire_protection": 2}},
        {
            "enchantments": {"protection": 10, "blast_protection": 3, "projectile_protection": 3, "fire_protection": 3, "aqua_affinity": 1, "thorns": 5, "respiration": 10,},
            "attributes": """AttributeModifiers:[{AttributeName:"generic.max_health",Amount:2,Operation:0,UUID:[I;-1201130,31815,173936,-63630],Slot:head,Name:"generic.max_health"},{AttributeName:"generic.attack_damage",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:head,Name:"generic.attack_damage"},{AttributeName:"generic.movement_speed",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:head,Name:"generic.movement_speed"},{AttributeName:"generic.armor",Amount:3,Operation:0,UUID:[I;-1201130,3964,185758,-7928],Slot:head,Name:"generic.armor"},{AttributeName:"generic.armor_toughness",Amount:2,Operation:0,UUID:[I;-1201130,22019,185254,-44038],Slot:head,Name:"generic.armor_toughness"}]""",
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
    ),

    "diamond_chestplate": (
        {"cost": 2, "enchantments": {"protection": 1}},
        {"cost": 3, "enchantments": {"protection": 2}},
        {"cost": 4, "enchantments": {"protection": 3}},
        {"cost": 10, "enchantments": {"protection": 4}},
        {"cost": 25, "enchantments": {"protection": 5}},
        {"cost": 40, "enchantments": {"protection": 6, "blast_protection": 1, "projectile_protection": 1, "fire_protection": 1}},
        {"cost": 50, "enchantments": {"protection": 7, "blast_protection": 2, "projectile_protection": 2, "fire_protection": 2}},
        {
            "enchantments": {"protection": 10, "blast_protection": 4, "projectile_protection": 4, "fire_protection": 4, "thorns": 5,},
            "attributes": """AttributeModifiers:[{AttributeName:"generic.max_health",Amount:4,Operation:0,UUID:[I;-1201130,31815,173936,-63630],Slot:chest,Name:"generic.max_health"},{AttributeName:"generic.attack_damage",Amount:0.15,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:chest,Name:"generic.attack_damage"},{AttributeName:"generic.movement_speed",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:chest,Name:"generic.movement_speed"},{AttributeName:"generic.armor",Amount:8,Operation:0,UUID:[I;-1201130,3964,185758,-7928],Slot:chest,Name:"generic.armor"},{AttributeName:"generic.armor_toughness",Amount:2,Operation:0,UUID:[I;-1201130,22019,185254,-44038],Slot:chest,Name:"generic.armor_toughness"}]""",
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
    ),

    "diamond_leggings": (
        {"cost": 2, "enchantments": {"protection": 1}},
        {"cost": 3, "enchantments": {"protection": 2}},
        {"cost": 4, "enchantments": {"protection": 3}},
        {"cost": 10, "enchantments": {"protection": 4}},
        {"cost": 25, "enchantments": {"protection": 5}},
        {"cost": 40, "enchantments": {"protection": 6, "blast_protection": 1, "projectile_protection": 1, "fire_protection": 1}},
        {"cost": 50, "enchantments": {"protection": 7, "blast_protection": 2, "projectile_protection": 2, "fire_protection": 2}},
        {
            "enchantments": {"protection": 10, "blast_protection": 4, "projectile_protection": 4, "fire_protection": 4, "thorns": 5},
            "attributes": """AttributeModifiers:[{AttributeName:"generic.max_health",Amount:4,Operation:0,UUID:[I;-1201130,31815,173936,-63630],Slot:legs,Name:"generic.max_health"},{AttributeName:"generic.attack_damage",Amount:0.15,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:legs,Name:"generic.attack_damage"},{AttributeName:"generic.movement_speed",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:legs,Name:"generic.movement_speed"},{AttributeName:"generic.armor",Amount:6,Operation:0,UUID:[I;-1201130,3964,185758,-7928],Slot:legs,Name:"generic.armor"},{AttributeName:"generic.armor_toughness",Amount:2,Operation:0,UUID:[I;-1201130,22019,185254,-44038],Slot:legs,Name:"generic.armor_toughness"}]""",
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
    ),

    "diamond_boots": (
        {"cost": 2, "enchantments": {"protection": 1}},
        {"cost": 3, "enchantments": {"protection": 2}},
        {"cost": 4, "enchantments": {"protection": 3}},
        {"cost": 10, "enchantments": {"protection": 4}},
        {"cost": 25, "enchantments": {"protection": 5}},
        {"cost": 40, "enchantments": {"protection": 6, "blast_protection": 1, "projectile_protection": 1, "fire_protection": 1}},
        {"cost": 50, "enchantments": {"protection": 7, "blast_protection": 2, "projectile_protection": 2, "fire_protection": 2}},
        {
            "enchantments": {"protection": 10, "blast_protection": 3, "projectile_protection": 3, "fire_protection": 3, "aqua_affinity": 1, "thorns": 5, "feather_falling": 10, "frost_walker": 3, "soul_speed": 5, "depth_strider": 3},
            "attributes": """AttributeModifiers:[{AttributeName:"generic.max_health",Amount:2,Operation:0,UUID:[I;-1201130,31815,173936,-63630],Slot:feet,Name:"generic.max_health"},{AttributeName:"generic.attack_damage",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:feet,Name:"generic.attack_damage"},{AttributeName:"generic.movement_speed",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:feet,Name:"generic.movement_speed"},{AttributeName:"generic.armor",Amount:3,Operation:0,UUID:[I;-1201130,3964,185758,-7928],Slot:feet,Name:"generic.armor"},{AttributeName:"generic.armor_toughness",Amount:2,Operation:0,UUID:[I;-1201130,22019,185254,-44038],Slot:feet,Name:"generic.armor_toughness"}]""",
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
    ),

    "netherite_sword": (
        {"cost": 0, "enchantments": {"sharpness": 1}},
        {"cost": 0, "enchantments": {"sharpness": 2}},
        {"cost": 0, "enchantments": {"sharpness": 3}},
        {"cost": 0, "enchantments": {"sharpness": 4}},
        {"cost": 1, "enchantments": {"sharpness": 5}},
        {"cost": 2, "enchantments": {"sharpness": 8}},
        {"cost": 2, "enchantments": {"sharpness": 12, "knockback": 1,}},
        {"cost": 2, "enchantments": {"sharpness": 20, "knockback": 1, "fire_aspect": 1,}},
        {"cost": 10, "enchantments": {"sharpness": 40, "knockback": 1, "fire_aspect": 1, "looting": 1,}},
        {"cost": 25, "enchantments": {"sharpness": 80, "knockback": 1, "fire_aspect": 1, "looting": 1, "sweeping_edge": 1}},
        {"cost": 40, "enchantments": {"sharpness": 130, "knockback": 2, "fire_aspect": 2, "looting": 2, "sweeping_edge": 2}},
        {
            "cost": 50,
            "enchantments": {"sharpness": 200, "knockback": 2, "fire_aspect": 2, "looting": 3, "sweeping_edge": 3},
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Near-perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
        {
            "enchantments": {"sharpness": 500, "knockback": 2, "fire_aspect": 2, "looting": 5, "sweeping_edge": 3},
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
    ),

    "netherite_helmet": (
        {"cost": 2, "enchantments": {"protection": 1}},
        {"cost": 3, "enchantments": {"protection": 2}},
        {"cost": 4, "enchantments": {"protection": 3}},
        {"cost": 10, "enchantments": {"protection": 4}},
        {"cost": 25, "enchantments": {"protection": 5}},
        {"cost": 50, "enchantments": {"protection": 7, "blast_protection": 2, "projectile_protection": 2, "fire_protection": 2}},
        {
            "enchantments": {"protection": 10, "blast_protection": 3, "projectile_protection": 3, "fire_protection": 3, "aqua_affinity": 1, "thorns": 5, "respiration": 10,},
            "attributes": """AttributeModifiers:[{AttributeName:"generic.max_health",Amount:4,Operation:0,UUID:[I;-1201130,31815,173936,-63630],Slot:head,Name:"generic.max_health"},{AttributeName:"generic.attack_damage",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:head,Name:"generic.attack_damage"},{AttributeName:"generic.movement_speed",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:head,Name:"generic.movement_speed"},{AttributeName:"generic.armor",Amount:3,Operation:0,UUID:[I;-1201130,3964,185758,-7928],Slot:head,Name:"generic.armor"},{AttributeName:"generic.armor_toughness",Amount:3,Operation:0,UUID:[I;-1201130,22019,185254,-44038],Slot:head,Name:"generic.armor_toughness"},{AttributeName:"generic.knockback_resistance",Amount:0.1,Operation:0,UUID:[I;-1201131,19840,13611,-39680],Slot:chest,Name:"generic.knockback_resistance"}]""",
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
    ),

    "netherite_chestplate": (
        {"cost": 2, "enchantments": {"protection": 1}},
        {"cost": 3, "enchantments": {"protection": 2}},
        {"cost": 4, "enchantments": {"protection": 3}},
        {"cost": 10, "enchantments": {"protection": 4}},
        {"cost": 25, "enchantments": {"protection": 5}},
        {"cost": 50, "enchantments": {"protection": 7, "blast_protection": 2, "projectile_protection": 2, "fire_protection": 2}},
        {
            "enchantments": {"protection": 10, "blast_protection": 4, "projectile_protection": 4, "fire_protection": 4, "thorns": 5,},
            "attributes": """AttributeModifiers:[{AttributeName:"generic.max_health",Amount:4,Operation:0,UUID:[I;-1201130,31815,173936,-63630],Slot:chest,Name:"generic.max_health"},{AttributeName:"generic.attack_damage",Amount:0.15,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:chest,Name:"generic.attack_damage"},{AttributeName:"generic.movement_speed",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:chest,Name:"generic.movement_speed"},{AttributeName:"generic.armor",Amount:8,Operation:0,UUID:[I;-1201130,3964,185758,-7928],Slot:chest,Name:"generic.armor"},{AttributeName:"generic.armor_toughness",Amount:3,Operation:0,UUID:[I;-1201130,22019,185254,-44038],Slot:chest,Name:"generic.armor_toughness"},{AttributeName:"generic.knockback_resistance",Amount:0.1,Operation:0,UUID:[I;-1201131,19840,13611,-39680],Slot:chest,Name:"generic.knockback_resistance"}]""",
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
    ),

    "netherite_leggings": (
        {"cost": 2, "enchantments": {"protection": 1}},
        {"cost": 3, "enchantments": {"protection": 2}},
        {"cost": 4, "enchantments": {"protection": 3}},
        {"cost": 10, "enchantments": {"protection": 4}},
        {"cost": 25, "enchantments": {"protection": 5}},
        {"cost": 50, "enchantments": {"protection": 7, "blast_protection": 2, "projectile_protection": 2, "fire_protection": 2}},
        {
            "enchantments": {"protection": 10, "blast_protection": 4, "projectile_protection": 4, "fire_protection": 4, "thorns": 5},
            "attributes": """AttributeModifiers:[{AttributeName:"generic.max_health",Amount:4,Operation:0,UUID:[I;-1201130,31815,173936,-63630],Slot:legs,Name:"generic.max_health"},{AttributeName:"generic.attack_damage",Amount:0.15,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:legs,Name:"generic.attack_damage"},{AttributeName:"generic.movement_speed",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:legs,Name:"generic.movement_speed"},{AttributeName:"generic.armor",Amount:6,Operation:0,UUID:[I;-1201130,3964,185758,-7928],Slot:legs,Name:"generic.armor"},{AttributeName:"generic.armor_toughness",Amount:3,Operation:0,UUID:[I;-1201130,22019,185254,-44038],Slot:legs,Name:"generic.armor_toughness"},{AttributeName:"generic.knockback_resistance",Amount:0.1,Operation:0,UUID:[I;-1201131,19840,13611,-39680],Slot:chest,Name:"generic.knockback_resistance"}]""",
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
    ),

    "netherite_boots": (
        {"cost": 2, "enchantments": {"protection": 1}},
        {"cost": 3, "enchantments": {"protection": 2}},
        {"cost": 4, "enchantments": {"protection": 3}},
        {"cost": 10, "enchantments": {"protection": 4}},
        {"cost": 25, "enchantments": {"protection": 5}},
        {"cost": 50, "enchantments": {"protection": 7, "blast_protection": 2, "projectile_protection": 2, "fire_protection": 2}},
        {
            "enchantments": {"protection": 10, "blast_protection": 3, "projectile_protection": 3, "fire_protection": 3, "aqua_affinity": 1, "thorns": 5, "feather_falling": 10, "frost_walker": 3, "soul_speed": 5, "depth_strider": 3},
            "attributes": """AttributeModifiers:[{AttributeName:"generic.max_health",Amount:4,Operation:0,UUID:[I;-1201130,31815,173936,-63630],Slot:feet,Name:"generic.max_health"},{AttributeName:"generic.attack_damage",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:feet,Name:"generic.attack_damage"},{AttributeName:"generic.movement_speed",Amount:0.1,Operation:1,UUID:[I;-1201130,31815,173936,-63630],Slot:feet,Name:"generic.movement_speed"},{AttributeName:"generic.armor",Amount:3,Operation:0,UUID:[I;-1201130,3964,185758,-7928],Slot:feet,Name:"generic.armor"},{AttributeName:"generic.armor_toughness",Amount:3,Operation:0,UUID:[I;-1201130,22019,185254,-44038],Slot:feet,Name:"generic.armor_toughness"},{AttributeName:"generic.knockback_resistance",Amount:0.1,Operation:0,UUID:[I;-1201131,19840,13611,-39680],Slot:chest,Name:"generic.knockback_resistance"}]""",
            "unbreakable": True,
            "display": """display:{Lore:['[{"text":"Perfectly crafted","italic":false,"color":"dark_purple"}]','[{"text":"This item will not be lost on death","italic":false,"color":"dark_purple"}]']}""",
        },
    ),

}
