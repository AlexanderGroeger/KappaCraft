execute if entity @a[scores={meleedamage=51152..,mlevel=19}] run tellraw @a[scores={meleedamage=51152..,mlevel=19}] ["",{"text":"Melee Level Up!","bold":true,"color":"gold"},{"text":" Level 19","color":"dark_gray"},{"text":" -> ","color":"gray"},{"text":"Level 20 \n","bold":true,"color":"white"},{"text":"Attack","bold":true,"color":"yellow"},{"text":" -0.5","color":"dark_gray"},{"text":" ->","color":"gray"},{"text":" 0.0","bold":true,"color":"white"}]
execute at @a[scores={meleedamage=51152..,mlevel=19}] run tellraw @a[distance=.01..40] {"text":"","color":"gold","extra":[{"selector":"@a[scores={meleedamage=51152..,mlevel=19}]"},{"text":" is now Melee Level 20"}]}
execute at @a[scores={meleedamage=51152..,mlevel=19}] run tellraw @a[] {"text":"Congratulate ","color":"gold","extra":[{"selector":"@a[scores={meleedamage=51152..,mlevel=19}]"},{"text":" for reaching the max Melee Level 20!"}]}
execute if entity @a[scores={mlevel=20}] run attribute @a[scores={mlevel=20},limit=1] minecraft:generic.attack_speed base set 3.96