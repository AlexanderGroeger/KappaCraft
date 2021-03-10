from letters import letters
import sys
import os

try:
    code = sys.argv[1].lower()
    if len(code) > 10 or not code.isalpha():
        raise Exception
except:
    sys.exit("Please supply a code using no more than 10 A-Z characters.")

checkCmd = "execute if block ~ ~ ~-_pos minecraft:player_head{_data} run _cmd"
stopCmd = "scoreboard players set #code match 1"

cmd = checkCmd

for i, c in enumerate(code):
    cmd = cmd.replace("_pos",str(1+i)).replace("_data",letters[c]).replace("_cmd",stopCmd if i+1 == len(code) else checkCmd)

with open("code_{}.mcfunction".format(code),'w') as f:
    f.write(cmd)
