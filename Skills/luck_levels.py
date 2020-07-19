cmd = "execute if entity @a[scores={{llevel={_lvl}}}] run attribute @a[scores={{llevel={_lvl}}},limit=1] minecraft:generic.luck base set {_newMCLuck:.2f}"

num_levels = 20

def Build():
    lines = []
    for lvl in range(num_levels+1):
        newMCLuck = lvl/4
        lines.append(cmd.format(_lvl = lvl, _newMCLuck = newMCLuck))

    f = open("luck_level_system.mcfunction", 'w')
    f.write("\n".join(lines))
    f.close()

Build()
