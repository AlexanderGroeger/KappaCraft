scoreboard players add @a MOBEFFECT 1
execute if entity @a[scores={MOBEFFECT=100..}] run effect give @e[type=zombie] minecraft:strength 1000000 1 true
execute if entity @a[scores={MOBEFFECT=100..}] run effect give @e[type=zombie] minecraft:resistance 1000000 1 true
execute if entity @a[scores={MOBEFFECT=100..}] run effect give @e[type=skeleton] minecraft:resistance 1000000 0 true
execute if entity @a[scores={MOBEFFECT=100..}] run effect give @e[type=spider] minecraft:speed 1000000 0 true
execute if entity @a[scores={MOBEFFECT=100..}] run effect give @e[type=spider] minecraft:strength 1000000 0 true
execute if entity @a[scores={MOBEFFECT=100..}] run effect give @e[type=wither_skeleton] minecraft:speed 1000000 0 true
execute if entity @a[scores={MOBEFFECT=100..}] run effect give @e[type=cave_spider] minecraft:strength 1000000 1 true
execute if entity @a[scores={MOBEFFECT=100..}] run scoreboard players set @a MOBEFFECT 0
scoreboard players add @a TIME 1
execute if entity @a[scores={TIME=72000..}] run scoreboard players add @a[scores={TIME=72000..}] Money 25
execute if entity @a[scores={TIME=72000..}] run tellraw @a[scores={TIME=72000..}] ["",{"text":"You've played for an hour! Here's $25 as a compliment.","color":"gray"}]
execute if entity @a[scores={TIME=72000..}] run scoreboard players set @a[scores={TIME=72000..}] TIME 0
execute if entity @a[scores={Mart=1..}] run scoreboard players enable @a[scores={Mart=1..}] Mart
execute at @a[scores={Mart=1..}] if entity @e[distance=..10,type=!minecraft:player] run scoreboard players set @a[scores={Mart=1}] Mart 2
execute if entity @a[scores={Mart=1}] run gamemode adventure @a[scores={Mart=1}]
execute if entity @a[scores={Mart=1}] run scoreboard players set @a[scores={Mart=1}] INSHOP 1
execute if entity @a[scores={Mart=1}] run execute in minecraft:overworld run tp @a[scores={Mart=1}] 29999888 192.00 29999833 720.19 0.69
tellraw @a[scores={Mart=2}] ["",{"text":"You're too close to mobs! Move somewhere else.","bold":true,"color":"white"}]
playsound minecraft:block.anvil.place master @a[scores={Mart=2}] ~ ~ ~ 500
execute if entity @a[scores={Mart=1..}] run scoreboard players set @a[scores={Mart=1..}] Mart 0
scoreboard players add @a TEAM 1
execute at @a[scores={TEAM=100..,PVP=..0}] run effect give @a[distance=0.1..15,scores={PVP=..0}] haste 21 0 true
execute at @a[scores={TEAM=100..,PVP=..0}] run effect give @a[distance=0.1..15,scores={PVP=..0}] regeneration 21 0 true
execute at @a[scores={TEAM=100..,PVP=..0}] run effect give @a[distance=0.1..15,scores={PVP=..0}] strength 21 0 true
execute if entity @a[scores={TEAM=100..}] run scoreboard players set @a TEAM 0
execute if entity @a[scores={tp=1..}] run execute at @a[scores={tp=0,INSHOP=0}] run execute if block ~ ~-1 ~ minecraft:fletching_table run tp @p[scores={tp=1..}] @p[scores={tp=0}]
execute if entity @a[scores={tp=1..}] run scoreboard players enable @a tp
execute as @a[scores={tp=1..}] run scoreboard players set @a tp 0
