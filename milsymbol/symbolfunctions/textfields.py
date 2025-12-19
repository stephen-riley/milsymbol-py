from .string_width import string_width


def textfields(symbol, ms):
    drawArray1 = []
    drawArray2 = []

    bbox = symbol.metadata["baseGeometry"][
        "bbox"
    ]  # Assuming BBox object or compatible dict

    flag = 70 if symbol.options.get("country_flag") else 0
    flag += 30 if symbol.options.get("signature") == "!" else 0
    stack = float(symbol.options.get("stack", 0)) * 15

    # Helper to get color
    def get_color(color_obj, affiliation):
        if isinstance(color_obj, dict):
            return color_obj.get(affiliation)
        return getattr(color_obj, affiliation, None)

    affiliation = symbol.metadata.get("affiliation")
    icon_colors = symbol.colors.get("iconColor")

    info_color = symbol.style.get("infoColor")
    if isinstance(info_color, dict) or hasattr(info_color, "Friend"):
        fontColor = get_color(info_color, affiliation)
    else:
        fontColor = info_color

    if not fontColor:
        fontColor = get_color(icon_colors, affiliation) or get_color(
            icon_colors, "Friend"
        )

    fontFamily = symbol.style.get("fontfamily")
    fontSize = float(symbol.style.get("infoSize"))

    info_background_obj = symbol.style.get("infoBackground")
    infoBackground = (
        get_color(info_background_obj, affiliation)
        if (
            isinstance(info_background_obj, dict)
            or hasattr(info_background_obj, "Friend")
        )
        else info_background_obj
    )

    infoBackgroundFrame = infoBackground  # JS logic seems to reuse

    gbbox = ms.BBox()
    spaceTextIcon = 20

    # Text helper
    def text_helper(s):
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
            "fontweight": "bold",
            "fontfamily": fontFamily,
            "fill": fontColor,
        }

    # Label Override Helper
    def label_override(label):
        texts = []
        space_text_icon_override = 0

        # Iterating through label properties (which map to options keys)
        # label is a dict where key is option name (e.g. 'quantity') and value is list/obj of label props
        for key, value in label.items():
            option_val = symbol.options.get(key)
            if option_val and option_val != "":
                label_configs = value if isinstance(value, list) else [value]

                for lbl in label_configs:
                    lbl_fontsize = lbl.get("fontsize")
                    lbl_x = lbl.get("x")
                    lbl_y = lbl.get("y")
                    lbl_textanchor = lbl.get("textanchor")

                    labelbox = {"y2": lbl_y, "y1": lbl_y - lbl_fontsize}

                    if lbl_textanchor == "start":
                        labelbox["x1"] = lbl_x
                        labelbox["x2"] = lbl_x + string_width(
                            option_val, lbl_fontsize, space_text_icon_override
                        )
                    elif lbl_textanchor == "middle":
                        w = string_width(
                            option_val, lbl_fontsize, space_text_icon_override
                        )
                        labelbox["x1"] = lbl_x - w / 2
                        labelbox["x2"] = lbl_x + w / 2
                    elif lbl_textanchor == "end":
                        labelbox["x1"] = lbl_x - string_width(
                            option_val, lbl_fontsize, space_text_icon_override
                        )
                        labelbox["x2"] = lbl_x

                    gbbox.merge(labelbox)

                    text_obj = {
                        "type": "text",
                        "fontfamily": fontFamily,
                        "fill": fontColor,
                        "x": lbl_x,
                        "y": lbl_y,
                        "text": option_val,
                    }

                    attr_map = {
                        "alignmentBaseline": "alignmentBaseline",
                        "fill": "fill",
                        "stroke": "stroke",
                        "textanchor": "textanchor",
                        "fontsize": "fontsize",
                        "fontweight": "fontweight",
                    }
                    for k, v in attr_map.items():
                        if k in lbl:
                            text_obj[v] = lbl[k]

                    texts.append(text_obj)
        return texts

    genericSIDC = None

    # Label Caching and Overrides Logic
    # In JS: ms._labelCache and ms._labelOverrides
    # We assume ms object has these.

    if symbol.metadata.get("numberSIDC"):
        # Number based SIDC
        if "number" not in ms._labelCache:
            ms._labelCache["number"] = {}
            # Apply overrides
            overrides = ms._labelOverrides.get("number", [])
            for func in overrides:
                if callable(func):
                    func(
                        symbol, ms._labelCache["number"]
                    )  # Need to check call signature in component overrides
                    # JS: func.call(this, ms._labelCache["number"]) -> 'this' is symbol

        genericSIDC = symbol.metadata.get("functionid")[0:6]

        if symbol.metadata.get("controlMeasure") and genericSIDC in ms._labelCache.get(
            "number", {}
        ):
            drawArray2.extend(label_override(ms._labelCache["number"][genericSIDC]))

            # outline
            if symbol.style.get("outlineWidth", 0) > 0:
                outline_color_obj = symbol.style.get("outlineColor")
                outline_color = outline_color_obj
                if isinstance(outline_color_obj, dict) or hasattr(
                    outline_color_obj, "Friend"
                ):
                    outline_color = get_color(outline_color_obj, affiliation)

                outlined = ms.outline(
                    drawArray2,
                    symbol.style.get("outlineWidth"),
                    symbol.style.get("strokeWidth"),
                    outline_color,
                )
                if outlined:
                    drawArray1.append(outlined)

            return {"pre": drawArray1, "post": drawArray2, "bbox": gbbox}

    else:
        # Letter based SIDC
        if "letter" not in ms._labelCache:
            ms._labelCache["letter"] = {}
            overrides = ms._labelOverrides.get("letter", [])
            for func in overrides:
                if callable(func):
                    func(symbol, ms._labelCache["letter"])

        sidc = symbol.options.get("sidc")
        genericSIDC = sidc[0:1] + "-" + sidc[2:3] + "-" + sidc[4:10]

        if genericSIDC in ms._labelCache.get("letter", {}):
            drawArray2.extend(label_override(ms._labelCache["letter"][genericSIDC]))

            if symbol.style.get("outlineWidth", 0) > 0:
                outline_color_obj = symbol.style.get("outlineColor")
                outline_color = outline_color_obj
                if isinstance(outline_color_obj, dict) or hasattr(
                    outline_color_obj, "Friend"
                ):
                    outline_color = get_color(outline_color_obj, affiliation)

                outlined = ms.outline(
                    drawArray2,
                    symbol.style.get("outlineWidth"),
                    symbol.style.get("strokeWidth"),
                    outline_color,
                )
                if outlined:
                    drawArray1.append(outlined)

            return {"pre": drawArray1, "post": drawArray2, "bbox": gbbox}

    # Check that we have some texts to print
    has_text = any(
        [
            symbol.options.get(k)
            for k in [
                "quantity",
                "reinforcedReduced",
                "staffComments",
                "additionalInformation",
                "evaluationRating",
                "combatEffectiveness",
                "signatureEquipment",
                "higherFormation",
                "hostile",
                "iffSif",
                "sigint",
                "uniqueDesignation",
                "type",
                "dtg",
                "altitudeDepth",
                "location",
                "speed",
                "specialHeadquarters",
                "platformType",
                "equipmentTeardownTime",
                "commonIdentifier",
                "auxiliaryEquipmentIndicator",
                "headquartersElement",
                "installationComposition",
                "guardedUnit",
                "specialDesignator",
            ]
        ]
    )

    if symbol.style.get("infoFields") and has_text:
        if symbol.options.get("specialHeadquarters"):
            drawArray2.append(text_helper(symbol.options.get("specialHeadquarters")))

        if symbol.options.get("quantity") and not symbol.metadata.get("dismounted"):
            drawArray2.append(
                {
                    "type": "text",
                    "text": symbol.options.get("quantity"),
                    "x": 100,
                    "y": getattr(bbox, "y1", 100) - 10,
                    "textanchor": "middle",
                    "fontsize": fontSize,
                    "fontfamily": fontFamily,
                    "fill": fontColor,
                    "stroke": False,
                }
            )
            gbbox.y1 = getattr(bbox, "y1", 100) - 10 - fontSize

        if symbol.options.get("headquartersElement"):
            drawArray2.append(
                {
                    "type": "text",
                    "text": symbol.options.get("headquartersElement"),
                    "x": 100,
                    "y": getattr(bbox, "y2", 100) + 35,
                    "textanchor": "middle",
                    "fontsize": 35,
                    "fontfamily": fontFamily,
                    "fontweight": "bold",
                    "fill": fontColor,
                    "stroke": False,
                }
            )
            gbbox.y2 = getattr(bbox, "y2", 100) + 35

        gStrings = {
            k: "" for k in ["L1", "L2", "L3", "L4", "L5", "R1", "R2", "R3", "R4", "R5"]
        }
        a = []

        # Air & Space
        sidc_numeric = False
        try:
            int(symbol.options.get("sidc", "a"))  # Check if numeric-ish
            sidc_numeric = True
        except ValueError:
            sidc_numeric = False

        if sidc_numeric and symbol.metadata.get("baseDimension") == "Air":
            gStrings["R1"] = symbol.options.get("uniqueDesignation")
            gStrings["R2"] = symbol.options.get("iffSif")
            gStrings["R3"] = symbol.options.get("type")

            if symbol.options.get("speed") or symbol.options.get("altitudeDepth"):
                a = []
                if symbol.options.get("speed"):
                    a.append(symbol.options.get("speed"))
                if symbol.options.get("altitudeDepth"):
                    a.append(symbol.options.get("altitudeDepth"))
                gStrings["R4"] = "/".join(a)

            if symbol.options.get("staffComments") or symbol.options.get(
                "additionalInformation"
            ):
                a = []
                if symbol.options.get("staffComments"):
                    a.append(symbol.options.get("staffComments"))
                if symbol.options.get("additionalInformation"):
                    a.append(symbol.options.get("additionalInformation"))
                gStrings["R5"] = "/".join(a)

        # Land or letterbased SIDC
        if not sidc_numeric or symbol.metadata.get("baseDimension") == "Ground":
            gStrings["L1"] = symbol.options.get("dtg")

            if symbol.options.get("altitudeDepth") or symbol.options.get("location"):
                a = []
                if symbol.options.get("altitudeDepth"):
                    a.append(symbol.options.get("altitudeDepth"))
                if symbol.options.get("location"):
                    a.append(symbol.options.get("location"))
                gStrings["L2"] = "/".join(a)

            gStrings["L4"] = symbol.options.get("uniqueDesignation")
            gStrings["L5"] = symbol.options.get("speed")
            gStrings["R2"] = symbol.options.get("staffComments")
            gStrings["R4"] = symbol.options.get("higherFormation")

            if any(
                [
                    symbol.options.get(k)
                    for k in [
                        "evaluationRating",
                        "combatEffectiveness",
                        "signatureEquipment",
                        "hostile",
                        "iffSif",
                    ]
                ]
            ):
                a = []
                for k in [
                    "evaluationRating",
                    "combatEffectiveness",
                    "signatureEquipment",
                    "hostile",
                    "iffSif",
                ]:
                    if symbol.options.get(k):
                        a.append(symbol.options.get(k))
                gStrings["R5"] = "/".join(a)

            if not sidc_numeric or symbol.metadata.get("unit"):
                if any(
                    [
                        symbol.options.get(k)
                        for k in ["type", "platformType", "equipmentTeardownTime"]
                    ]
                ):
                    a = []
                    for k in ["type", "platformType", "equipmentTeardownTime"]:
                        if symbol.options.get(k):
                            a.append(symbol.options.get(k))
                    gStrings["L3"] = "/".join(a)

                gStrings["R1"] = symbol.options.get("reinforcedReduced")
                if symbol.metadata.get("activity"):
                    gStrings["R1"] = symbol.options.get("country")

                if symbol.options.get("additionalInformation") or symbol.options.get(
                    "commonIdentifier"
                ):
                    a = []
                    if symbol.options.get("additionalInformation"):
                        a.append(symbol.options.get("additionalInformation"))
                    if symbol.options.get("commonIdentifier"):
                        a.append(symbol.options.get("commonIdentifier"))
                    gStrings["R3"] = "/".join(a)
            else:
                if any(
                    [
                        symbol.options.get(k)
                        for k in [
                            "type",
                            "platformType",
                            "commonIdentifier",
                            "installationComposition",
                        ]
                    ]
                ):
                    a = []
                    for k in [
                        "type",
                        "platformType",
                        "commonIdentifier",
                        "installationComposition",
                    ]:
                        if symbol.options.get(k):
                            a.append(symbol.options.get(k))
                    gStrings["L3"] = "/".join(a)

                gStrings["R1"] = symbol.options.get("country")

                if symbol.options.get("additionalInformation") or symbol.options.get(
                    "equipmentTeardownTime"
                ):
                    a = []
                    if symbol.options.get("additionalInformation"):
                        a.append(symbol.options.get("additionalInformation"))
                    if symbol.options.get("equipmentTeardownTime"):
                        a.append(symbol.options.get("equipmentTeardownTime"))
                    gStrings["R3"] = "/".join(a)

        # Dismounted individual
        if symbol.metadata.get("dismounted"):
            if symbol.options.get("quantity"):
                drawArray2.append(
                    {
                        "type": "text",
                        "text": symbol.options.get("quantity"),
                        "x": 100,
                        "y": getattr(bbox, "y2", 100) + fontSize,
                        "textanchor": "middle",
                        "fontsize": fontSize,
                        "fontfamily": fontFamily,
                        "fill": fontColor,
                        "stroke": False,
                    }
                )
                gbbox.y2 = getattr(bbox, "y2", 100) + fontSize

            gStrings["L1"] = symbol.options.get("dtg")

            if symbol.options.get("altitudeDepth") or symbol.options.get("location"):
                a = []
                if symbol.options.get("altitudeDepth"):
                    a.append(symbol.options.get("altitudeDepth"))
                if symbol.options.get("location"):
                    a.append(symbol.options.get("location"))
                gStrings["L2"] = "/".join(a)

            if any(
                [
                    symbol.options.get(k)
                    for k in ["type", "platformType", "commonIdentifier"]
                ]
            ):
                a = []
                for k in ["type", "platformType", "commonIdentifier"]:
                    if symbol.options.get(k):
                        a.append(symbol.options.get(k))
                gStrings["L3"] = "/".join(a)

            gStrings["L4"] = symbol.options.get("uniqueDesignation")
            gStrings["L5"] = symbol.options.get("speed")
            gStrings["R1"] = symbol.options.get("country")
            gStrings["R2"] = symbol.options.get("staffComments")

            if symbol.options.get("additionalInformation"):
                a = [
                    symbol.options.get("additionalInformation")
                ]  # JS logic does a=[] then push.
                gStrings["R3"] = "/".join(a)

            gStrings["R4"] = symbol.options.get("higherFormation")

            if any(
                [
                    symbol.options.get(k)
                    for k in [
                        "evaluationRating",
                        "combatEffectiveness",
                        "signatureEquipment",
                        "hostile",
                        "iffSif",
                    ]
                ]
            ):
                a = []
                for k in [
                    "evaluationRating",
                    "combatEffectiveness",
                    "signatureEquipment",
                    "hostile",
                    "iffSif",
                ]:
                    if symbol.options.get(k):
                        a.append(symbol.options.get(k))
                gStrings["R5"] = "/".join(a)

        # Sea numberbased SIDC
        if sidc_numeric and symbol.metadata.get("baseDimension") == "Sea":
            if symbol.options.get("guardedUnit") or symbol.options.get(
                "specialDesignator"
            ):
                a = []
                if symbol.options.get("guardedUnit"):
                    a.append(symbol.options.get("guardedUnit"))
                if symbol.options.get("specialDesignator"):
                    a.append(symbol.options.get("specialDesignator"))
                gStrings["L1"] = "/".join(a)

            gStrings["R1"] = symbol.options.get("uniqueDesignation")
            gStrings["R2"] = symbol.options.get("type")
            gStrings["R3"] = symbol.options.get("iffSif")

            if symbol.options.get("staffComments") or symbol.options.get(
                "additionalInformation"
            ):
                a = []
                if symbol.options.get("staffComments"):
                    a.append(symbol.options.get("staffComments"))
                if symbol.options.get("additionalInformation"):
                    a.append(symbol.options.get("additionalInformation"))
                gStrings["R4"] = "/".join(a)

            if symbol.options.get("location") or symbol.options.get("speed"):
                a = []
                if symbol.options.get("location"):
                    a.append(symbol.options.get("location"))
                if symbol.options.get("speed"):
                    a.append(symbol.options.get("speed"))
                gStrings["R5"] = "/".join(a)

        # Sub numberbased SIDC
        if sidc_numeric and symbol.metadata.get("baseDimension") == "Subsurface":
            gStrings["L1"] = symbol.options.get("specialDesignator")
            gStrings["R1"] = symbol.options.get("uniqueDesignation")
            gStrings["R2"] = symbol.options.get("type")
            gStrings["R3"] = symbol.options.get("altitudeDepth")
            gStrings["R4"] = symbol.options.get("staffComments")
            gStrings["R5"] = symbol.options.get("additionalInformation")

        # Calculates max width needed for layout
        width_l1 = (
            string_width(gStrings["L1"], fontSize, spaceTextIcon)
            if gStrings["L1"]
            else 0
        )
        width_l2 = (
            string_width(gStrings["L2"], fontSize, spaceTextIcon)
            if gStrings["L2"]
            else 0
        )
        width_l3 = (
            string_width(gStrings["L3"], fontSize, spaceTextIcon)
            if gStrings["L3"]
            else 0
        )
        width_l4 = (
            string_width(gStrings["L4"], fontSize, spaceTextIcon)
            if gStrings["L4"]
            else 0
        )
        width_l5 = (
            string_width(gStrings["L5"], fontSize, spaceTextIcon)
            if gStrings["L5"]
            else 0
        )

        special_hq_width = (
            (
                string_width(
                    symbol.options.get("specialHeadquarters"), fontSize, spaceTextIcon
                )
                - bbox.width()
            )
            / 2
            if symbol.options.get("specialHeadquarters")
            else 0
        )
        quantity_width = (
            (
                string_width(symbol.options.get("quantity"), fontSize, spaceTextIcon)
                - bbox.width()
            )
            / 2
            if symbol.options.get("quantity")
            else 0
        )

        margin_left = max(
            special_hq_width,
            quantity_width,
            width_l1,
            width_l2,
            width_l3,
            width_l4,
            width_l5,
        )
        gbbox.x1 = bbox.x1 - margin_left

        width_r1 = (
            string_width(str(gStrings["R1"]) + str(stack), fontSize, spaceTextIcon)
            if gStrings["R1"]
            else 0
        )
        width_r2 = (
            string_width(str(gStrings["R2"]) + str(stack), fontSize, spaceTextIcon)
            if gStrings["R2"]
            else 0
        )
        width_r3 = (
            string_width(str(gStrings["R3"]) + str(stack), fontSize, spaceTextIcon)
            if gStrings["R3"]
            else 0
        )
        # JS uses + flag * 1.5, which is added to string, but JS implicit coercion string + number -> string.
        # But flag is a number (offset). Wait.
        # JS: strWidth(gStrings.R4 + stack + flag * 1.5, fontSize, spaceTextIcon)
        # If gStrings.R4 is string, then + stack (number) -> string concatenation.
        # Then + flag * 1.5 (number) -> string concatenation.
        # So "Text" + "0" + "105" -> "Text0105".
        # Then strWidth calculates width of that string.
        # BUT `stack` and `flag` seem to be offsets in JS logic in other places (line 9).
        # Let's check `strWidth` call again.
        # JS: strWidth(str, fontSize, spaceTextIcon).
        # It calculates width of chars.
        # If I pass a concatenated string, it calculates text width.
        # IF the intention was to add extra width for stack/flag, then concatenating them as text is wrong if they are pixel values.
        # `flag` is 70 or 0 + 30. This is pixels.
        # `stack` is stack*15. This is pixels.
        # Concatenating pixels to string makes it "Text70".
        # If the intention is visual space, then `strWidth` usage is weird if passed concatenated number.
        # However, `strWidth` returns pixel width.
        # IF `stack` and `flag` are visual offsets, they should be added to the RESULT of `strWidth`.
        # JS Lines 556: strWidth(gStrings.R4 + stack + flag * 1.5, fontSize, spaceTextIcon)
        # This looks like a bug in JS or relying on implicit conversion to make the box wider?
        # 70 pixels width ~ 3-4 chars?
        # "70" string width is ~2 chars.
        # Maybe it's intended to be added to width?
        # BUT strWidth takes string.
        # If I look at line 536: gbbox.x2 = bbox.x2 + Math.max(...)
        # So it extends the bbox to the right.
        # If I concatenate "Text" + "70", I get width of "Text70".
        # If I want width of "Text" PLUS 70 pixels, this is wrong.
        # BUT, looking at `textfields.js`, it seems likely it IS a bug or weird hack in JS original.
        # I should probably replicate the JS behavior even if weird, OR fix it if it's obviously pixel addition.
        # Given `stack` and `flag` are derived from options that imply graphical elements (flag icon, stack symbols), they likely consume space.
        # Adding them as text to the string seems wrong.
        # But I must follow "porting" so mostly 1:1.
        # WAIT. In JS `+` operator. string + number = string.
        # So it calculates width of the string representation of the offset.
        # This seems very wrong for layout.
        # UNLESS `strWidth` handles numbers?
        # `strWidth` iterates over `str.length`.
        # If I pass "Text70", it calculates width of chars '7', '0'.
        # That is NOT 70 pixels. '7' is 19, '0' is 19. Total 38.
        # So maybe I should just replicate the concatenation?
        # Visual check: Flag is 70px wide usually in milsymbol.
        # If I add "70" to string, I add ~40px space.
        # Maybe it aligns?
        # Let's check if I can check `milsymbol.js` common bugs.
        # But I'll stick to 1:1 port of logic: String concatenation.
        # NO, wait. `stack` is `this.options.stack * 15`.
        # If stack is undefined, it is 0.
        # I will do string concatenation to be safe as per JS source.

        width_r4 = (
            string_width(
                str(gStrings["R4"]) + str(stack) + str(flag * 1.5),
                fontSize,
                spaceTextIcon,
            )
            if gStrings["R4"]
            else 0
        )
        width_r5 = (
            string_width(
                str(gStrings["R5"]) + str(stack) + str(flag * 1.5),
                fontSize,
                spaceTextIcon,
            )
            if gStrings["R5"]
            else 0
        )

        margin_right = max(
            special_hq_width,
            quantity_width,
            width_r1,
            width_r2,
            width_r3,
            width_r4,
            width_r5,
        )
        gbbox.x2 = bbox.x2 + margin_right

        # Extra space above/below
        if gStrings["L1"] or gStrings["R1"]:
            gbbox.y1 = min(gbbox.y1, 100 - 2.5 * fontSize)
        if gStrings["L2"] or gStrings["R2"]:
            gbbox.y1 = min(gbbox.y1, 100 - 1.5 * fontSize)
        if gStrings["L4"] or gStrings["R4"]:
            gbbox.y2 = max(gbbox.y2, 100 + 1.7 * fontSize)
        if gStrings["L5"] or gStrings["R5"]:
            gbbox.y2 = max(gbbox.y2, 100 + 2.7 * fontSize)

        # Background boxes
        if symbol.style.get("infoBackground"):
            # Implementation of background box logic
            # This is verbose in JS, I'll implement logic similarly
            def update_box(box, text, y_top_factor, y_bottom_factor, is_left):
                if not text:
                    return box
                w = string_width(text, fontSize, spaceTextIcon)
                if is_left:
                    box["x1"] = min(box.get("x1", 1000), bbox.x1 - w)
                    box["x2"] = bbox.x1 - spaceTextIcon / 2
                else:
                    box["x1"] = bbox.x2 + spaceTextIcon / 2
                    box["x2"] = max(box.get("x2", 0), bbox.x2 + w)

                box["y1"] = min(box.get("y1", 1000), 100 - y_top_factor * fontSize)
                box["y2"] = max(
                    box.get("y2", 0),
                    100 + y_bottom_factor * fontSize + spaceTextIcon / 2,
                )
                return box

            leftBox = {"x1": 100, "y1": 1000, "y2": 0}
            leftBox = update_box(
                leftBox, gStrings["L1"], 2.5, -1.5, True
            )  # L1 y range logic differs slightly in JS code, need to match line 588
            # JS L1: y1: 100 - 2.5*FS, y2: 100 - 1.5*FS + pad
            # My helper assumes y_bottom is relative to 100 + ...
            # JS L1: y2 = 100 - 1.5*FS...
            # I should just write it out to be safe.

            # Reset
            leftBox = {"x1": 100, "y1": 1000, "y2": 0}
            if gStrings["L1"]:
                w = string_width(gStrings["L1"], fontSize, spaceTextIcon)
                leftBox["x1"] = min(leftBox["x1"], bbox.x1 - w)
                leftBox["x2"] = bbox.x1 - spaceTextIcon / 2
                leftBox["y1"] = min(leftBox["y1"], 100 - 2.5 * fontSize)
                leftBox["y2"] = max(
                    leftBox["y2"], 100 - 1.5 * fontSize + spaceTextIcon / 2
                )

            if gStrings["L2"]:
                w = string_width(gStrings["L2"], fontSize, spaceTextIcon)
                leftBox["x1"] = min(leftBox["x1"], bbox.x1 - w)
                leftBox["x2"] = bbox.x1 - spaceTextIcon / 2
                leftBox["y1"] = min(leftBox["y1"], 100 - 1.5 * fontSize)
                leftBox["y2"] = max(
                    leftBox["y2"], 100 - 0.5 * fontSize + spaceTextIcon / 2
                )

            if gStrings["L3"]:
                w = string_width(gStrings["L3"], fontSize, spaceTextIcon)
                leftBox["x1"] = min(leftBox["x1"], bbox.x1 - w)
                leftBox["x2"] = bbox.x1 - spaceTextIcon / 2
                leftBox["y1"] = min(leftBox["y1"], 100 - 0.5 * fontSize)
                leftBox["y2"] = max(
                    leftBox["y2"], 100 + 0.5 * fontSize + spaceTextIcon / 2
                )

            if gStrings["L4"]:
                w = string_width(gStrings["L4"], fontSize, spaceTextIcon)
                leftBox["x1"] = min(leftBox["x1"], bbox.x1 - w)
                leftBox["x2"] = bbox.x1 - spaceTextIcon / 2
                leftBox["y1"] = min(leftBox["y1"], 100 + 0.5 * fontSize)
                leftBox["y2"] = max(
                    leftBox["y2"], 100 + 1.5 * fontSize + spaceTextIcon / 2
                )

            if gStrings["L5"]:
                w = string_width(gStrings["L5"], fontSize, spaceTextIcon)
                leftBox["x1"] = min(leftBox["x1"], bbox.x1 - w)
                leftBox["x2"] = bbox.x1 - spaceTextIcon / 2
                leftBox["y1"] = min(leftBox["y1"], 100 + 1.5 * fontSize)
                leftBox["y2"] = max(
                    leftBox["y2"], 100 + 2.5 * fontSize + spaceTextIcon / 2
                )

            if "x2" in leftBox and leftBox["y2"] != 0:  # Check if updated
                gbbox.x1 -= fontSize / 2
                items = [
                    str(leftBox["x1"] - fontSize / 2),
                    str(leftBox["y1"] + fontSize / 2),
                    str(leftBox["x1"]),
                    str(leftBox["y1"]),
                    str(leftBox["x2"]),
                    str(leftBox["y1"]),
                    str(leftBox["x2"]),
                    str(leftBox["y2"]),
                    str(leftBox["x1"] - fontSize / 2),
                    str(leftBox["y2"]),
                ]
                # d: M x,y x,y ... z
                d_str = (
                    "M "
                    + items[0]
                    + ","
                    + items[1]
                    + " "
                    + items[2]
                    + ","
                    + items[3]
                    + " "
                    + items[4]
                    + ","
                    + items[5]
                    + " "
                    + items[6]
                    + ","
                    + items[7]
                    + " "
                    + items[8]
                    + ","
                    + items[9]
                    + " z"
                )
                drawArray2.append(
                    {
                        "type": "path",
                        "d": d_str,
                        "fill": infoBackground,
                        "stroke": infoBackgroundFrame or False,
                    }
                )

            # Note: JS instantiates rightBox = { x2: 100, y1: 1000, y2: 0 } initially but uses x1 later?
            # JS line 580: rightBox = { x2: 100, ... }
            # Line 662: rightBox = { x1: ..., x2: max(...) }
            # So I should initialize similarly or handle per item.
            # I will just track values.
            rb_active = False
            rb_x1 = bbox.x2 + spaceTextIcon / 2
            rb_x2 = (
                bbox.x2 + spaceTextIcon / 2
            )  # JS uses 100 init, but logical logic updates max.
            rb_y1 = 1000
            rb_y2 = 0

            if gStrings["R1"]:
                w = string_width(gStrings["R1"], fontSize, spaceTextIcon)
                rb_x2 = max(rb_x2, bbox.x2 + w)
                rb_y1 = min(rb_y1, 100 - 2.5 * fontSize)
                rb_y2 = max(rb_y2, 100 - 1.5 * fontSize + spaceTextIcon / 2)
                rb_active = True

            if gStrings["R2"]:
                w = string_width(gStrings["R2"], fontSize, spaceTextIcon)
                rb_x2 = max(rb_x2, bbox.x2 + w)
                rb_y1 = min(rb_y1, 100 - 1.5 * fontSize)
                rb_y2 = max(rb_y2, 100 - 0.5 * fontSize + spaceTextIcon / 2)
                rb_active = True

            if gStrings["R3"]:
                w = string_width(gStrings["R3"], fontSize, spaceTextIcon)
                rb_x2 = max(rb_x2, bbox.x2 + w)
                rb_y1 = min(rb_y1, 100 - 0.5 * fontSize)
                rb_y2 = max(rb_y2, 100 + 0.5 * fontSize + spaceTextIcon / 2)
                rb_active = True

            if gStrings["R4"]:
                w = string_width(gStrings["R4"], fontSize, spaceTextIcon)
                rb_x2 = max(rb_x2, bbox.x2 + w)
                rb_y1 = min(rb_y1, 100 + 0.5 * fontSize)
                rb_y2 = max(rb_y2, 100 + 1.5 * fontSize + spaceTextIcon / 2)
                rb_active = True

            if gStrings["R5"]:
                w = string_width(gStrings["R5"], fontSize, spaceTextIcon)
                rb_x2 = max(rb_x2, bbox.x2 + w)
                rb_y1 = min(rb_y1, 100 + 1.5 * fontSize)
                rb_y2 = max(rb_y2, 100 + 2.5 * fontSize + spaceTextIcon / 2)
                rb_active = True

            if rb_active:
                gbbox.x2 += fontSize / 2
                items = [
                    str(rb_x1),
                    str(rb_y1),
                    str(rb_x2 + fontSize / 2),
                    str(rb_y1),
                    str(rb_x2 + fontSize / 2),
                    str(rb_y2 - fontSize / 2),
                    str(rb_x2),
                    str(rb_y2),
                    str(rb_x1),
                    str(rb_y2),
                ]
                d_str = (
                    "M "
                    + items[0]
                    + ","
                    + items[1]
                    + " "
                    + items[2]
                    + ","
                    + items[3]
                    + " "
                    + items[4]
                    + ","
                    + items[5]
                    + " "
                    + items[6]
                    + ","
                    + items[7]
                    + " "
                    + items[8]
                    + ","
                    + items[9]
                    + " z"
                )
                drawArray2.append(
                    {
                        "type": "path",
                        "d": d_str,
                        "fill": infoBackground,
                        "stroke": infoBackgroundFrame or False,
                    }
                )

        # geometries (Drawing text)
        def draw_text(text, x, y, anchor):
            drawArray2.append(
                {
                    "type": "text",
                    "text": text,
                    "x": x,
                    "y": y,
                    "textanchor": anchor,
                    "fontsize": fontSize,
                    "fontfamily": fontFamily,
                    "fill": fontColor,
                    "stroke": False,
                }
            )

        if gStrings["L1"]:
            draw_text(
                gStrings["L1"], bbox.x1 - spaceTextIcon, 100 - 1.5 * fontSize, "end"
            )
        if gStrings["L2"]:
            draw_text(
                gStrings["L2"], bbox.x1 - spaceTextIcon, 100 - 0.5 * fontSize, "end"
            )
        if gStrings["L3"]:
            draw_text(
                gStrings["L3"], bbox.x1 - spaceTextIcon, 100 + 0.5 * fontSize, "end"
            )
        if gStrings["L4"]:
            draw_text(
                gStrings["L4"], bbox.x1 - spaceTextIcon, 100 + 1.5 * fontSize, "end"
            )
        if gStrings["L5"]:
            draw_text(
                gStrings["L5"], bbox.x1 - spaceTextIcon, 100 + 2.5 * fontSize, "end"
            )

        if gStrings["R1"]:
            draw_text(
                gStrings["R1"],
                bbox.x2 + spaceTextIcon + stack,
                100 - 1.5 * fontSize,
                "start",
            )
        if gStrings["R2"]:
            draw_text(
                gStrings["R2"],
                bbox.x2 + spaceTextIcon + stack,
                100 - 0.5 * fontSize,
                "start",
            )
        if gStrings["R3"]:
            draw_text(
                gStrings["R3"],
                bbox.x2 + spaceTextIcon + stack,
                100 + 0.5 * fontSize,
                "start",
            )
        if gStrings["R4"]:
            draw_text(
                gStrings["R4"],
                flag + bbox.x2 + spaceTextIcon + stack,
                100 + 1.5 * fontSize,
                "start",
            )
        if gStrings["R5"]:
            draw_text(
                gStrings["R5"],
                flag + bbox.x2 + spaceTextIcon + stack,
                100 + 2.5 * fontSize,
                "start",
            )

        # outline
        infoOutlineWidth = symbol.style.get("infoOutlineWidth")
        outlineWidth = symbol.style.get("outlineWidth", 0)

        if (
            infoOutlineWidth is not None
            and infoOutlineWidth != False
            and infoOutlineWidth > 0
        ):
            do_outline = True
        elif infoOutlineWidth is False and outlineWidth > 0:
            do_outline = True
        else:
            do_outline = False

        if do_outline:
            width_val = outlineWidth if infoOutlineWidth is False else infoOutlineWidth
            color_val = symbol.style.get("infoOutlineColor") or (
                get_color(symbol.style.get("outlineColor"), affiliation)
                if (
                    isinstance(symbol.style.get("outlineColor"), dict)
                    or hasattr(symbol.style.get("outlineColor"), "Friend")
                )
                else symbol.style.get("outlineColor")
            )

            outlined = ms.outline(
                drawArray2, width_val, symbol.style.get("strokeWidth"), color_val
            )
            if outlined:
                drawArray1.append(outlined)

    return {"pre": drawArray1, "post": drawArray2, "bbox": gbbox}
