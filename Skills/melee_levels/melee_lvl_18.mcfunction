execute if entity @a[scores={meleedamage=46011..,mlevel=18}] run tellraw @a[scores={meleedamage=46011..,mlevel=18}] ["",{"text":"Melee Level Up!","bold":true,"color":"gold"},{"text":" Level 18","color":"dark_gray"},{"text":" -> ","color":"gray"},{"text":"Level 19 \n","bold":true,"color":"white"},{"text":"Attack Speed","bold":true,"color":"yellow"},{"text":" -0.06","color":"dark_gray"},{"text":" ->","color":"gray"},{"text":" -0.05","bold":true,"color":"white"}]
execute at @a[scores={meleedamage=46011..,mlevel=18}] run tellraw @a[distance=.01..40] {"text":"","color":"gold","extra":[{"selector":"@a[scores={meleedamage=46011..,mlevel=18}]"},{"text":" is now Melee Level 19"}]}
execute at @a[scores={meleedamage=46011..,mlevel=18}] run tellraw @a[] {"text":"Congratulate ","color":"gold","extra":[{"selector":"@a[scores={meleedamage=46011..,mlevel=18}]"},{"text":" for reaching the max Melee Level 19!"}]}
execute if entity @a[scores={mlevel=19}] run attribute @a[scores={mlevel=19},limit=1] minecraft:generic.attack_speed base set 3.95
execute if entity @a[scores={mlevel=19}] run attribute @a[scores={mlevel=19},limit=1] minecraft:generic.attack_damage base set -0.1