execute if entity @a[scores={meleedamage=481503..,mlevel=43}] run tellraw @a[scores={meleedamage=481503..,mlevel=43}] ["",{"text":"Melee Level Up!","bold":true,"color":"gold"},{"text":" Level 43","color":"dark_gray"},{"text":" -> ","color":"gray"},{"text":"Level 44 \n","bold":true,"color":"white"},{"text":"Attack Speed","bold":true,"color":"yellow"},{"text":" 0.14","color":"dark_gray"},{"text":" ->","color":"gray"},{"text":" 0.15","bold":true,"color":"white"}]
execute if entity @a[scores={meleedamage=481503..,mlevel=43}] run execute at @a[scores={meleedamage=481503..,mlevel=43}] run playsound minecraft:entity.player.levelup master @a ~ ~ ~ 1 1.2
execute at @a[scores={meleedamage=481503..,mlevel=43}] run tellraw @a[distance=.01..40] {"text":"","color":"gold","extra":[{"selector":"@a[scores={meleedamage=481503..,mlevel=43}]"},{"text":" is now Melee Level 44"}]}
execute if entity @a[scores={meleedamage=481503..,mlevel=43}] run scoreboard players set @a[scores={meleedamage=481503..,mlevel=43}] mlevel 44
execute if entity @a[scores={mlevel=44}] run attribute @a[scores={mlevel=44},limit=1] minecraft:generic.attack_speed base set 4.15