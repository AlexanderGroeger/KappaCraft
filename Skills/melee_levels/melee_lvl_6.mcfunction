execute if entity @a[scores={meleedamage=9199..,mlevel=6}] run tellraw @a[scores={meleedamage=9199..,mlevel=6}] ["",{"text":"Melee Level Up!","bold":true,"color":"gold"},{"text":" Level 6","color":"dark_gray"},{"text":" -> ","color":"gray"},{"text":"Level 7 \n","bold":true,"color":"white"},{"text":"Attack Speed","bold":true,"color":"yellow"},{"text":" -0.15","color":"dark_gray"},{"text":" ->","color":"gray"},{"text":" -0.14","bold":true,"color":"white"}]
execute at @a[scores={meleedamage=9199..,mlevel=6}] run tellraw @a[distance=.01..40] {"text":"","color":"gold","extra":[{"selector":"@a[scores={meleedamage=9199..,mlevel=6}]"},{"text":" is now Melee Level 7"}]}
execute at @a[scores={meleedamage=9199..,mlevel=6}] run tellraw @a[] {"text":"Congratulate ","color":"gold","extra":[{"selector":"@a[scores={meleedamage=9199..,mlevel=6}]"},{"text":" for reaching the max Melee Level 7!"}]}
execute if entity @a[scores={mlevel=7}] run attribute @a[scores={mlevel=7},limit=1] minecraft:generic.attack_speed base set 3.86
execute if entity @a[scores={mlevel=7}] run attribute @a[scores={mlevel=7},limit=1] minecraft:generic.attack_damage base set -1.3