execute if entity @a[scores={meleedamage=525839..,mlevel=44}] run tellraw @a[scores={meleedamage=525839..,mlevel=44}] ["",{"text":"Melee Level Up!","bold":true,"color":"gold"},{"text":" Level 44","color":"dark_gray"},{"text":" -> ","color":"gray"},{"text":"Level 45 \n","bold":true,"color":"white"},{"text":"Attack","bold":true,"color":"yellow"},{"text":" 2.0","color":"dark_gray"},{"text":" ->","color":"gray"},{"text":" 2.5","bold":true,"color":"white"}]
execute at @a[scores={meleedamage=525839..,mlevel=44}] run tellraw @a[distance=.01..40] {"text":"","color":"gold","extra":[{"selector":"@a[scores={meleedamage=525839..,mlevel=44}]"},{"text":" is now Melee Level 45"}]}
execute at @a[scores={meleedamage=525839..,mlevel=44}] run tellraw @a[] {"text":"Congratulate ","color":"gold","extra":[{"selector":"@a[scores={meleedamage=525839..,mlevel=44}]"},{"text":" for reaching the max Melee Level 45!"}]}
execute if entity @a[scores={mlevel=45}] run attribute @a[scores={mlevel=45},limit=1] minecraft:generic.attack_speed base set 4.16