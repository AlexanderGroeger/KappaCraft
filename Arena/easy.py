rounds = [
    # Round 1
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 30,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 10,
                        "armor": {
                            "head": "leather_helmet",
                            "body": "leather_chestplate"
						}
                    },
                    {
                        "type": "skeleton",
                        "count": 5,
                        "armor": {
                            "head": "iron_helmet"
                        },
                    }
                ],
            },
        ]
    },
    # Round 2
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 30,
        "waves": [
			{
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 10,
                        "armor": {
                            "head": "leather_helmet",
                        },
						"weapons": {
							"mainhand": "wooden_sword",
						},
                    }
                ],
            },
			{
                "delay": 15,
                "mobs": [
                    {
                        "type": "skeleton",
						"count": 5,
                        "armor": {
                            "head": "leather_helmet",
                        },
						"weapons": {
							"mainhand": "wooden_sword",
						},
                    }
                ],
            },
		]
    },
	# Round 3
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 30,
        "waves": [
			{
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 5,
                        "armor": {
                            "head": "leather_helmet",
                        },
						"weapons": {
							"mainhand": "stone_axe",
						},
                    },
                    {
                        "type": "spider",
						"count": 5,
                    }
                ],
            },
			{
                "delay": 20,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 8,
						"armor": {
                            "head": "iron_helmet",
                        },
						"weapons": {
							"mainhand": "wooden_hoe",
						},
                    }
                ],
            },
		]
    },
	# Round 4
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 30,
        "waves": [
			{
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 30,
                        "armor": {
                            "head": "leather_helmet",
                        },
						"weapons": {
							"mainhand": "wooden_sword",
						},
                    }
                ],
            },
		]
    },
	# Round 5
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 30,
        "waves": [
			{
                "delay": 0,
                "mobs": [
                    {
                        "type": "silverfish",
						"count": 15,
                        "attributes": [
							("generic.movement_speed", 0.3)
                        ]
                    }
                ],
            },
			{
                "delay": 20,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 10,
						"armor": {
                            "head": "iron_helmet",
                        },
						"weapons": {
							"mainhand": "wooden_hoe",
						},
                    }
                ],
            },
		]
    },
	# Round 6
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 35,
        "waves": [
			{
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 10,
                        "attributes": [
							("generic.movement_speed", 0.3)
                        ]
                    }
                ],
            },
			{
                "delay": 20,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 15,
						"armor": {
                            "head": "leather_helmet",
							"chestplate": "leather_chestplate",
							"leggings": "leather_leggings",
							"boots": "leather_boots",
                        },
						"weapons": {
							"mainhand": "wooden_hoe",
						},
                    }
                ],
            },
		]
    },
	# Round 7
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 35,
        "waves": [
			{
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 40,
						"armor": {
                            "head": "leather_helmet",
							"chestplate": "leather_chestplate",
							"leggings": "leather_leggings",
							"boots": "leather_boots",
                        },
						"weapons": {
							"mainhand": "stone_sword",
						},
                        "attributes": [
							("generic.movement_speed", 0.15)
						]
                    }
                ],
            },
		]
    },
	# Round 8
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 35,
        "waves": [
			{
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 5,
						"armor": {
                            "head": "leather_helmet",
							"chestplate": "leather_chestplate",
                        },
						"weapons": {
							"mainhand": "iron_sword",
						},
                        "attributes": [
							("generic.attack_knockback", 5)
                        ]
                    }
                ],
            },
			{
                "delay": 10,
                "mobs": [
                    {
                        "type": "spider",
						"count": 10,
                        "attributes": [
							("generic.attack_knockback", 5)
                        ]
                    }
                ],
            },
			{
                "delay": 25,
                "mobs": [
                    {
                        "type": "skeleton",
						"count": 5,
						"armor": {
                            "head": "leather_helmet",
							"chestplate": "leather_chestplate",
                        },
						"weapons": {
							"mainhand": {
								"type": "bow",
								"enchant": [
                                    ("punch", 2),
								]
							}
						},
                    }
                ],
            },
		]
    },
	# Round 9
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 35,
        "waves": [
			{
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 7,
						"armor": {
                            "head": "iron_helmet",
							"chestplate": "iron_chestplate",
                        },
						"weapons": {
							"mainhand": "iron_sword",
						},
                        "attributes": [
							("generic.attack_knockback", 0.0)
                        ]
                    }
                ],
            },
			{
                "delay": 15,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 7,
						"armor": {
                            "head": "iron_helmet",
							"chestplate": "iron_chestplate",
                        },
						"weapons": {
							"mainhand": "iron_sword",
						},
                        "attributes": [
							("generic.attack_knockback", 0.0)
                        ]
                    }
                ],
            },
			{
                "delay": 30,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 7,
						"armor": {
                            "head": "iron_helmet",
							"chestplate": "iron_chestplate",
                        },
						"weapons": {
							"mainhand": "iron_sword",
						},
                        "attributes": ("generic.attack_knockback", 0.0)
                    }
                ],
            },
		]
    },
    # Round 10
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 180,
        "waves": [
            {
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 50,
                        "attributes": ("generic.max_health", 1)
                    }
                ]
            },
            {
                "delay": 50,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 50,
                        "attributes": ("generic.max_health", 1)
                    }
                ]
            },
            {
                "delay": 100,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 50,
                        "attributes": ("generic.max_health", 1)
                    }
                ]
            }
        ]
    },
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
        "time": 40,
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
        "time": 40,
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
                        "type": "witch",
                        "count": 5
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
                        "attributes": ("generic.movement_speed", .4)
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
                    },
                    {
                        "type": "cave_spider",
                        "count": 30
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
                        "count": 20,
                    },
                    {
                        "type": "spider",
                        "count": 20
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
                            "head": "diamond_helmet",
                            "body": "diamond_chestplate",
                        }
                    },
                    {
                        "type": "drowned",
                        "count": 10,
                        "armor": {
                            "body": "iron_chestplate"
                        },
                        "weapons": {
                            "mainhand": {
                                "type": "trident",
                                "enchant": ("loyality", 1)
                            }
                        }
                    },
                ]
            },
            {
                "delay": 20,
                "mobs": [
                    {
                        "type": "skeleton",
                        "count": 20,
                        "armor": {
                            "head": "leather_helmet"
                        },
                        "weapons": {
                            "mainhand": "bow"
                        },
                        "effects": ("invisibility", 1)
                    },
                    {
                        "type": "zombie",
                        "count": 10,
                        "armor": {
                            "head": "netherite_helmet"
                        },
                        "weapons": {
                            "mainhand": "iron_sword"
                        },
                        "attributes": ("generic.movement_speed", .5)
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
                        "count": 20,
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
                        "count": 20,
                        "armor": {
                            "head": "gold_helmet",
                            "body": "gold_chestplate",
                            "legs": "gold_leggings",
                            "feet": "gold_boots"
                        }
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
                        "count": 20,
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
                        "count": 20,
                        "weapons": {
                            "mainhand": "iron_sword",
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
                        "count": 20,
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
                        "count": 10,
                        "weapons": {
                            "mainhand": {
                                "type": "bow",
                                "enchant": ("power", 3)
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
                        "count": 20,
                    }
                ]
            },
            {
                "delay": 10,
                "mobs": [
                    {
                        "type": "zombie",
                        "count": 30,
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
                        "count": 20,
                        "armor": {
                            "head": "gold_helmet",
                            "body": "diamond_chestplate",
                            "legs": "gold_leggings",
                            "feet": "gold_boots"
                        },
                        "weapons": {
                            "mainhand": "iron_sword"
                        },
                        "attributes": ("generic.max_health", 50)
                    }
                ]
            }
        ]
    }
]
