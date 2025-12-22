def affliationdimension(symbol, ms):
    drawArray1 = []
    drawArray2 = []

    # JS: let bbox = this.metadata.baseGeometry.bbox;
    base_geometry = symbol.metadata.get("baseGeometry", {})
    bbox = base_geometry.get("bbox")

    # JS: const frameColor = this.colors.frameColor[this.metadata.affiliation];
    # symbol.colors["frameColor"] is a ColorMode object or dict.
    # In ms.py getColorMode returns a ColorMode object which has attributes like .Friend etc.
    # But in symbol.py it seems it might be a dict or object.
    # Let's check symbol.py getColors().
    # It returns a dict where values are ColorMode objects (which have attributes) OR dicts.
    # ColorMode object access: .Friend, .Hostile etc.
    # But JS uses [this.metadata.affiliation].
    # Python ColorMode might need getattr or matching key access.
    # If ColorMode is a class, we use getattr.

    affiliation = symbol.metadata.get("affiliation")
    frame_color_obj = symbol.colors.get("frameColor")

    frameColor = None
    if frame_color_obj:
        if isinstance(frame_color_obj, dict):
            frameColor = frame_color_obj.get(affiliation)
        else:
            # Assume ColorMode object with attributes
            frameColor = getattr(frame_color_obj, affiliation, None)

    # JS: if (this.metadata.dimensionUnknown && frameColor)
    if symbol.metadata.get("dimensionUnknown") and frameColor:
        drawArray2.append(
            {
                "type": "text",
                "text": "?",
                "x": 100,
                "y": 127,
                "fill": frameColor,
                "fontfamily": symbol.style.get("fontfamily"),
                "fontsize": 80,
                "fontweight": "bold",
                "textanchor": "middle",
            }
        )

    # JS: if (this.metadata.baseGeometry.g && frameColor)
    if base_geometry.get("g") and frameColor:
        spacing = 10
        if affiliation == "Unknown" or (
            affiliation == "Hostile"
            and symbol.metadata.get("dimension") != "Subsurface"
        ):
            spacing = -10

        context = symbol.metadata.get("context")
        joker = symbol.metadata.get("joker")
        faker = symbol.metadata.get("faker")

        if context == "Exercise":
            if not (joker or faker):
                drawArray2.append(
                    {
                        "type": "text",
                        "text": "X",
                        "x": bbox.x2 + spacing,
                        "y": 50,
                        "fill": frameColor,
                        "fontfamily": symbol.style.get("fontfamily"),
                        "fontsize": 35,
                        "fontweight": "bold",
                        "textanchor": "start",
                        "alignmentBaseline": "middle",
                    }
                )

            if joker:
                drawArray2.append(
                    {
                        "type": "text",
                        "text": "J",
                        "x": bbox.x2 + spacing,
                        "y": 40,
                        "fill": frameColor,
                        "fontfamily": symbol.style.get("fontfamily"),
                        "fontsize": 35,
                        "fontweight": "bold",
                        "textanchor": "start",
                        "alignmentBaseline": "middle",
                    }
                )

            if faker:
                drawArray2.append(
                    {
                        "type": "text",
                        "text": "K",
                        "x": bbox.x2 + spacing,
                        "y": 40,
                        "fill": frameColor,
                        "fontfamily": symbol.style.get("fontfamily"),
                        "fontsize": 35,
                        "fontweight": "bold",
                        "textanchor": "start",
                        "alignmentBaseline": "middle",
                    }
                )

            # JS: bbox = { x2: bbox.x2 + spacing + 22, y1: 40 - 25 };
            # We create a new BBox with updated values.
            # Note: ms.BBox will default unspecified values to 100.
            # This is fine for merging as long as we don't shrink the box.

            bbox_vals = {"x2": bbox.x2 + spacing + 22, "y1": 40 - 25}
            bbox = ms.BBox(bbox_vals)

        if context == "Simulation":
            drawArray2.append(
                {
                    "type": "text",
                    "text": "S",
                    "x": bbox.x2 + spacing,
                    "y": 40,
                    "fill": frameColor,
                    "fontfamily": symbol.style.get("fontfamily"),
                    "fontsize": 35,
                    "fontweight": "bold",
                    "textanchor": "start",
                    "alignmentBaseline": "middle",
                }
            )
            # JS: bbox = new ms.BBox({ x2: bbox.x2 + spacing + 22, y1: 40 - 25 });
            bbox_vals = {"x2": bbox.x2 + spacing + 22, "y1": 40 - 25}
            bbox = ms.BBox(bbox_vals)

    # outline
    if symbol.style.get("outlineWidth", 0) > 0:
        outline_color = symbol.style.get("outlineColor")
        oc = outline_color
        if isinstance(outline_color, dict) or hasattr(
            outline_color, "Friend"
        ):  # ColorMode check
            # Access by affiliation
            if isinstance(outline_color, dict):
                oc = outline_color.get(affiliation)
            else:
                oc = getattr(outline_color, affiliation, None)

        # ms.outline(geom, width, stroke_width, color)
        # JS: ms.outline(drawArray2, ...)

        outlined_geom = ms.outline(
            drawArray2,
            symbol.style.get("outlineWidth"),
            symbol.style.get("strokeWidth"),
            oc,
        )
        if outlined_geom:
            drawArray1.append(outlined_geom)

    return {"pre": drawArray1, "post": drawArray2, "bbox": bbox}
