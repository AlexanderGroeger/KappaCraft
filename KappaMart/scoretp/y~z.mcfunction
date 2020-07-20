summon minecraft:area_effect_cloud ~ ~ ~ {CustomName:scoretp_yz_hejgb,Duration:1,Particle:take}
tp @e[type=area_effect_cloud,name=scoretp_yz_hejgb] @s

scoreboard players operation @e[type=area_effect_cloud,name=scoretp_yz_hejgb] scoretp_y = @s scoretp_y
scoreboard players operation @e[type=area_effect_cloud,name=scoretp_yz_hejgb] scoretp_z = @s scoretp_z

execute @e[type=area_effect_cloud,name=scoretp_yz_hejgb] ~ ~ ~ function scoretp:y
execute @e[type=area_effect_cloud,name=scoretp_yz_hejgb] ~ ~ ~ function scoretp:~z

tp @s @e[type=area_effect_cloud,name=scoretp_yz_hejgb]
kill @e[type=area_effect_cloud,name=scoretp_yz_hejgb]