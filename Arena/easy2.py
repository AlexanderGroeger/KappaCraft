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
                            "legs": "leather_leggings",
                            "feet": "leather_boots",
                        },
                        "weapons": "wooden_sword",
                    },
                    {
                        "type": "skeleton",
                        "count": 2,
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
                        "count": 6,
                        "armor": {
                            "head": "leather_helmet",
                            "body": "leather_chestplate",
                            "legs": "leather_leggings",
                            "feet": "leather_boots",
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
                        "count": 10,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "leather_chestplate",
                            "legs": "leather_leggings",
                            "feet": "chainmail_boots",
                        },
                        "weapons": {
                            "mainhand": {
                                "type": "golden_shovel",
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
                        "count": 8,
                    }
                ]
            },
            {
                "delay": 10,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 7,
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
                        "count": 6,
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
                        "count": 5,
                        "armor": {
                            "head": "iron_helmet",
                            "body": "iron_chestplate",
                        },
                    }
                ]
            }
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
                        "count": 10,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                            "legs": "chainmail_leggings",
                            "feet": "chainmail_boots"
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
                        "count": 5,
                        "armor": {
                            "head": "chainmail_helmet",
                            "body": "chainmail_chestplate",
                            "legs": "chainmail_leggings",
                            "feet": "chainmail_boots"
                        },
                        "weapons": "wooden_sword",
                    },
                    {
                        "type": "husk",
                        "count": 2,
                        "armor": {
                            "head": "golden_helmet",
                            "body": "golden_chestplate",
                            "legs": "golden_leggings",
                            "feet": "golden_boots"
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
                        "count": 7,
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
                            "mainhand": "wooden_sword"
                        }
                    },
                    {
                        "type": "skeleton",
                        "count": 4,
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
                        "count": 8,
                        "armor": {
                            "head": "golden_helmet",
                            "body": "golden_chestplate",
                            "legs": "golden_leggings",
                            "feet": "golden_boots"
                        },
                        "attributes": ("generic.movement_speed", .3)
                    },
                    {
                        "type": "husk",
                        "count": 3,
                        "armor": {
                            "head": "iron_helmet",
                            "body": "golden_chestplate",
                            "legs": "iron_leggings",
                            "feet": "iron_boots"
                        },
                        "weapons": {
                            "mainhand": "wooden_sword"
                        },
                    },
                    {
                        "type": "cave_spider",
                        "count": 3
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
                        "type": "blaze",
                        "count": 1,
                    },
                ]
            },
            {
                "delay": 10,
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
                        "count": 5,
                        "armor": {
                            "head": "golden_helmet"
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
                        "weapons": "wooden_sword",
                        "attributes": ("generic.movement_speed", .15)
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
                        "count": 10,
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
                        "count": 6,
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
                        "count": 4,
                        "armor": {
                            "head": "iron_helmet",
                            "body": "chainmail_chestplate",
                            "legs": "chainmail_leggings",
                            "feet": "iron_boots"
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
                        "count": 8,
                        "weapons": "stone_sword",
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
                                "enchant": ("thorns", 2)
                            },
                            "offhand": "shield"
                        }
                    },
                    {
                        "type": "skeleton",
                        "count": 2,
                        "weapons": {
                            "mainhand": {
                                "type": "bow",
                                "enchant": ("power", 1)
                            },
                        }
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
                        "count": 12,
                    }
                ]
            },
            {
                "delay": 10,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 10,
                        "armor": {
                            "head": "iron_helmet",
                            "body": "iron_chestplate",
                            "legs": "iron_leggings",
                            "feet": "iron_boots"
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
                            "head": "golden_helmet",
                            "body": "golden_chestplate",
                            "legs": "golden_leggings",
                            "feet": "golden_boots"
                        },
                        "weapons": "golden_sword",
                        "attributes": ("generic.max_health", 50)
                    }
                ]
            }
        ]
    }
]
