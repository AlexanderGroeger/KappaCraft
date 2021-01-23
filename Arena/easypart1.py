rounds = [
    # Round 1
    {
        # Gives player $3 for completing round
        "bonus": 3,
        # Loot table of all mobs unless otherwise overwritten
        "loot": "loot:arena/tier1mob",
        # Time in seconds that players must complete the round
        "time": 300,

        "waves": [
            {
                # Time delay before this wave spawns
                "delay": 0,
                # Loot Table
                "loot": "loot:arena/tier1chest"
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
                        "loot": "loot:arena/tier1chest",
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
        "time": 300,
        # Needs mobs
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
        "time": 300,
        # Needs mobs
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
                    }
                ],
            },
			{
                "delay": 0,
                "mobs": [
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
        "time": 300,
        # Needs mobs
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
        "time": 300,
        # Needs mobs
        "waves": [
			{
                "delay": 0,
                "mobs": [
                    {
                        "type": "silverfish",
						"count": 15,
                        "attributes": [
							("generic.movement_speed", 0.9)
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
        "time": 300,
        # Needs mobs
        "waves": [
			{
                "delay": 0,
                "mobs": [
                    {
                        "type": "zombie",
						"count": 10,
                        "attributes": [
							("generic.movement_speed", 0.9)
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
        "time": 300,
        # Needs mobs
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
							("generic.movement_speed", 0.6)
							
                    }
                ],
            },
		]
    },
	# Round 8
    {
        "bonus": 3,
        "loot": "loot:arena/tier1mob",
        "time": 300,
        # Needs mobs
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
							("generic.attack_knockback", 0.9)
							
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
							("generic.attack_knockback", 0.9)
							
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
        "time": 300,
        # Needs mobs
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
                        "attributes": [
							("generic.attack_knockback", 0.0)
							
                    }
                ],
            },
		]
    },
]
