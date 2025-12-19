import math


def modifier(symbol, ms):
    drawArray1 = []
    drawArray2 = []

    # helper for color
    def get_color(color_obj, affiliation):
        if isinstance(color_obj, dict):
            return color_obj.get(affiliation)
        return getattr(color_obj, affiliation, None)

    affiliation = symbol.metadata.get("affiliation")
    frame_color = symbol.style.get("frameColor")
    icon_colors = symbol.colors.get("iconColor")

    color = None
    if frame_color:
        color = get_color(frame_color, affiliation)
    else:
        color = get_color(icon_colors, affiliation)

    base_bbox = symbol.metadata.get("baseGeometry", {}).get("bbox")
    # Clone bbox (assuming ms.BBox can clone from another BBox or dict)
    bbox = ms.BBox(base_bbox)

    gbbox = ms.BBox()
    geom = None

    hqStaffLength = float(symbol.style.get("hqStaffLength") or ms.getHqStaffLength())

    # HEADQUARTERS
    if symbol.metadata.get("headquarters") and hqStaffLength > 0:
        y = 100
        dimension = symbol.metadata.get("dimension")

        # Check alignment conditions
        dim_aff = str(dimension) + str(affiliation)
        if dim_aff in [
            "AirFriend",
            "AirNeutral",
            "GroundFriend",
            "GroundNeutral",
            "SeaNeutral",
            "SubsurfaceNeutral",
        ]:
            y = bbox.y2

        dim_type = str(symbol.metadata.get("dimensionType"))
        aff_type = str(symbol.metadata.get("affiliationType"))
        if dim_type + aff_type == "SubsurfaceFriend":
            y = bbox.y1

        geom = {
            "type": "path",
            "d": "M"
            + str(bbox.x1)
            + ","
            + str(y)
            + " L"
            + str(bbox.x1)
            + ","
            + str(bbox.y2 + hqStaffLength),
        }

        # outline
        if symbol.style.get("outlineWidth", 0) > 0:
            outline_color_obj = symbol.style.get("outlineColor")
            outline_color = outline_color_obj
            if isinstance(outline_color_obj, dict) or hasattr(
                outline_color_obj, "Friend"
            ):
                outline_color = get_color(outline_color_obj, affiliation)

            outlined = ms.outline(
                geom,
                symbol.style.get("outlineWidth"),
                symbol.style.get("strokeWidth"),
                outline_color,
            )
            if outlined:
                drawArray1.append(outlined)

        drawArray2.append(geom)
        gbbox.y2 = bbox.y2 + hqStaffLength

    # TASK FORCE
    if symbol.metadata.get("taskForce"):
        width_map = {
            "Corps/MEF": 110,
            "Army": 145,
            "Army Group/front": 180,
            "Region/Theater": 215,
        }
        width = width_map.get(symbol.metadata.get("echelon"), 90)

        geom = {
            "type": "path",
            "d": "M"
            + str(100 - width / 2)
            + ","
            + str(bbox.y1)
            + " L"
            + str(100 - width / 2)
            + ","
            + str(bbox.y1 - 40)
            + " "
            + str(100 + width / 2)
            + ","
            + str(bbox.y1 - 40)
            + " "
            + str(100 + width / 2)
            + ","
            + str(bbox.y1),
        }

        if symbol.style.get("outlineWidth", 0) > 0:
            outline_color_obj = symbol.style.get("outlineColor")
            outline_color = outline_color_obj
            if isinstance(outline_color_obj, dict) or hasattr(
                outline_color_obj, "Friend"
            ):
                outline_color = get_color(outline_color_obj, affiliation)

            outlined = ms.outline(
                geom,
                symbol.style.get("outlineWidth"),
                symbol.style.get("strokeWidth"),
                outline_color,
            )
            if outlined:
                drawArray1.append(outlined)

        drawArray2.append(geom)
        gbbox.x1 = min(bbox.x1, 100 - width / 2)
        gbbox.x2 = max(bbox.x2, 100 + width / 2)
        gbbox.y1 = bbox.y1 - 40

    # INSTALLATION
    if symbol.metadata.get("installation"):
        gapFiller = 0
        dim_aff = str(symbol.metadata.get("dimension")) + str(affiliation)
        if dim_aff in ["AirHostile", "GroundHostile", "SeaHostile"]:
            gapFiller = 14
        if dim_aff in [
            "AirUnknown",
            "GroundUnknown",
            "SeaUnknown",
            "AirFriend",
            "SeaFriend",
        ]:
            gapFiller = 2

        stroke_width_val = float(symbol.style.get("strokeWidth", 0))
        geom = {
            "type": "path",
            "fill": color,
            "d": "M85,"
            + str(bbox.y1 + gapFiller - stroke_width_val / 2)
            + " 85,"
            + str(bbox.y1 - 10)
            + " 115,"
            + str(bbox.y1 - 10)
            + " 115,"
            + str(bbox.y1 + gapFiller - stroke_width_val / 2)
            + " 100,"
            + str(bbox.y1 - stroke_width_val)
            + " Z",
        }

        if symbol.style.get("outlineWidth", 0) > 0:
            outline_color_obj = symbol.style.get("outlineColor")
            outline_color = outline_color_obj
            if isinstance(outline_color_obj, dict) or hasattr(
                outline_color_obj, "Friend"
            ):
                outline_color = get_color(outline_color_obj, affiliation)

            outlined = ms.outline(
                geom,
                symbol.style.get("outlineWidth"),
                symbol.style.get("strokeWidth"),
                outline_color,
            )
            if outlined:
                drawArray1.append(outlined)

        drawArray2.append(geom)
        # JS: gbbox.merge({ y1: bbox.y1 - 10 });
        gbbox.merge({"y1": bbox.y1 - 10})

    # FEINT DUMMY
    if symbol.metadata.get("feintDummy"):
        topPoint = bbox.y1 - 0 - bbox.width() / 2

        dash_arrays = ms.getDashArrays()
        geom = {
            "type": "path",
            "strokedasharray": dash_arrays.get("feintDummy"),
            "d": "M100,"
            + str(topPoint)
            + " L"
            + str(bbox.x1)
            + ","
            + str(bbox.y1 - 0)
            + " M100,"
            + str(topPoint)
            + " L"
            + str(bbox.x2)
            + ","
            + str(bbox.y1 - 0),
        }

        if symbol.style.get("outlineWidth", 0) > 0:
            outline_color_obj = symbol.style.get("outlineColor")
            outline_color = outline_color_obj
            if isinstance(outline_color_obj, dict) or hasattr(
                outline_color_obj, "Friend"
            ):
                outline_color = get_color(outline_color_obj, affiliation)

            outlined = ms.outline(
                geom,
                symbol.style.get("outlineWidth"),
                symbol.style.get("strokeWidth"),
                outline_color,
            )
            if outlined:
                drawArray1.append(outlined)

        drawArray2.append(geom)
        gbbox.merge({"y1": topPoint})

    # Unit Size (Echelon)
    echelon = symbol.metadata.get("echelon")
    if echelon:
        installationPadding = 15 if symbol.metadata.get("installation") else 0
        echelons = {
            "Team/Crew": {
                "g": [
                    {"type": "circle", "cx": 100, "cy": bbox.y1 - 20, "r": 15},
                    {
                        "type": "path",
                        "d": "M80," + str(bbox.y1 - 10) + "L120," + str(bbox.y1 - 30),
                    },
                ],
                "bbox": {"y1": bbox.y1 - 40 - installationPadding},
            },
            "Squad": {
                "g": [
                    {
                        "type": "circle",
                        "fill": color,
                        "cx": 100,
                        "cy": bbox.y1 - 20,
                        "r": 7.5,
                    }
                ],
                "bbox": {"y1": bbox.y1 - 20 - 7.5 - installationPadding},
            },
            "Section": {
                "g": [
                    {
                        "type": "circle",
                        "fill": color,
                        "cx": 115,
                        "cy": bbox.y1 - 20,
                        "r": 7.5,
                    },
                    {
                        "type": "circle",
                        "fill": color,
                        "cx": 85,
                        "cy": bbox.y1 - 20,
                        "r": 7.5,
                    },
                ],
                "bbox": {"y1": bbox.y1 - 20 - 7.5 - installationPadding},
            },
            "Platoon/detachment": {
                "g": [
                    {
                        "type": "circle",
                        "fill": color,
                        "cx": 100,
                        "cy": bbox.y1 - 20,
                        "r": 7.5,
                    },
                    {
                        "type": "circle",
                        "fill": color,
                        "cx": 70,
                        "cy": bbox.y1 - 20,
                        "r": 7.5,
                    },
                    {
                        "type": "circle",
                        "fill": color,
                        "cx": 130,
                        "cy": bbox.y1 - 20,
                        "r": 7.5,
                    },
                ],
                "bbox": {"y1": bbox.y1 - 20 - 7.5 - installationPadding},
            },
            "Company/battery/troop": {
                "g": [
                    {
                        "type": "path",
                        "d": "M100," + str(bbox.y1 - 10) + "L100," + str(bbox.y1 - 35),
                    }
                ],
                "bbox": {"y1": bbox.y1 - 40 - installationPadding},
            },
            "Battalion/squadron": {
                "g": [
                    {
                        "type": "path",
                        "d": "M90," + str(bbox.y1 - 10) + "L90," + str(bbox.y1 - 35),
                    },
                    {
                        "type": "path",
                        "d": "M110," + str(bbox.y1 - 10) + "L110," + str(bbox.y1 - 35),
                    },
                ],
                "bbox": {"y1": bbox.y1 - 40 - installationPadding},
            },
            "Regiment/group": {
                "g": [
                    {
                        "type": "path",
                        "d": "M100," + str(bbox.y1 - 10) + "L100," + str(bbox.y1 - 35),
                    },
                    {
                        "type": "path",
                        "d": "M120," + str(bbox.y1 - 10) + "L120," + str(bbox.y1 - 35),
                    },
                    {
                        "type": "path",
                        "d": "M80," + str(bbox.y1 - 10) + "L80," + str(bbox.y1 - 35),
                    },
                ],
                "bbox": {"y1": bbox.y1 - 40 - installationPadding},
            },
            "Brigade": {
                "g": [
                    {
                        "type": "path",
                        "d": "M87.5," + str(bbox.y1 - 10) + " l25,-25 m0,25 l-25,-25",
                    }
                ],
                "bbox": {"y1": bbox.y1 - 15 - 25 - installationPadding},
            },
            "Division": {
                "g": [
                    {
                        "type": "path",
                        "d": "M70,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25   M105,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25",
                    }
                ],
                "bbox": {
                    "y1": bbox.y1 - 15 - 25 - installationPadding,
                    "x1": 70,
                    "x2": 130,
                },
            },
            "Corps/MEF": {
                "g": [
                    {
                        "type": "path",
                        "d": "M52.5,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25    M87.5,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25    M122.5,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25",
                    }
                ],
                "bbox": {
                    "y1": bbox.y1 - 15 - 25 - installationPadding,
                    "x1": 52.5,
                    "x2": 147.5,
                },
            },
            "Army": {
                "g": [
                    {
                        "type": "path",
                        "d": "M35,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25   M70,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25   M105,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25    M140,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25",
                    }
                ],
                "bbox": {
                    "y1": bbox.y1 - 15 - 25 - installationPadding,
                    "x1": 35,
                    "x2": 165,
                },
            },
            "Army Group/front": {
                "g": [
                    {
                        "type": "path",
                        "d": "M17.5,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25    M52.5,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25    M87.5,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25    M122.5,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25       M157.5,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25",
                    }
                ],
                "bbox": {
                    "y1": bbox.y1 - 15 - 25 - installationPadding,
                    "x1": 17.5,
                    "x2": 182.5,
                },
            },
            "Region/Theater": {
                "g": [
                    {
                        "type": "path",
                        "d": "M0,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25   M35,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25   M70,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25   M105,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25    M140,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25     M175,"
                        + str(bbox.y1 - 10)
                        + " l25,-25 m0,25 l-25,-25",
                    }
                ],
                "bbox": {
                    "y1": bbox.y1 - 15 - 25 - installationPadding,
                    "x1": 0,
                    "x2": 200,
                },
            },
            "Command": {
                "g": [
                    {
                        "type": "path",
                        "d": "M70,"
                        + str(bbox.y1 - 22.5)
                        + " l25,0 m-12.5,12.5 l0,-25   M105,"
                        + str(bbox.y1 - 22.5)
                        + " l25,0 m-12.5,12.5 l0,-25",
                    }
                ],
                "bbox": {
                    "y1": bbox.y1 - 15 - 25 - installationPadding,
                    "x1": 70,
                    "x2": 130,
                },
            },
        }

        ech_data = echelons.get(echelon)
        if ech_data:
            geom = ech_data.get("g")

            if symbol.style.get("outlineWidth", 0) > 0:
                outline_color_obj = symbol.style.get("outlineColor")
                outline_color = outline_color_obj
                if isinstance(outline_color_obj, dict) or hasattr(
                    outline_color_obj, "Friend"
                ):
                    outline_color = get_color(outline_color_obj, affiliation)

                outlined = ms.outline(
                    {
                        "type": "translate",
                        "x": 0,
                        "y": -installationPadding,
                        "draw": geom,
                    },
                    symbol.style.get("outlineWidth"),
                    symbol.style.get("strokeWidth"),
                    outline_color,
                )
                if outlined:
                    drawArray1.append(outlined)

            drawArray2.append(
                {"type": "translate", "x": 0, "y": -installationPadding, "draw": geom}
            )
            gbbox.merge(ech_data.get("bbox"))

    # Movability indicators
    mobility = symbol.metadata.get("mobility")
    if mobility:
        if not symbol.style.get("frame"):
            bbox.y2 = symbol.bbox.y2

        if affiliation == "Neutral":
            if mobility in ["Towed", "Short towed array", "Long towed Array"]:
                bbox.y2 += 8
            if mobility in ["Over snow (prime mover)", "Sled"]:
                bbox.y2 += 18
            if mobility == "Barge":
                bbox.y2 += 5

        mobilities = {
            "Wheeled limited cross country": {
                "g": [
                    {"type": "path", "d": "M 53,1 l 94,0"},
                    {"type": "circle", "cx": 58, "cy": 8, "r": 8},
                    {"type": "circle", "cx": 142, "cy": 8, "r": 8},
                ],
                "bbox": {"y2": bbox.y2 + 8 * 2},
            },
            "Wheeled cross country": {
                "g": [
                    {"type": "path", "d": "M 53,1 l 94,0"},
                    {"type": "circle", "cx": 58, "cy": 8, "r": 8},
                    {"type": "circle", "cx": 142, "cy": 8, "r": 8},
                    {"type": "circle", "cx": 100, "cy": 8, "r": 8},
                ],
                "bbox": {"y2": bbox.y2 + 8 * 2},
            },
            "Tracked": {
                "g": [
                    {
                        "type": "path",
                        "d": "M 53,1 l 100,0 c15,0 15,15 0,15 l -100,0 c-15,0 -15,-15 0,-15",
                    }
                ],
                "bbox": {"y2": bbox.y2 + 18, "x1": 42, "x2": 168},
            },
            "Wheeled and tracked combination": {
                "g": [
                    {"type": "circle", "cx": 58, "cy": 8, "r": 8},
                    {
                        "type": "path",
                        "d": "M 83,1 l 70,0 c15,0 15,15 0,15 l -70,0 c-15,0 -15,-15 0,-15",
                    },
                ],
                "bbox": {"y2": bbox.y2 + 8 * 2, "x2": 168},
            },
            "Towed": {
                "g": [
                    {"type": "path", "d": "M 63,1 l 74,0"},
                    {"type": "circle", "cx": 58, "cy": 3, "r": 8},
                    {"type": "circle", "cx": 142, "cy": 3, "r": 8},
                ],
                "bbox": {"y2": bbox.y2 + 10},
            },
            "Rail": {
                "g": [
                    {"type": "path", "d": "M 53,1 l 96,0"},
                    {"type": "circle", "cx": 58, "cy": 8, "r": 8},
                    {"type": "circle", "cx": 73, "cy": 8, "r": 8},
                    {"type": "circle", "cx": 127, "cy": 8, "r": 8},
                    {"type": "circle", "cx": 142, "cy": 8, "r": 8},
                ],
                "bbox": {"y2": bbox.y2 + 8 * 2},
            },
            "Over snow (prime mover)": {
                "g": [{"type": "path", "d": "M 50,-9 l10,10 90,0"}],
                "bbox": {"y2": bbox.y2 + 9},
            },
            "Sled": {
                "g": [
                    {
                        "type": "path",
                        "d": "M 145,-12  c15,0 15,15 0,15 l -90,0 c-15,0 -15,-15 0,-15",
                    }
                ],
                "bbox": {"y2": bbox.y2 + 15, "x1": 42, "x2": 168},
            },
            "Pack animals": {
                "g": [{"type": "path", "d": "M 80,20 l 10,-20 10,20 10,-20 10,20"}],
                "bbox": {"y2": bbox.y2 + 20},
            },
            "Barge": {
                "g": [{"type": "path", "d": "M 50,1 l 100,0 c0,10 -100,10 -100,0"}],
                "bbox": {"y2": bbox.y2 + 10},
            },
            "Amphibious": {
                "g": [
                    {
                        "type": "path",
                        "d": "M 65,10 c 0,-10 10,-10 10,0 0,10 10,10 10,0	0,-10 10,-10 10,0 0,10 10,10 10,0	0,-10 10,-10 10,0 0,10 10,10 10,0	0,-10 10,-10 10,0",
                    }
                ],
                "bbox": {"y2": bbox.y2 + 20},
            },
            "Short towed array": {
                "g": [
                    {
                        "type": "path",
                        "fill": color,
                        "d": "M 50,5 l 100,0 M50,0 l10,0 0,10 -10,0 z M150,0 l-10,0 0,10 10,0 z M100,0 l5,5 -5,5 -5,-5 z",
                    }
                ],
                "bbox": {"y2": bbox.y2 + 10},
            },
            "Long towed Array": {
                "g": [
                    {
                        "type": "path",
                        "fill": color,
                        "d": "M 50,5 l 100,0 M50,0 l10,0 0,10 -10,0 z M150,0 l-10,0 0,10 10,0 z M105,0 l-10,0 0,10 10,0 z M75,0 l5,5 -5,5 -5,-5 z  M125,0 l5,5 -5,5 -5,-5 z",
                    }
                ],
                "bbox": {"y2": bbox.y2 + 10},
            },
        }

        mob_data = mobilities.get(mobility)
        if mob_data:
            geom = mob_data.get("g")

            if symbol.style.get("outlineWidth", 0) > 0:
                outline_color_obj = symbol.style.get("outlineColor")
                outline_color = outline_color_obj
                if isinstance(outline_color_obj, dict) or hasattr(
                    outline_color_obj, "Friend"
                ):
                    outline_color = get_color(outline_color_obj, affiliation)

                outlined = ms.outline(
                    {"type": "translate", "x": 0, "y": bbox.y2, "draw": geom},
                    symbol.style.get("outlineWidth"),
                    symbol.style.get("strokeWidth"),
                    outline_color,
                )
                if outlined:
                    drawArray1.append(outlined)

            drawArray2.append({"type": "translate", "x": 0, "y": bbox.y2, "draw": geom})
            gbbox.merge(mob_data.get("bbox"))

    # Dismounted Leadership
    if symbol.metadata.get("leadership"):
        leadership_map = {"Friend": {"type": "path", "d": "m 45,60 55,-25 55,25"}}
        leadership = leadership_map.get(affiliation)
        if leadership:
            drawArray1.append(
                leadership
            )  # JS pushes to drawArray1 (pre) for some reason? No, it pushes to 1 (outline layer?)
            # JS: drawArray1.push(leadership);
            # Usually modifiers are in drawArray2. But here it is 1. Maybe because it's distinct?
            # Or maybe to be behind?

            # The JS code pushes to drawArray1.

            gbbox.merge({"y1": bbox.y1 - 20})

    # Assign fill, stroke and stroke-width
    for item in drawArray1:
        if "fill" not in item:
            item["fill"] = False
        if "stroke" not in item:
            item["stroke"] = color
        if "strokewidth" not in item:
            item["strokewidth"] = symbol.style.get("strokeWidth")

    for item in drawArray2:
        if "fill" not in item:
            item["fill"] = False
        if "stroke" not in item:
            item["stroke"] = color
        if "strokewidth" not in item:
            item["strokewidth"] = symbol.style.get("strokeWidth")

    return {"pre": drawArray1, "post": drawArray2, "bbox": gbbox}
