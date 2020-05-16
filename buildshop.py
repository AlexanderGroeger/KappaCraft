import copy
from shop import shopDeals

def AddBackslashes(cmd):
    result = ""
    nested = False
    quote = False
    bracket = False
    for c in cmd:
        if c == "\"":
            if not nested:
                quote = not quote
            result += "\\"*(2+4*int(nested))
        elif c == "[" and quote:
            nested = True
        elif c == "]" and quote:
            nested = False
        result+=c
    return result

def FormatCommand(mcname,data,mode):

    position = data[mode]["p"]
    if "$" in data[mode]:
        value = str(data[mode]["$"])
    else:
        value = None

    if mode == "Buy" or mode == "Sell":
        quantity = str(data[mode]["n"])
        name = AddBackslashes(data["Name"][int(int(quantity) > 1)])
        line3 = ""
        if len(quantity+name) > 11 and " " in name:
            name, line3 = name.split(" ")

    elif mode == "Custom":
        name = mcname

    if mode == "Sell":

        command = ("data merge block {_position} "
            +"{{Text1:'{{\"text\":\"Sell\",\"clickEvent\":{{\"action\":\"run_command\",\"value\":\""
            +"execute as @s store result score @s TEMPVALUE run clear @s minecraft:{_mcname} 0\""
            +"}},\"bold\":true,\"color\":\"dark_green\"}}',Text2:'{{\"text\":\"{_quantity} {_name}\""
            +",\"clickEvent\":{{\"action\":\"run_command\",\"value\":\""
            +"execute if score @s TEMPVALUE matches {_quantity}.. run scoreboard players add @s Money {_value}\""
            +"}},\"bold\":true}}',Text3:'{{\"text\":\"{_line3}\""
            +",\"clickEvent\":{{\"action\":\"run_command\",\"value\":\""
            +"execute if score @s TEMPVALUE matches {_quantity}.. run clear @s minecraft:{_mcname} {_quantity}\""
            +"}},\"bold\":true}}',Text4:'{{\"text\":\"${_value}\",\"clickEvent\":{{\"action\":\"run_command\",\"value\":\""
            +"scoreboard players set @s TEMPVALUE 0\"}},\"bold\":true}}'}}").format(_position = position, _value = value, _mcname = mcname, _name = name, _quantity = quantity, _line3 = line3)

    elif mode == "Buy":

        command = ("data merge block {_position} "
            +"{{Text1:'{{\"text\":\"Buy\",\"clickEvent\":{{\"action\":\"run_command\",\"value\":\""
            +"execute if score @s Money matches {_value}.. run give @s minecraft:{_mcname} {_quantity}"
            +"\"}},\"bold\":true,\"color\":\"red\"}}',Text2:'{{\"text\":\"{_quantity} {_name}\""
            +",\"clickEvent\":{{\"action\":\"run_command\",\"value\":\""
            +"execute if score @s Money matches {_value}.. run scoreboard players remove @s Money {_value}"
            +"\"}},\"bold\":true}}',Text3:'{{\"text\":\"{_line3}\",\"bold\":true}}',"
            +"Text4:'{{\"text\":\"${_value}\",\"bold\":true}}'}}").format(_position = position, _value = value, _mcname = mcname, _name = name, _quantity = quantity, _line3 = line3)

    elif mode == "Custom":

        textLines = copy.deepcopy(data["TextLines"])
        cmds = copy.deepcopy(data[mode]["cmds"])
        if value:
            cmds[0] = "execute if score @s Money matches {}.. run ".format(value)+cmds[0]
            cmds.append("execute if score @s Money matches {}.. run scoreboard players remove @s Money {}".format(value,value))
        command = "data merge block {} {{".format(position)
        lines = []
        endLine = False
        for i in range(4):
            text = ""
            line = textLines[i] if i < len(textLines) else None
            cmd = AddBackslashes(cmds[i]) if i < len(cmds) else None
            # if not cmd and not line and endLine:
            #     break
            text += "Text{}:'{{\"text\":\"".format(str(i+1))
            if value and i == 3:
                text += "${}".format(str(value))
            if not line and not endLine:
                endLine = True
            if not endLine:
                if line:
                    text += line["text"]
            text += "\""
            if cmd:
                text += ",\"clickEvent\":{{\"action\":\"run_command\",\"value\":\"{}\"}}".format(cmd)
            if line or endLine:
                text += ",\"bold\":true"
            if line and "color" in line:
                text += ",\"color\":\"{}\"".format(line["color"])
            text += "}'"
            lines.append(text)
        command += ",".join(lines)
        command += "}"
    return command


def Build():
    cmds = []
    for name, data in shopDeals.items():
        if "Buy" in data:
            cmds.append(FormatCommand(name,data,"Buy"))
        if "Sell" in data:
            cmds.append(FormatCommand(name,data,"Sell"))
        if "Custom" in data:
            cmds.append(FormatCommand(name,data,"Custom"))

    f = open("shop.mcfunction", 'w')
    f.write("\n".join(cmds))
    f.close()

Build()
