execute if block 29 133 20 minecraft:flower_pot run scoreboard players set @s TEMPVALUE -5
execute if block 31 133 20 minecraft:flower_pot run scoreboard players set @s TEMPVALUE -5
execute if block 29 133 22 minecraft:flower_pot run scoreboard players set @s TEMPVALUE -5
execute if block 31 133 22 minecraft:flower_pot run scoreboard players set @s TEMPVALUE -5
execute if entity @s[scores={TEMPVALUE=0}] run execute at @s run summon firework_rocket ~ ~1 ~ {LifeTime:15,FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Flight:1,Explosions:[{Type:1,Flicker:1,Trail:1,Colors:[I;11743532,3887386,11250603],FadeColors:[I;14188952,4312372,15790320]}]}}}}
scoreboard players set @s TEMPVALUE 0
