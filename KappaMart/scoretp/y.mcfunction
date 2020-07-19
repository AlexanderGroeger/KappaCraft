summon minecraft:area_effect_cloud ~ ~ ~ {CustomName:scoretp_y_hejgb,Duration:1,Particle:take}
tp @e[type=area_effect_cloud,name=scoretp_y_hejgb] @s
tp @e[type=area_effect_cloud,name=scoretp_y_hejgb] ~ -4096 ~

scoreboard players operation @e[type=area_effect_cloud,name=scoretp_y_hejgb] scoretp_y = @s scoretp_y
scoreboard players add @e[type=area_effect_cloud,name=scoretp_y_hejgb] scoretp_y 4096

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=4096] ~ ~4096 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=4096] scoretp_y 4096

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=2048] ~ ~2048 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=2048] scoretp_y 2048

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=1024] ~ ~1024 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=1024] scoretp_y 1024

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=512] ~ ~512 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=512] scoretp_y 512

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=256] ~ ~256 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=256] scoretp_y 256

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=128] ~ ~128 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=128] scoretp_y 128

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=64] ~ ~64 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=64] scoretp_y 64

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=32] ~ ~32 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=32] scoretp_y 32

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=16] ~ ~16 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=16] scoretp_y 16

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=8] ~ ~8 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=8] scoretp_y 8

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=4] ~ ~4 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=4] scoretp_y 4

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=2] ~ ~2 ~
scoreboard players remove @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=2] scoretp_y 2

tp @e[type=area_effect_cloud,name=scoretp_y_hejgb,score_scoretp_y_min=1] ~ ~1 ~

tp @s @e[type=area_effect_cloud,name=scoretp_y_hejgb]
kill @e[type=area_effect_cloud,name=scoretp_y_hejgb]