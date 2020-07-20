summon minecraft:area_effect_cloud ~ ~ ~ {CustomName:scoretp_xyz_hejgb,Duration:1,Particle:take}
tp @e[type=area_effect_cloud,name=scoretp_xyz_hejgb] @s

scoreboard players operation @e[type=area_effect_cloud,name=scoretp_xyz_hejgb] scoretp_x = @s scoretp_x
scoreboard players operation @e[type=area_effect_cloud,name=scoretp_xyz_hejgb] scoretp_y = @s scoretp_y
scoreboard players operation @e[type=area_effect_cloud,name=scoretp_xyz_hejgb] scoretp_z = @s scoretp_z

execute @e[type=area_effect_cloud,name=scoretp_xyz_hejgb] ~ ~ ~ function scoretp:x
execute @e[type=area_effect_cloud,name=scoretp_xyz_hejgb] ~ ~ ~ function scoretp:~y
execute @e[type=area_effect_cloud,name=scoretp_xyz_hejgb] ~ ~ ~ function scoretp:z

tp @s @e[type=area_effect_cloud,name=scoretp_xyz_hejgb]
kill @e[type=area_effect_cloud,name=scoretp_xyz_hejgb]