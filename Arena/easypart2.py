rounds = [
    # Round 11
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 300,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 20,
                        "armor": {
                            "head": "leather_helmet",
                            "body": "leather_chestplate",
                            "legs": "leather_leggings",
                            "feet": "leather_boots",
                        },
                        "weapons": {
                            "mainhand": {
                                "type": "iron_sword",
                                "enchant": ("sharpness", 1)
                            }
                        }
                    },
                    {
                        "type": "skeleton",
                        "count": 5,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                        },
                        "weapons": {
                            "mainhand": {
                                "type": "bow",
                                "enchant": ("power", 1)
                            }
                        }
                    }
                ],
            },
            {
                "delay": 10,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 20,
                        "armor": {
                            "head": "leather_helmet",
                            "body": "leather_chestplate",
                            "legs": "leather_leggings",
                            "feet": "leather_boots",
                        },
                        "weapons": {
                            "mainhand": {
                                "type": "iron_sword",
                                "enchant": ("sharpness", 1)
                            }
                        }
                    },
                    {
                        "type": "spider",
                        "count": 10,
                    }
                ]
            }
        ]
    },
    # Round 12
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 300,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 25,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "leather_chestplate",
                            "legs": "leather_leggings",
                            "feet": "chainmail_boots",
                        },
                        "weapons": {
                            "mainhand": {
                                "type": "stone_sword",
                                "enchant": ("knockback", 2)
                            }
                        }
                    },
                    {
                        "type": "zombie",
                        "count": 5,
                        "armor": {
                            "body": "diamond_chestplate",
                        },
                    }
                ]
            },
            {
                "delay": 20,
                "mobs": [
                    {
                        "type": "skeleton",
                        "count": 20,
                        "armor": {
                            "head": "iron_helmet",
                        },
                    },
                    {
                        "type": "spider",
                        "count": 10,
                    },
                    {
                        "type": "creeper",
                        "count": 2,
                    },
                ],
            },
        ]
    },
    # Round 13
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 300,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "creeper",
                        "count": 10,
                        "attributes": ("generic.movement_speed", .3)
                    },
                ]
            },
            {
                "delay": 10,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 25,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "leather_chestplate",
                            "legs": "leather_leggings",
                            "feet": "chainmail_boots",
                        },
                        "weapons": {
                            "mainhand": {
                                "type": "iron_sword",
                                "enchant": ("fire_aspect", 1)
                            }
                        },
                        "attributes": ("generic.movement_speed", .2)
                    },
                ]
            },
        ]
    },
    # Round 14
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 300,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 20,
                    }
                ]
            },
            {
                "delay": 10,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 20,
                        "armor": {
                            "head": "lether_helmet",
                            "body": "leather_chestplate",
                        },
                    }
                ]
            },
            {
                "delay": 20,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 20,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                        },
                    }
                ]
            },
            {
                "delay": 30,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 20,
                        "armor": {
                            "head": "iron_helmet",
                            "body": "iron_chestplate",
                        },
                    }
                ]
            }
        ]
    },
    # Round 15
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 300,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 5,
                        "armor": {
                            "head": "diamond_helmet",
                            "body": "diamond_chestplate",
                        },
                    },
                    {
                        "type": "husk",
                        "count": 5,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                        },
                    },
                    {
                        "type": "cave_spider",
                        "count": 5
                    },
                    {
                        "type": "witch",
                        "count": 5
                    }
                ]
            },
            {
                "delay": 20,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 50,
                    }
                ]
            }
        ]
    },
    # Round 16
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 300,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "husk",
                        "count": 10,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate"
                        },
                        "attributes": ("generic.movement_speed", .4)
                    },
                    {
                        "type": "creeper",
                        "count": 10,
                        "attributes": ("generic.movement_speed", .3)
                    },
                    {
                        "type": "skeleton",
                        "count": 10,
                        "weapons": {
                            "mainhand": {
                                "type": "bow",
                                "enchant": [
                                    ("power", 1)
                                    ("punch", 1)
                                ]
                            }
                        }
                    },
                    {
                        "type": "slime",
                        "count": 10,
                    }
                ]
            }
        ]
    },
    # Round 17
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 300,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 20,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                            "legs": "chainmail_leggings",
                            "feet": "chainmail_boots"
                        },
                        "weapons": {
                            "mainhand": "iron_axe",
                            "offhand": "shield"
                        }
                    }
                ]
            },
            {
                "delay": 20,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 10,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                            "legs": "chainmail_leggings",
                            "feet": "chainmail_boots"
                        },
                        "weapons": {
                            "mainhand": "diamond_sword",
                            "offhand": "shield"
                        }
                    },
                    {
                        "type": "husk",
                        "count": 10,
                        "armor": {
                            "head": "gold_helmet",
                            "body": "gold_chestplate",
                            "legs": "gold_leggings",
                            "feet": "gold_boots"
                        },
                        "weapons": {
                            "mainhand": "gold_sword",
                            "offhand": "shield"
                        }
                    }
                ]
            },
            {
                "delay": 30,
                "mobs": [
                    {
                        "type": "skeleton",
                        "count": 30,
                        "weapons": "bow"
                    }
                ]
            }
        ]
    },
    # Round 19
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 300,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 15,
                        "effects": ("invisibility", 1),
                        "armor": {
                            "body": "iron_chestplate"
                        },
                        "weapons": {
                            "mainhand": "wooden_sword"
                        }
                    },
                    {
                        "type": "skeleton",
                        "count": 15,
                        "effects": ("invisibility", 1),
                        "armor": {
                            "body": "iron_chestplate"
                        },
                        "weapons": {
                            "mainhand": "bow"
                        }
                    },
                    {
                        "type": "endermen",
                        "count": 10,
                    },
                ]
            },
            {
                "delay": 30,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 30,
                        "armor": {
                            "head": "gold_helmet",
                            "body": "gold_chestplate",
                            "legs": "gold_leggings",
                            "feet": "gold_boots"
                        },
                        "weapons": {
                            "mainhand": "gold_sword"
                        },
                        "effects": ("generic.movement_speed", .4)
                    },
                    {
                        "type": "husk",
                        "count": 10,
                        "armor": {
                            "head": "iron_helmet",
                            "body": "gold_chestplate",
                            "legs": "iron_leggings",
                            "feet": "iron_boots"
                        },
                        "weapons": {
                            "mainhand": "wooden_sword"
                        },
                    }
                ]
            }
        ]
    }
]
