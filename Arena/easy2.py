rounds = [
    # Round 11
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 40,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 7,
                        "armor": {
                            "head": "leather_helmet",
                            "body": "leather_chestplate",
                        },
                        "weapons": "wooden_shovel",
                    },
                    {
                        "type": "skeleton",
                        "count": 2,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                        },
                        "weapons": "bow",
                    }
                ],
            },
            {
                "delay": 20,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 5,
                        "armor": {
                            "head": "leather_helmet",
                            "body": "leather_chestplate",
                        },
                        "weapons": "wooden_sword",
                    }
                ]
            }
        ]
    },
    # Round 12
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 40,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 7,
                        "armor": {
                            "body": "leather_chestplate",
                            "legs": "leather_leggings",
                        },
                        "weapons": {
                            "mainhand": {
                                "type": "golden_hoe",
                                "enchant": ("knockback", 2)
                            }
                        }
                    },
                    {
                        "type": "zombie",
                        "count": 3,
                        "armor": {
                            "body": "iron_chestplate",
                        },
                    }
                ]
            },
            {
                "delay": 20,
                "mobs": [
                    {
                        "type": "skeleton",
                        "count": 5,
                        "armor": {
                            "head": "iron_helmet",
                        },
                    },
                    {
                        "type": "creeper",
                        "count": 2,
                        "attributes": ("generic.movement_speed",.3),
                        "nbt": {
                            "Fuse": 15,
                            "ExplosionRadius": 2,
                        }
                    },
                ],
            },
        ]
    },
    # Round 13
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 40,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 5,
                    }
                ]
            },
            {
                "delay": 10,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 5,
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
                        "count": 5,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                        },
                    }
                ]
            },
        ]
    },
    # Round 14
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 40,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 7,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                        },
                        "weapons": "wooden_shovel",
                    }
                ]
            },
            {
                "delay": 20,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 4,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                        },
                        "weapons": "wooden_sword",
                    },
                    {
                        "type": "husk",
                        "count": 2,
                        "armor": {
                            "head": "golden_helmet",
                            "body": "golden_chestplate",
                        },
                        "weapons": "golden_sword",
                    }
                ]
            },
            {
                "delay": 30,
                "mobs": [
                    {
                        "type": "skeleton",
                        "count": 3,
                        "weapons": "bow"
                    }
                ]
            }
        ]
    },
    # Round 15
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 40,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 4,
                        "effects": ("invisibility", 1),
                        "armor": {
                            "body": "iron_chestplate"
                        },
                        "weapons": {
                            "mainhand": "wooden_shovel"
                        }
                    },
                    {
                        "type": "skeleton",
                        "count": 3,
                        "effects": ("invisibility", 1),
                        "armor": {
                            "body": "iron_chestplate"
                        },
                        "weapons": {
                            "mainhand": "bow"
                        }
                    },
                    {
                        "type": "witch",
                        "count": 1
                    },
                ]
            },
            {
                "delay": 30,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 6,
                        "armor": {
                            "head": "golden_helmet",
                            "body": "golden_chestplate",
                        },
                        "attributes": ("generic.movement_speed", .3)
                    },
                    {
                        "type": "husk",
                        "count": 3,
                        "armor": {
                            "head": "iron_helmet",
                            "body": "golden_chestplate",
                        },
                        "weapons": {
                            "mainhand": "wooden_sword"
                        },
                    },
                    {
                        "type": "cave_spider",
                        "count": 2
                    },
                ]
            }
        ]
    },
    # Round 16
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 45,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 10,
                        "armor": {
                            "head": "iron_helmet",
                            "body": "iron_chestplate",
                        }
                    },
                ]
            },
            {
                "delay": 20,
                "mobs": [
                    {
                        "type": "skeleton",
                        "count": 4,
                        "armor": {
                            "head": "golden_chestplate"
                        },
                        "weapons": "bow",
                        "effects": ("invisibility", 1)
                    },
                    {
                        "type": "zombie",
                        "count": 5,
                        "armor": {
                            "head": "golden_helmet"
                        },
                        "weapons": "wooden_axe",
                        "attributes": ("generic.movement_speed", .15)
                    },
                    {
                        "type": "blaze",
                        "count": 1,
                    },
                ]
            },
        ]
    },
    # Round 17
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 45,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "husk",
                        "count": 5,
                        "armor": {
                            "head": "leather_helmet",
                            "body": "leather_chestplate",
                            "legs": "leather_leggings",
                            "feet": "leather_boots"
                        }
                    }
                ]
            },
            {
                "delay": 10,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 4,
                        "armor": {
                            "head": "golden_helmet",
                            "body": "golden_chestplate",
                            "legs": "golden_leggings",
                            "feet": "golden_boots"
                        }
                    }
                ]
            },
            {
                "delay": 20,
                "mobs": [
                    {
                        "type": "skeleton",
                        "count": 3,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                            "legs": "chainmail_leggings",
                            "feet": "chainmail_boots"
                        }
                    }
                ]
            },
            {
                "delay": 30,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 2,
                        "armor": {
                            "head": "iron_helmet",
                            "body": "chainmail_chestplate",
                        },
                        "nbt": {
                            "IsBaby": 1
                        }
                    }
                ]
            },
        ]
    },
    # Round 18
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 45,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 5,
                        "weapons": "wooden_sword",
                    }
                ]
            },
            {
                "delay": 20,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 5,
                        "weapons": {
                            "mainhand": {
                                "type": "shield",
                                "enchant": ("thorns", 1)
                            },
                            "offhand": "shield"
                        }
                    },
                    {
                        "type": "skeleton",
                        "count": 3,
                        "weapons": "bow",
                    },
                ]
            }
        ]
    },
    # Round 19
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 45,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 7,
                    }
                ]
            },
            {
                "delay": 15,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 3,
                        "armor": {
                            "head": "iron_helmet",
                            "body": "iron_chestplate",
                            "legs": "iron_leggings",
                            "feet": "iron_boots"
                        },
                        "attributes": ("generic.movement_speed", .3),
                    }
                ]
            },
            {
                "delay": 30,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 7,
                        "armor": {
                            "head": "golden_helmet",
                            "body": "golden_chestplate",
                            "legs": "golden_leggings",
                            "feet": "golden_boots"
                        },
                        "weapons": "golden_sword",
                        "attributes": ("generic.movement_speed", .18),
                    }
                ]
            }
        ]
    }
]
