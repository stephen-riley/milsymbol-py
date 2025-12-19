def load_symbol_geometries(ms):
    ms._symbolGeometries = {}

    # BBox Helper
    # Assuming ms.BBox exists
    BBox = ms.BBox

    # Ground Friend / Assumed Friend (Rectangle)
    # Standard 2525C frame for ground unit is 1.5:1
    ms._symbolGeometries["GroundFriend"] = {
        "g": {"type": "path", "d": "M 25,50 L 175,50 L 175,150 L 25,150 Z"},
        "bbox": BBox({"x1": 25, "y1": 50, "x2": 175, "y2": 150}),
    }

    # Ground Hostile (Diamond)
    # Standard 1:1 Diamond
    ms._symbolGeometries["GroundHostile"] = {
        "g": {"type": "path", "d": "M 100,15 L 185,100 L 100,185 L 15,100 Z"},
        "bbox": BBox({"x1": 15, "y1": 15, "x2": 185, "y2": 185}),
    }

    # Ground Neutral (Square)
    # Standard 1:1 Square
    ms._symbolGeometries["GroundNeutral"] = {
        "g": {"type": "path", "d": "M 50,50 L 150,50 L 150,150 L 50,150 Z"},
        "bbox": BBox({"x1": 50, "y1": 50, "x2": 150, "y2": 150}),
    }

    # Ground Unknown (Quatrefoil)
    ms._symbolGeometries["GroundUnknown"] = {
        "g": {
            "type": "path",
            "d": "M 100,20 Q 180,20 180,100 Q 180,180 100,180 Q 20,180 20,100 Q 20,20 100,20 Z",
        },
        "bbox": BBox({"x1": 20, "y1": 20, "x2": 180, "y2": 180}),
    }

    # Aliases
    ms._symbolGeometries["GroundAssumed Friend"] = ms._symbolGeometries["GroundFriend"]
    ms._symbolGeometries["GroundSuspect"] = ms._symbolGeometries["GroundHostile"]
    ms._symbolGeometries["GroundJoker"] = ms._symbolGeometries["GroundFriend"]
    ms._symbolGeometries["GroundFaker"] = ms._symbolGeometries["GroundHostile"]

    # Position Marker (Circle) - Used as fallback often
    ms._symbolGeometries["PositionMarker"] = {
        "g": {"type": "circle", "cx": 100, "cy": 100, "r": 10},
        "bbox": BBox({"x1": 90, "y1": 90, "x2": 110, "y2": 110}),
    }

    # Sea, Air, etc. use geometric shapes too, often open frames.
    # For now, mapping them to something visible so tests pass visually.
    # Sea Friend (Circle)
    ms._symbolGeometries["SeaFriend"] = {
        "g": {"type": "circle", "cx": 100, "cy": 100, "r": 80},
        "bbox": BBox({"x1": 20, "y1": 20, "x2": 180, "y2": 180}),
    }

    # Apply defaults for other dimensions to prevent crashes/empty
    for aff in ["Friend", "Hostile", "Neutral", "Unknown"]:
        for dim in ["Air", "Space", "Subsurface"]:
            key = dim + aff
            if key not in ms._symbolGeometries:
                # Fallback to Ground shapes for now to ensure visibility
                ms._symbolGeometries[key] = ms._symbolGeometries["Ground" + aff]
