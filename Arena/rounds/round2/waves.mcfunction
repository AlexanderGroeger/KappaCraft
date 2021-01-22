execute if score #arena timer matches 6001 run scoreboard players set #arena spawns_left 21
execute if score #arena timer matches 6001 run function arena:rounds/round2/wave1
execute if score #arena timer matches 5601 run scoreboard players set #arena spawns_left 21
execute if score #arena timer matches 5601 run function arena:rounds/round2/wave2
execute if score #arena timer matches 5601 run scoreboard players set #arena finished_spawns 2