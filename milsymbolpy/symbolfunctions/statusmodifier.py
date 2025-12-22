def statusmodifier(symbol, ms):
    drawArray1 = []
    drawArray2 = []

    bbox = symbol.metadata["baseGeometry"][
        "bbox"
    ]  # Assuming this is a BBox object or dict with similar interface
    # In Python if it's a dict, we might need a wrapper or access carefully.
    # symbol.metadata["baseGeometry"] comes from symbolgeometries.py or dynamic.
    # It should be a BBox object if coming from ms.py structure.
    # But let's be safe.

    def get_attr(obj, name, default):
        # 1. Try getattr
        res = getattr(obj, name, None)
        if res is not None:
            return res
        # 2. If no attribute, check if dict and use get
        if isinstance(obj, dict):
            return obj.get(name, default)
        # 3. Return default
        return default

    y1 = get_attr(bbox, "y1", 100)
    y2 = get_attr(bbox, "y2", 100)
    x1 = get_attr(bbox, "x1", 100)
    # width() method?
    width = bbox.width() if hasattr(bbox, "width") else (get_attr(bbox, "x2", 100) - x1)

    # Helper for color
    def get_color(color_obj, affiliation):
        if isinstance(color_obj, dict):
            return color_obj.get(affiliation)
        return getattr(color_obj, affiliation, None)

    condition = symbol.metadata.get("condition")
    if condition:
        if (
            symbol.metadata.get("fill")
            and symbol.style.get("monoColor") == ""
            and not symbol.style.get("simpleStatusModifier")
        ):
            colors = {
                "FullyCapable": "rgb(0,255,0)",
                "Damaged": "rgb(255,255,0)",
                "Destroyed": "rgb(255,0,0)",
                "FullToCapacity": "rgb(0, 180, 240)",
            }

            # If it is unframed and equipment use the bottom of the icon
            if not symbol.metadata.get("frame") and symbol.metadata.get("iconBottom"):
                y2 = symbol.metadata.get("iconBottom")

            # If we have headquartersElement add space for the text
            if symbol.options.get("headquartersElement"):
                y2 += 35

            # If we have a mobility indicator we need to make space for it.
            if symbol.metadata.get("mobility"):
                y2 += 25
            else:
                y2 += 5

            fill_color = colors.get(condition)
            frame_colors = symbol.colors.get("frameColor")
            stroke_color = get_color(frame_colors, symbol.metadata.get("affiliation"))

            drawArray2.append(
                {
                    "type": "path",
                    "strokewidth": symbol.style.get("strokeWidth"),
                    "fill": fill_color,
                    "stroke": stroke_color,
                    "d": "M"
                    + str(x1)
                    + ","
                    + str(y2)
                    + " l"
                    + str(width)
                    + ",0 0,25 -"
                    + str(width)
                    + ",0 z",
                }
            )

            y2 += 25

            # outline
            if symbol.style.get("outlineWidth", 0) > 0:
                outline_color_obj = symbol.style.get("outlineColor")
                outline_color = outline_color_obj
                if isinstance(outline_color_obj, dict) or hasattr(
                    outline_color_obj, "Friend"
                ):
                    outline_color = get_color(
                        outline_color_obj, symbol.metadata.get("affiliation")
                    )

                outlined = ms.outline(
                    drawArray2,
                    symbol.style.get("outlineWidth"),
                    symbol.style.get("strokeWidth"),
                    outline_color,
                )
                if outlined:
                    drawArray1.append(outlined)

        else:
            # Simple status modifier
            frame_colors = symbol.colors.get("frameColor")
            stroke_color = get_color(frame_colors, symbol.metadata.get("affiliation"))

            if condition == "Damaged" or condition == "Destroyed":
                drawArray2.append(
                    {
                        "type": "path",
                        "d": "M150,20 L50,180",
                        "strokewidth": float(symbol.style.get("strokeWidth")) * 2,
                        "stroke": stroke_color,
                    }
                )
                y1 = 20
                y2 = 180

            if condition == "Destroyed":
                drawArray2.append(
                    {
                        "type": "path",
                        "d": "M50,20 L150,180",
                        "strokewidth": float(symbol.style.get("strokeWidth")) * 2,
                        "stroke": stroke_color,
                    }
                )

            # outline
            if symbol.style.get("outlineWidth", 0) > 0:
                outline_color_obj = symbol.style.get("outlineColor")
                outline_color = outline_color_obj
                if isinstance(outline_color_obj, dict) or hasattr(
                    outline_color_obj, "Friend"
                ):
                    outline_color = get_color(
                        outline_color_obj, symbol.metadata.get("affiliation")
                    )

                outlined = ms.outline(
                    drawArray2,
                    symbol.style.get("outlineWidth"),
                    symbol.style.get("strokeWidth"),
                    outline_color,
                )
                if outlined:
                    drawArray1.append(outlined)

    return {"pre": drawArray1, "post": drawArray2, "bbox": {"y1": y1, "y2": y2}}
