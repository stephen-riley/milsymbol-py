def engagmentbar(symbol, ms):
    drawArray1 = []
    drawArray2 = []

    bbox = symbol.bbox
    x1 = bbox.x1
    x2 = bbox.x2
    y1 = bbox.y1
    y2 = bbox.y2

    engagement_bar = symbol.options.get("engagementBar")

    if engagement_bar and engagement_bar != "":
        y1 -= 6
        fontFamily = symbol.style.get("fontfamily")

        # Helper for color
        def get_color(color_obj, affiliation):
            if isinstance(color_obj, dict):
                return color_obj.get(affiliation)
            return getattr(color_obj, affiliation, None)

        icon_colors = symbol.colors.get("iconColor")
        fontColor = get_color(
            icon_colors, symbol.metadata.get("affiliation")
        ) or get_color(icon_colors, "Friend")

        drawArray2.append(
            {
                "type": "text",
                "text": engagement_bar,
                "x": 100,
                "y": getattr(bbox, "y1", 100)
                - 11,  # bbox.y1 might have changed? Loop uses local y1 but text uses current bbox.y1 - 11. Wait.
                # in JS: y: bbox.y1 - 11. JS `bbox` is `this.bbox` (initial).
                "textanchor": "middle",
                "fontsize": 22,
                "fontfamily": fontFamily,
                "fontweight": "bold",
                "fill": fontColor,
                "stroke": False,
            }
        )

        color = False
        if symbol.metadata.get("fill") and symbol.style.get("monoColor") == "":
            colors = {
                "TARGET": "rgb(255, 0, 0)",
                "NON-TARGET": "rgb(255, 255, 255)",
                "EXPIRED": "rgb(255, 120, 0)",
            }
            engagement_type = symbol.options.get("engagementType", "").upper()
            fill_colors = symbol.colors.get("fillColor")

            color = colors.get(engagement_type) or get_color(
                fill_colors, symbol.metadata.get("affiliation")
            )

        # Bar width
        # JS: const width = Math.max(bbox.width(), this.options.engagementBar.length * 16);
        current_width = bbox.width()
        text_width = len(engagement_bar) * 16
        width = max(current_width, text_width)

        x1 = min(x1, 100 - width / 2)
        x2 = max(x2, 100 + width / 2)

        # Add the bar to the geometry
        # JS: drawArray2.unshift(...)
        frame_colors = symbol.colors.get("frameColor")
        stroke_color = get_color(frame_colors, symbol.metadata.get("affiliation"))

        drawArray2.insert(
            0,
            {
                "type": "path",
                "strokewidth": symbol.style.get("strokeWidth"),
                "fill": color,
                "stroke": stroke_color,
                "d": "M"
                + str(100 - width / 2)
                + ","
                + str(y1)
                + " l"
                + str(width)
                + ",0 0,-25 -"
                + str(width)
                + ",0 z",
            },
        )

        # Add the height of the condition bar to the geometry bounds
        y1 -= 25

        # outline
        if symbol.style.get("outlineWidth", 0) > 0:
            outline = None
            if symbol.metadata.get("fill") and symbol.style.get("monoColor") == "":
                outline = drawArray2[0]
            else:
                outline = drawArray2

            outline_color_obj = symbol.style.get("outlineColor")
            outline_color_val = outline_color_obj
            if isinstance(outline_color_obj, dict) or hasattr(
                outline_color_obj, "Friend"
            ):
                outline_color_val = get_color(
                    outline_color_obj, symbol.metadata.get("affiliation")
                )

            outlined = ms.outline(
                outline,
                symbol.style.get("outlineWidth"),
                symbol.style.get("strokeWidth"),
                outline_color_val,
            )
            if outlined:
                drawArray1.append(outlined)

    return {
        "pre": drawArray1,
        "post": drawArray2,
        "bbox": {"x1": x1, "x2": x2, "y1": y1, "y2": y2},
    }
