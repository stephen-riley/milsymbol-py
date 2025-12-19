def basegeometry(symbol, ms):
    drawArray1 = []
    drawArray2 = []

    # JS: const frameColor = this.colors.frameColor[this.metadata.affiliation];
    # Helper to get color by affiliation
    def get_color(color_obj, affiliation):
        if isinstance(color_obj, dict):
            return color_obj.get(affiliation)
        return getattr(color_obj, affiliation, None)

    affiliation = symbol.metadata.get("affiliation")
    frame_color_obj = symbol.colors.get("frameColor")
    frameColor = get_color(frame_color_obj, affiliation)

    base_geometry = symbol.metadata.get("baseGeometry", {})
    g = base_geometry.get("g", {})

    # JS: if ((!this.metadata.frame && this.style.icon) || typeof this.metadata.baseGeometry.g.type == "undefined")
    # Python: check if 'type' in g
    if (not symbol.metadata.get("frame") and symbol.style.get("icon")) or g.get(
        "type"
    ) is None:
        return {
            "pre": drawArray1,
            "post": drawArray2,
            "bbox": base_geometry.get("bbox"),
        }

    # JS: let geom = { type: this.metadata.baseGeometry.g.type };
    geom = {"type": g.get("type")}

    if geom["type"] == "path":
        geom["d"] = g.get("d")
    elif geom["type"] == "circle":
        geom["cx"] = g.get("cx")
        geom["cy"] = g.get("cy")
        geom["r"] = g.get("r")

    # JS: geom.fill = this.style.fillColor || this.colors.fillColor[this.metadata.affiliation];
    fill_color_obj = symbol.colors.get("fillColor")
    fill_color_aff = get_color(fill_color_obj, affiliation)
    geom["fill"] = (
        symbol.style.get("fillColor")
        if symbol.style.get("fillColor")
        else fill_color_aff
    )

    geom["fillopacity"] = symbol.style.get("fillOpacity")
    geom["stroke"] = frameColor
    if symbol.style.get("fill") and symbol.style.get("frame"):
        geom["stroke"] = "black"
    geom["strokewidth"] = (
        symbol.style.get("strokeWidth") if symbol.style.get("size") >= 10 else 10
    )

    # outline
    if symbol.style.get("frame") and symbol.style.get("outlineWidth", 0) > 0:
        outline_geom = None
        if (
            geom["type"] == "path"
            and symbol.metadata.get("fill")
            and not symbol.style.get("monoColor")
        ):
            outline_geom = {"type": g.get("type")}
            outline_geom["d"] = str(g.get("d")) + " Z"  # Making sure the path is closed
            outline_geom["strokewidth"] = (
                symbol.style.get("strokeWidth")
                if symbol.style.get("size") >= 10
                else 10
            )
        else:
            outline_geom = geom

        outline_color_obj = symbol.style.get("outlineColor")
        outline_color = outline_color_obj
        if isinstance(outline_color_obj, dict) or hasattr(outline_color_obj, "Friend"):
            outline_color = get_color(outline_color_obj, affiliation)

        outlined = ms.outline(
            outline_geom,
            symbol.style.get("outlineWidth"),
            symbol.style.get("strokeWidth"),
            outline_color,
        )
        if outlined:
            drawArray1.append(outlined)

    # JS: Add a dashed outline to the frame if we are using monocolor and the status is not present.
    if (
        symbol.style.get("monoColor") or not symbol.style.get("fill")
    ) and symbol.metadata.get("notpresent"):
        geom["strokedasharray"] = symbol.metadata.get("notpresent")

    drawArray2.append(geom)

    # Dismounted Individual (Commented out in JS)

    # Space Modifiers
    if symbol.metadata.get("space"):
        modifier = {
            "Friend": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "M 100,30 C 90,30 80,35 68.65625,50 l 62.6875,0 C 120,35 110,30 100,30",
            },
            "Hostile": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "M67,50 L100,20 133,50 z",
            },
            "Neutral": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "M45,50 l0,-20 110,0 0,20 z",
            },
            "Unknown": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "M 100 22.5 C 85 22.5 70 31.669211 66 50 L 134 50 C 130 31.669204 115 22.5 100 22.5 z",
            },
        }
        mod = modifier.get(affiliation)
        if mod:
            drawArray2.append(mod)

    # Modifiers for activity.
    if symbol.metadata.get("activity"):
        modifier = {
            "Friend": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "m 160,135 0,15 15,0 0,-15 z m -135,0 15,0 0,15 -15,0 z m 135,-85 0,15 15,0 0,-15 z m -135,0 15,0 0,15 -15,0 z",
            },
            "Hostile": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "M 100 28 L 89.40625 38.59375 L 100 49.21875 L 110.59375 38.59375 L 100 28 z M 38.6875 89.3125 L 28.0625 99.9375 L 38.6875 110.53125 L 49.28125 99.9375 L 38.6875 89.3125 z M 161.40625 89.40625 L 150.78125 100 L 161.40625 110.59375 L 172 100 L 161.40625 89.40625 z M 99.9375 150.71875 L 89.3125 161.3125 L 99.9375 171.9375 L 110.53125 161.3125 L 99.9375 150.71875",
            },
            "Neutral": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "m 140,140 15,0 0,15 -15,0 z m -80,0 0,15 -15,0 0,-15 z m 80,-80 0,-15 15,0 0,15 z m -80,0 -15,0 0,-15 15,0 z",
            },
            "Unknown": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "M 107.96875 31.46875 L 92.03125 31.71875 L 92.03125 46.4375 L 107.71875 46.4375 L 107.96875 31.46875 z M 47.03125 92.5 L 31.09375 92.75 L 31.09375 107.5 L 46.78125 107.5 L 47.03125 92.5 z M 168.4375 92.5 L 152.5 92.75 L 152.5 107.5 L 168.1875 107.5 L 168.4375 92.5 z M 107.96875 153.5625 L 92.03125 153.8125 L 92.03125 168.53125 L 107.71875 168.53125 L 107.96875 153.5625 z",
            },
        }
        mod = modifier.get(affiliation)
        if mod:
            drawArray2.append(mod)

    # Cyberspace Modifiers
    if symbol.metadata.get("cyberspace"):
        modifier = {
            "Friend": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "m 135,150 40,-40 0,40 z",
            },
            "Hostile": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "m 150,78 0,44 22,-22 z",
            },
            "Neutral": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "m 115,155 40,-40 0,40 z",
            },
            "Unknown": {
                "type": "path",
                "stroke": False,
                "fill": frameColor,
                "d": "M 150 65.7 L 150 134 C 176 123 176 77.2 150 65.7 z",
            },
        }
        mod = modifier.get(affiliation)
        if mod:
            drawArray2.append(mod)

    # Add a dashed outline to the frame if the status is not present.
    if (
        symbol.style.get("fill")
        and symbol.style.get("frame")
        and symbol.metadata.get("notpresent")
        and not symbol.metadata.get("unframed")
    ):
        # Clone base geometry
        geom = {"type": g.get("type")}
        if geom["type"] == "path":
            geom["d"] = g.get("d")
        elif geom["type"] == "circle":
            geom["cx"] = g.get("cx")
            geom["cy"] = g.get("cy")
            geom["r"] = g.get("r")

        geom["fill"] = False
        white_colors = symbol.colors.get("white")
        geom["stroke"] = get_color(white_colors, affiliation)
        geom["strokewidth"] = float(symbol.style.get("strokeWidth")) + 1
        geom["strokedasharray"] = symbol.metadata.get("notpresent")
        drawArray2.append(geom)

    return {"pre": drawArray1, "post": drawArray2, "bbox": base_geometry.get("bbox")}
