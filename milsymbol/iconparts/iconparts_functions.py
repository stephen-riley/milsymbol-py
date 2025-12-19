def defaultProperties(instructions, iconColor):
    if isinstance(instructions, dict) or isinstance(instructions, list):
        if isinstance(instructions, list):
            for i in range(len(instructions)):
                defaultProperties(instructions[i], iconColor)
            return

        instructions["icon"] = True

        if instructions.get("type") == "text":
            if "fontfamily" not in instructions:
                instructions["fontfamily"] = "Arial"
            if "fontweight" not in instructions:
                instructions["fontweight"] = "bold"
            if "textanchor" not in instructions:
                instructions["textanchor"] = "middle"
            if "stroke" not in instructions:
                instructions["stroke"] = False

        if "fill" not in instructions:
            instructions["fill"] = iconColor
        if "stroke" not in instructions:
            instructions["stroke"] = iconColor
        if "strokewidth" not in instructions:
            instructions["strokewidth"] = 3
        return


def text(s):
    size = 45
    if len(s) == 1:
        size = 45
    if len(s) == 3:
        size = 39
    if len(s) >= 4:
        size = 33

    return {
        "type": "text",
        "stroke": False,
        "textanchor": "middle",
        "alignmentBaseline": "middle",
        "x": 100,
        "y": 103,
        "fontsize": size,
        "text": s,
    }


def textm1(s):
    size = 28
    if len(s) == 3:
        size = 25
    if len(s) >= 4:
        size = 22

    return {
        "type": "text",
        "stroke": False,
        "textanchor": "middle",
        "alignmentBaseline": "middle",
        "x": 100,
        "y": 71,
        "fontsize": size,
        "text": s,
    }


def textm2(s):
    size = 28
    if len(s) == 3:
        size = 25
    if len(s) >= 4:
        size = 20

    return {
        "type": "text",
        "stroke": False,
        "textanchor": "middle",
        "alignmentBaseline": "middle",
        "x": 100,
        "y": 134,
        "fontsize": size,
        "text": s,
    }
