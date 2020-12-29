import os
from cmds import *

def WriteMeleeFunctions():
    meleeAttackSpeedAttributeCmd = executeIf + Format(attribute, attribute = "generic.attack_speed", attrivalue = "___newMCSpeed")
    meleeAttackDamageAttributeCmd = executeIf + Format(attribute, attribute = "generic.attack_damage", attrivalue = "___newMCAttack")
    num_levels = 50
    max_attack_speed_boost = .4
    max_attack_boost = 5
    base_exp = 1000
    exp_gain_percent = 9

    lines = []
    totalExp = 0

    # Generate root of tree
    for oldLvl in range(num_levels+1):
        newLvl = oldLvl + 1
        oldSpeed = (oldLvl)/num_levels*max_attack_speed_boost - .2
        newSpeed = (newLvl)/num_levels*max_attack_speed_boost - .2

        oldAttack = round((newLvl-5)/num_levels*max_attack_boost - 2, 3)
        newAttack = round((newLvl)/num_levels*max_attack_boost - 2, 1)

        oldMCSpeed = 4 + oldSpeed
        oldMCAttack = oldAttack
        newMCSpeed = 4 + newSpeed
        newMCAttack = newAttack

        lines.append(
            Format(
                meleeAttackSpeedAttributeCmd,
                target = Format(targetOldLvl, levelName = "mlevel", newLvl = oldLvl),
                newMCSpeed = "{:.3f}".format(oldMCSpeed),
                oldLvl = oldLvl,
            )
        )

        lines.append(
            Format(
                meleeAttackDamageAttributeCmd,
                target = Format(targetOldLvl, levelName = "mlevel", oldLvl = oldLvl),
                newMCAttack = "{:.1f}".format(oldMCAttack),
                oldLvl = oldLvl,
            )
        )

        if oldLvl < num_levels:
            exp = int(base_exp*(1+(exp_gain_percent/100.))**oldLvl)
            totalExp += exp
            lines.append(
                Format(
                    branchCmd,
                    target = targetExpOldLvl,
                    system = "melee",
                    scoreExp = "meleedamage",
                    levelName = "mlevel",
                    exp = totalExp,
                    oldLvl = oldLvl,
                )
            )


    lines.append("scoreboard players set @a didmeleedamage 0")
    lines.append("scoreboard players set @a died 0")

    with open("melee_level_system.mcfunction", 'w') as f:
        f.write("\n".join(lines))


    # Generate Tree Branches
    totalExp = 0
    for oldLvl in range(num_levels):

        exp = int(base_exp*(1+(exp_gain_percent/100.))**oldLvl)
        totalExp += exp
        newLvl = oldLvl + 1

        if newLvl % 5:
            awardType = "Attack Speed"
        else:
            awardType = "Attack Damage"

        oldSpeed = (oldLvl)/num_levels*max_attack_speed_boost - .2
        newSpeed = (newLvl)/num_levels*max_attack_speed_boost - .2

        oldAttack = round((newLvl-5)/num_levels*max_attack_boost - 2, 3)
        newAttack = round((newLvl)/num_levels*max_attack_boost - 2, 1)

        newMCSpeed = 4 + newSpeed
        newMCAttack = newAttack

        targetLvlTransition = Format(
            targetExpOldLvl,
            scoreExp = "meleedamage",
            exp = totalExp,
            levelName = "mlevel",
            oldLvl = oldLvl,
        )

        lines = []

        # Determine which lines go where
        lines.append(levelNotificationCmd+awardTextCmds[awardType])
        if newLvl == num_levels or newLvl == int(num_levels/2):
            lines.append(luckNotificationCmd)
            lines.append(luckScoreboardCmd)
        if newLvl == num_levels:
            lines.append(heartNotificationCmd)
            lines.append(heartScoreboardCmd)
        lines.append(levelAnnouncementCmd)
        if newLvl == num_levels:
            lines.append(levelMaxAnnouncementCmd)
        lines.append(soundLevelUpCmd)
        lines.append(Format(levelScoreboardCmd, score_mode = "set", scoreboard = "mlevel", score_value = newLvl))


        for i, line in enumerate(lines):
            lines[i] = Format(
                line,
                target = targetLvlTransition,
                oldLvl = oldLvl,
                newLvl = newLvl,
                levelName = "mlevel",
                levelTypeName = "Melee",
                scoreExp = "meleedamage",
                exp = totalExp,
                oldSpeed = "{:.3f}".format(oldSpeed),
                newSpeed = "{:.3f}".format(newSpeed),
                newMCSpeed = "{:.3f}".format(newMCSpeed),
                oldAttack = "{:.1f}".format(oldAttack),
                newAttack = "{:.1f}".format(newAttack),
                newMCAttack = "{:.1f}".format(newMCAttack),
                awardText = awardTextCmds[awardType]
            )

        folder = "melee_levels"
        if not os.path.isdir(folder):
            os.mkdir(folder)
        with open(os.path.join(folder,"melee_lvl_{}.mcfunction".format(oldLvl)), 'w') as f:
            f.write("\n".join(lines))

if __name__ == "__main__":
    WriteMeleeFunctions()
