import os
from cmds import *

def WriteSprintFunctions():
    sprintSpeedAttributeCmd = executeIf + Format(attribute, attribute = "minecraft:generic.movement_speed", attrivalue = "___newMCSpeed")
    levelName = "slevel"
    expName = "sprint"
    num_levels = 50
    max_sprint_boost_percent = 25
    base_exp = 20000
    exp_gain_percent = 12

    lines = []
    totalExp = 0

    # Generate root of tree
    for oldLvl in range(num_levels+1):
        newLvl = oldLvl + 1
        oldSpeed = (oldLvl)/num_levels*max_sprint_boost_percent
        newSpeed = (newLvl)/num_levels*max_sprint_boost_percent
        oldMCSpeed = round(.1000 + oldSpeed/1000, 4)
        newMCSpeed = round(.1000 + newSpeed/1000, 4)

        lines.append(
            Format(
                sprintSpeedAttributeCmd,
                target = Format(targetOldLvl, levelName = "mlevel", newLvl = oldLvl),
                newMCSpeed = "{:.4f}".format(oldMCSpeed),
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
                    system = "sprint",
                    scoreExp = expName,
                    levelName = levelName,
                    exp = totalExp,
                    oldLvl = oldLvl,
                )
            )


    lines.append("scoreboard players set @a moved 0")
    lines.append("scoreboard players set @a died 0")

    with open("sprint_level_system.mcfunction", 'w') as f:
        f.write("\n".join(lines))


    # Generate Tree Branches
    totalExp = 0
    for oldLvl in range(num_levels):

        exp = int(base_exp*(1+(exp_gain_percent/100.))**oldLvl)
        totalExp += exp
        newLvl = oldLvl + 1

        awardType = "Walk Speed"

        oldSpeed = round((oldLvl)/num_levels*max_sprint_boost_percent,4)
        newSpeed = round((newLvl)/num_levels*max_sprint_boost_percent,4)
        newMCSpeed = round(.1000 + newSpeed/1000,4)

        targetLvlTransition = Format(
            targetExpOldLvl,
            scoreExp = expName,
            exp = totalExp,
            levelName = levelName,
            oldLvl = oldLvl,
        )

        lines = []

        # Determine which lines go where
        lines.append(levelNotificationCmd+awardTextCmds[awardType])
        if newLvl % 5 == 0:
            lines.append(luckNotificationCmd)
            lines.append(luckScoreboardCmd)
        if newLvl == num_levels:
            lines.append(heartNotificationCmd)
            lines.append(heartScoreboardCmd)
        lines.append(levelAnnouncementCmd)
        if newLvl == num_levels:
            lines.append(levelMaxAnnouncementCmd)
        lines.append(soundLevelUpCmd)
        lines.append(Format(levelScoreboardCmd, score_mode = "set", scoreboard = "slevel", score_value = newLvl))


        for i, line in enumerate(lines):
            lines[i] = Format(
                line,
                target = targetLvlTransition,
                oldLvl = oldLvl,
                newLvl = newLvl,
                levelName = levelName,
                levelTypeName = "Sprint",
                scoreExp = expName,
                exp = totalExp,
                oldSpeed = "{:.1f}".format(oldSpeed),
                newSpeed = "{:.1f}".format(newSpeed),
                newMCSpeed = "{:.4f}".format(newMCSpeed),
                awardText = awardTextCmds[awardType]
            )

        folder = "sprint_levels"
        if not os.path.isdir(folder):
            os.mkdir(folder)
        with open(os.path.join(folder,"sprint_lvl_{}.mcfunction".format(oldLvl)), 'w') as f:
            f.write("\n".join(lines))

if __name__ == "__main__":
    WriteSprintFunctions()
