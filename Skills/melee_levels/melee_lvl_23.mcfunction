execute if entity @a[scores={meleedamage=76779..,mlevel=23}] run tellraw @a[scores={meleedamage=76779..,mlevel=23}] ["",{"text":"Melee Level Up!","bold":true,"color":"gold"},{"text":" Level 23","color":"dark_gray"},{"text":" -> ","color":"gray"},{"text":"Level 24 \n","bold":true,"color":"white"},{"text":"Attack Speed","bold":true,"color":"yellow"},{"text":" -0.02","color":"dark_gray"},{"text":" ->","color":"gray"},{"text":" -0.01","bold":true,"color":"white"}]
execute at @a[scores={meleedamage=76779..,mlevel=23}] run tellraw @a[distance=.01..40] {"text":"","color":"gold","extra":[{"selector":"@a[scores={meleedamage=76779..,mlevel=23}]"},{"text":" is now Melee Level 24"}]}
execute at @a[scores={meleedamage=76779..,mlevel=23}] run tellraw @a[] {"text":"Congratulate ","color":"gold","extra":[{"selector":"@a[scores={meleedamage=76779..,mlevel=23}]"},{"text":" for reaching the max Melee Level 24!"}]}
execute if entity @a[scores={mlevel=24}] run attribute @a[scores={mlevel=24},limit=1] minecraft:generic.attack_speed base set 3.99
execute if entity @a[scores={mlevel=24}] run attribute @a[scores={mlevel=24},limit=1] minecraft:generic.attack_damage base set 0.4