def metadata(symbol, ms, metadata, mapping):
    sidc = symbol.options["sidc"]

    # substr(0, 2) -> [0:2]
    version = sidc[0:2]

    # substr(2, 1) -> [2:3]
    standardIdentity1 = sidc[2:3]

    # substr(3, 1) -> [3:4]
    standardIdentity2 = sidc[3:4]

    # substr(4, 2) -> [4:6]
    symbolSet = sidc[4:6]

    # substr(6, 1) -> [6:7]
    status = sidc[6:7]

    # substr(7, 1) -> [7:8]
    headquartersTaskForceDummy = sidc[7:8]

    # substr(8, 2) -> [8:10]
    echelonMobility = sidc[8:10]

    # substr(22, 1) -> [22:23]
    frameshape = sidc[22:23] if len(sidc) > 22 else "0"

    affiliationMapping = {
        "0": "Unknown",
        "1": "Unknown",
        "2": "Friend",
        "3": "Friend",
        "4": "Neutral",
        "5": "Hostile",
        "6": "Hostile",
    }

    if version in ["10", "11", "12"]:
        metadata["edition"] = "D"
    if version in ["13", "14"]:
        metadata["edition"] = "E"

    if version == "13" and standardIdentity2 == "5":
        metadata["suspect"] = True

    dimensionMapping = {
        "00": "Sea",
        "01": "Air",
        "02": "Air",
        "05": "Air",
        "06": "Air",
        "10": "Ground",
        "11": "Ground",
        "12": "Ground",
        "15": "Ground",
        "44": "Ground",  # Wait, 44 missing? In JS source 20, 25 not in map list but checked later
        # JS Map:
        # 10,11,12,15, 20:Ground, 30:Sea, 35:Sub, 36:Sub, 39:Sub, 40:Ground,
        # 50:Air, 51:Air, 52:Ground, 53:Sea, 54:Sub, 60:Ground
        "20": "Ground",
        "30": "Sea",
        "35": "Subsurface",
        "36": "Subsurface",
        "39": "Subsurface",
        "40": "Ground",
        "50": "Air",
        "51": "Air",
        "52": "Ground",
        "53": "Sea",
        "54": "Subsurface",
        "60": "Ground",
    }

    # substr(10, 10) -> [10:20]
    functionid = sidc[10:20]
    metadata["functionid"] = functionid

    # Modifiers
    # substr(20, 1) -> [20:21]
    mod1_char = sidc[20:21] if len(sidc) > 20 else "0"
    # functionid.substr(6, 2) -> functionid[6:8]
    mod1_func = functionid[6:8] if len(functionid) >= 8 else "00"

    metadata["_modifier1"] = mod1_char + mod1_func

    # substr(21, 1) -> [21:22]
    mod2_char = sidc[21:22] if len(sidc) > 21 else "0"
    # functionid.substr(8, 2) -> functionid[8:10]
    mod2_func = functionid[8:10] if len(functionid) >= 10 else "00"

    metadata["_modifier2"] = mod2_char + mod2_func

    # Context
    # mapping.context index based on sidc.substr(2, 1) which is standardIdentity1
    # JS: mapping.context[parseInt(this.options.sidc.substr(2, 1))]
    try:
        ctx_idx = int(standardIdentity1)
        if 0 <= ctx_idx < len(mapping["context"]):
            metadata["context"] = mapping["context"][ctx_idx]
    except ValueError:
        pass

    metadata["affiliation"] = affiliationMapping.get(standardIdentity2, "Unknown")
    metadata["dimension"] = dimensionMapping.get(symbolSet, "")

    if symbolSet in ["10", "11", "25", "27", "40"]:
        metadata["unit"] = True

    if symbolSet in ["05", "06", "50"]:
        metadata["space"] = True

    if symbolSet == "40":
        metadata["activity"] = True

    if symbolSet == "15":
        metadata["landequipment"] = True

    if symbolSet == "20":
        metadata["installation"] = True

    if symbolSet == "25":
        metadata["controlMeasure"] = True

    if symbolSet == "60":
        metadata["cyberspace"] = True

    if symbolSet == "36" and symbol.style["alternateMedal"] is False:
        metadata["fill"] = False

    if symbolSet == "30" and functionid.startswith("150000"):
        metadata["frame"] = False

    # Status checks
    if status == "1":
        metadata["notpresent"] = ms._dashArrays["anticipated"]

    if standardIdentity2 in ["0", "2", "5"]:
        metadata["notpresent"] = ms._dashArrays["pending"]

    # Fused tracks
    if symbolSet == "30" and functionid.startswith("160000"):
        metadata["notpresent"] = ms._dashArrays["pending"]
    if symbolSet == "35" and functionid.startswith("140000"):
        metadata["notpresent"] = ms._dashArrays["pending"]
    if symbolSet == "35" and functionid.startswith("150000"):
        metadata["notpresent"] = ms._dashArrays["pending"]

    # Condition Bar
    if status in ["2", "3", "4", "5"]:
        try:
            st_idx = int(status)
            if 0 <= st_idx < len(mapping["status"]):
                metadata["condition"] = mapping["status"][st_idx]
        except ValueError:
            pass

    metadata["baseDimension"] = metadata["dimension"]
    metadata["baseAffilation"] = metadata["affiliation"]

    if standardIdentity2 == "5" and standardIdentity1 == "1":
        metadata["joker"] = True
    if standardIdentity2 == "6" and standardIdentity1 == "1":
        metadata["faker"] = True

    if metadata["joker"] or metadata["faker"]:
        metadata["affiliation"] = mapping["affiliation"][1]  # Friend

    if symbolSet == "00":
        metadata["dimensionUnknown"] = True

    if (
        symbolSet == "00"
        and standardIdentity1 == "1"
        and metadata["affiliation"] != "Unknown"
    ):
        metadata["affiliation"] = ""

    if symbolSet == "27":
        metadata["dimension"] = "LandDismountedIndividual"
        metadata["dismounted"] = True

    # Same geometry cases
    if symbolSet in ["15", "52"]:
        metadata["dimension"] = mapping["dimension"][2]  # Sea -> index 2

    # Civilian
    # Checking substrings of functionid
    # functionid.substring(0, 2) -> [0:2]
    fi2 = functionid[0:2]
    is_civ = False

    if symbolSet == "01" and fi2 == "12":
        is_civ = True
    elif symbolSet == "05" and fi2 == "12":
        is_civ = True
    elif symbolSet == "11":
        is_civ = True
    elif symbolSet == "12" and fi2 == "12":
        is_civ = True
    elif symbolSet == "15" and fi2 == "16":
        is_civ = True
    elif symbolSet == "30" and fi2 == "14":
        is_civ = True
    elif symbolSet == "35" and fi2 == "12":
        is_civ = True

    if is_civ:
        metadata["civilian"] = True

    # Frame shape overrides 2525E
    if frameshape != "0" and metadata.get("edition") == "E":
        metadata.update(
            {
                "civilian": False,
                "cyberspace": False,
                "installation": False,
                "landequipment": False,
                "activity": False,
                "space": False,
                "unit": False,
            }
        )

        if frameshape == "1":  # Space
            metadata["dimension"] = "Air"
            metadata["space"] = True
        elif frameshape == "2":  # Air
            metadata["dimension"] = "Air"
        elif frameshape == "3":  # Land Unit
            metadata["dimension"] = "Ground"
            metadata["unit"] = True
        elif frameshape == "4":  # Land Equipment/Sea Surface
            metadata["dimension"] = "Sea"
            metadata["landequipment"] = True
        elif frameshape == "5":  # Land Installation
            metadata["dimension"] = "Ground"
            metadata["installation"] = True
        elif frameshape == "6":  # Dismounted Individuals
            metadata["dimension"] = "LandDismountedIndividual"
            metadata["dismounted"] = True
        elif frameshape == "7":  # Sea Subsurface
            metadata["dimension"] = "Subsurface"
        elif frameshape == "8":  # Activity/Event
            metadata["dimension"] = "Ground"
            metadata["activity"] = True
            metadata["unit"] = True
        elif frameshape == "9":  # Cyberspace
            metadata["dimension"] = "Ground"
            # metadata.cyberspace = False; already set
            metadata["unit"] = True

    if frameshape == "A":
        metadata["frame"] = False

    # Headquarters/TF/Dummy
    if headquartersTaskForceDummy in ["1", "3", "5", "7"]:
        metadata["feintDummy"] = True
    if headquartersTaskForceDummy in ["2", "3", "6", "7"]:
        metadata["headquarters"] = True
    if headquartersTaskForceDummy in ["4", "5", "6", "7"]:
        metadata["taskForce"] = True

    # Echelon/Mobility
    # echelonMobility is string, convert to int for comparison
    try:
        em = int(echelonMobility)
        if em <= 30:
            metadata["echelon"] = mapping["echelonMobility"].get(echelonMobility)
        elif em >= 30 and em < 70:
            metadata["mobility"] = mapping["echelonMobility"].get(echelonMobility)
        elif em >= 70 and em < 80:
            metadata["leadership"] = mapping["echelonMobility"].get(echelonMobility)
    except ValueError:
        pass

    return metadata
