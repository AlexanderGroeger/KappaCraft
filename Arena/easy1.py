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
                        "count": 7,
                        "armor": {
                            "head": "leather_helmet",
                            "body": "leather_chestplate"
						}
                    },
                    {
                        "type": "skeleton",
                        "count": 4,
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
						"count": 7,
                        "armor": {
                            "head": "leather_helmet",
                        },
						"weapons": {
							"mainhand": "wooden_hoe",
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
							"mainhand": "wooden_hoe",
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
							"mainhand": "stone_hoe",
						},
                    },
                    {
                        "type": "spider",
						"count": 3,
                    }
                ],
            },
			{
                "delay": 20,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 4,
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
						"count": 12,
						"attributes": [
							("generic.movement_speed", 0.34)
						],
                        "armor": {
                            "head": "leather_helmet",
                        },
						"weapons": {
							"mainhand": "wooden_hoe",
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
						"count": 10,
                        "attributes": [
							("generic.movement_speed", 0.35)
                        ]
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
						"count": 5,
                        "attributes": [
							("generic.movement_speed", 0.37)
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
						"count": 15,
						"armor": {
                            "head": "leather_helmet",
							"chestplate": "iron_chestplate",
							"leggings": "leather_leggings",
							"boots": "leather_boots",
                        },
						"weapons": {
							"mainhand": "iron_hoe",
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
							"mainhand": "iron_hoe",
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
						"count": 5,
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
						"count": 4,
						"armor": {
                            "head": "iron_helmet",
							"chestplate": "iron_chestplate",
                        },
						"weapons": {
							"mainhand": "iron_hoe",
						},
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
							"mainhand": "iron_hoe",
						},
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
							"mainhand": "iron_hoe",
						},
                        "attributes": ("generic.attack_knockback", 0.0)
                    }
                ],
            },
		]
    }
]
