execute if score #arena round matches 1..25 run function arena:rounds/easy_rounds
execute if score #arena round matches 26..50 run function arena:rounds/normal_rounds
execute if score #arena round matches 51..75 run function arena:rounds/hard_rounds
execute if score #arena round matches 76..100 run function arena:rounds/impossible_rounds

execute if score #arena timer matches 2.. run scoreboard players remove #arena timer 1
execute if score #arena start matches 2.. run scoreboard players set #arena start 1
