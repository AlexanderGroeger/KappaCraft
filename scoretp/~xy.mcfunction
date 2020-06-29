summon minecraft:area_effect_cloud ~ ~ ~ {CustomName:scoretp_xy_hejgb,Duration:1,Particle:take}
tp @e[type=area_effect_cloud,name=scoretp_xy_hejgb] @s

scoreboard players operation @e[type=area_effect_cloud,name=scoretp_xy_hejgb] scoretp_x = @s scoretp_x
scoreboard players operation @e[type=area_effect_cloud,name=scoretp_xy_hejgb] scoretp_y = @s scoretp_y

execute @e[type=area_effect_cloud,name=scoretp_xy_hejgb] ~ ~ ~ function scoretp:~x
execute @e[type=area_effect_cloud,name=scoretp_xy_hejgb] ~ ~ ~ function scoretp:y

tp @s @e[type=area_effect_cloud,name=scoretp_xy_hejgb]
kill @e[type=area_effect_cloud,name=scoretp_xy_hejgb]