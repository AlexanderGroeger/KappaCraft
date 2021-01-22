execute if score #arena start matches 2.. run execute if score #arena round matches 1 run scoreboard players set #arena timer 6001
execute if score #arena round matches 1 run function arena:rounds/round1/waves.mcfunction
execute if score #arena start matches 2.. run execute if score #arena round matches 2 run scoreboard players set #arena timer 6001
execute if score #arena round matches 2 run function arena:rounds/round2/waves.mcfunction