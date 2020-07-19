cmd = "execute if entity @a[scores={{hlevel={_lvl}}}] run attribute @a[scores={{hlevel={_lvl}}},limit=1] minecraft:generic.max_health base set {_newMCHealth}"

num_levels = 8

def Build():
    lines = []
    for lvl in range(num_levels+1):
        newMCHealth = 14+2*lvl
        lines.append(cmd.format(_lvl = lvl, _newMCHealth = newMCHealth))
    lines.append(cmd.format(_lvl = lvl+1, _newMCHealth = 40))

    f = open("health_level_system.mcfunction", 'w')
    f.write("\n".join(lines))
    f.close()

Build()
