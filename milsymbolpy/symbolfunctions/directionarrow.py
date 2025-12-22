import math


def directionarrow(symbol, ms):
    drawArray1 = []
    drawArray2 = []

    bbox = symbol.metadata["baseGeometry"].get("bbox")
    if not symbol.metadata.get("baseGeometry", {}).get("g"):
        # in the case we don't have any frame
        bbox = symbol.bbox  # Set bbox to the current symbols bounds

    gbbox = ms.BBox()

    # helper for color
    def get_color(color_obj, affiliation):
        if isinstance(color_obj, dict):
            return color_obj.get(affiliation)
        return getattr(color_obj, affiliation, None)

    icon_colors = symbol.colors.get("iconColor")
    color = get_color(icon_colors, symbol.metadata.get("affiliation")) or get_color(
        icon_colors, "Friend"
    )

    arrow = None

    if symbol.style.get("infoFields"):
        direction = symbol.options.get("direction")
        # Check if direction is defined and not empty string (legacy string compat)
        if direction is not None and direction != "":
            # Convert direction to float if it's a string
            try:
                direction = float(direction)
            except ValueError:
                direction = 0  # Or handle validly

            speed_leader = symbol.options.get("speedLeader", 0)

            if speed_leader == 0:
                # Movement indicator
                arrowLength = 95
                arrow = [
                    {
                        "type": "rotate",
                        "degree": direction,
                        "x": 100,
                        "y": 100,
                        "draw": [
                            {
                                "type": "path",
                                "fill": color,
                                "stroke": color,
                                "strokewidth": symbol.style.get("strokeWidth"),
                                "d": "M100,100 l0,-"
                                + str(arrowLength - 20)
                                + " -5,3 5,-15 5,15 -5,-3",
                            }
                        ],
                    }
                ]

                rad = (direction / 360) * math.pi * 2
                # Note: JS uses direction/360 * 2*PI. Math.cos expects radians.
                # direction is likely in degrees.

                gbbox.y1 = min(100 - math.cos(rad) * arrowLength, 100)
                gbbox.y2 = max(100 - math.cos(rad) * arrowLength, 100)
                gbbox.x1 = min(100 + math.sin(rad) * arrowLength, 100)
                gbbox.x2 = max(100 + math.sin(rad) * arrowLength, 100)

                base_dimension = symbol.metadata.get("baseDimension")

                if base_dimension == "Ground" or base_dimension == "":
                    if not symbol.metadata.get("headquarters"):
                        # For all symbols not headquarters
                        arrow = [
                            {"type": "translate", "x": 0, "y": bbox.y2, "draw": arrow},
                            {
                                "type": "path",
                                "fill": color,
                                "stroke": color,
                                "strokewidth": symbol.style.get("strokeWidth"),
                                "d": "M 100," + str(bbox.y2) + "l0," + str(100),
                            },
                        ]
                    else:
                        # For headquarters
                        hq_length = (
                            symbol.style.get("hqStaffLength") or ms.getHqStaffLength()
                        )
                        # JS: bbox.y2 - (100 - (hqLength))
                        y_trans = bbox.y2 - (100 - hq_length)

                        arrow = [
                            {
                                "type": "translate",
                                "x": bbox.x1 - 100,
                                "y": y_trans,
                                "draw": arrow,
                            }
                        ]
                        gbbox.x1 += bbox.x1 - 100
                        gbbox.x2 += bbox.x1 - 100

                gbbox.y2 += bbox.y2 + float(symbol.style.get("strokeWidth", 0))
                drawArray2.append(arrow)

            else:
                # This is speed leader
                # JS: const length = this.options.speedLeader * (100 / this.style.size);
                size = symbol.style.get("size")
                length = speed_leader * (100 / size)

                rad = (direction * math.pi) / 180
                y = -length * math.cos(rad)
                x = length * math.sin(rad)

                gbbox.x1 = min(100, 100 + x)
                gbbox.x2 = max(100, 100 + x)
                gbbox.y1 = min(100, 100 + y)
                gbbox.y2 = max(100, 100 + y)

                arrow = {
                    "type": "path",
                    "fill": color,
                    "stroke": color,
                    "strokewidth": symbol.style.get("strokeWidth"),
                    "d": "M 100,100  l" + str(x) + "," + str(y),
                }
                drawArray1.append(arrow)

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

                # JS: drawArray1.unshift(ms.outline(arrow...))
                # Python list.insert(0, ...)
                outlined = ms.outline(
                    arrow,
                    symbol.style.get("outlineWidth"),
                    symbol.style.get("strokeWidth"),
                    outline_color,
                )
                if outlined:
                    drawArray1.insert(0, outlined)

    return {"pre": drawArray1, "post": drawArray2, "bbox": gbbox}
