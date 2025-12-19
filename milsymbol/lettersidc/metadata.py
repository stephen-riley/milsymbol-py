def metadata(symbol, ms, metadata_obj, mapping):
    sidc = symbol.options.get("sidc", "").upper()
    symbol.options["sidc"] = sidc  # Update in place just in case

    codingscheme = sidc[0] if len(sidc) > 0 else "-"
    affiliation = sidc[1] if len(sidc) > 1 else "-"
    battledimension = sidc[2] if len(sidc) > 2 else "-"
    status = sidc[3] if len(sidc) > 3 else "-"

    functionid = sidc[4:10] if len(sidc) >= 10 else "------"
    metadata_obj["functionid"] = functionid

    symbolmodifier11 = sidc[10] if len(sidc) > 10 else "-"
    symbolmodifier12 = sidc[11] if len(sidc) > 11 else "-"

    # Mapping affiliation
    if affiliation in ["H", "S", "J", "K"]:
        metadata_obj["affiliation"] = mapping["affiliation"][0]
    if affiliation in ["F", "A", "D", "M"]:
        metadata_obj["affiliation"] = mapping["affiliation"][1]
    if affiliation in ["N", "L"]:
        metadata_obj["affiliation"] = mapping["affiliation"][2]
    if affiliation in ["P", "U", "G", "W", "O"]:
        metadata_obj["affiliation"] = mapping["affiliation"][3]

    # Mapping dimension
    if battledimension in ["P", "A"]:
        metadata_obj["dimension"] = mapping["dimension"][0]
    if battledimension in ["G", "Z", "F", "X"]:
        metadata_obj["dimension"] = mapping["dimension"][1]
    if battledimension in ["S"]:
        metadata_obj["dimension"] = mapping["dimension"][2]
    if battledimension in ["U"]:
        metadata_obj["dimension"] = mapping["dimension"][3]

    # dimension is in Space
    if battledimension == "P" and codingscheme != "O":
        metadata_obj["space"] = True

    # codingscheme that are Activities
    if codingscheme == "O" and battledimension in ["V", "O", "R"]:
        metadata_obj["activity"] = True

    # SymbolSets that are control-measure
    if codingscheme == "G":
        metadata_obj["controlMeasure"] = True

    # symbolmodifier11 that are Installations
    if symbolmodifier11 == "H":
        metadata_obj["installation"] = True

    # Planned/Anticipated/Suspect symbols should have a dashed outline
    if symbol.style.get("frame") and status == "A":
        metadata_obj["notpresent"] = ms._dashArrays["anticipated"]
    if symbol.style.get("frame") and affiliation in ["P", "A", "S", "G", "M"]:
        metadata_obj["notpresent"] = ms._dashArrays["pending"]

    # Should it have a Condition Bar
    if status == "C":
        metadata_obj["condition"] = mapping["status"][2]
    if status == "D":
        metadata_obj["condition"] = mapping["status"][3]
    if status == "X":
        metadata_obj["condition"] = mapping["status"][4]
    if status == "F":
        metadata_obj["condition"] = mapping["status"][5]

    # Is it part of Exercise Symbols
    if affiliation in ["G", "W", "D", "L", "M", "J", "K"]:
        metadata_obj["context"] = mapping["context"][1]

    # Framing of SO tactical symbols differs slightly...
    if codingscheme == "O":
        metadata_obj["dimension"] = mapping["dimension"][1]
    # Framing of EMS tactical symbols differs slightly...
    if codingscheme == "E":
        metadata_obj["dimension"] = mapping["dimension"][1]

    # First save the dimensionType and affiliationType before we modifies it...
    metadata_obj["baseDimension"] = metadata_obj.get("dimension")
    metadata_obj["baseAffilation"] = metadata_obj.get("affiliation")

    # Joker and faker should have the shape of friendly
    if affiliation == "J":
        metadata_obj["joker"] = True
    if affiliation == "K":
        metadata_obj["faker"] = True
    if metadata_obj.get("joker") or metadata_obj.get("faker"):
        metadata_obj["affiliation"] = mapping["affiliation"][1]

    # Ground Equipment should have the same geometry as sea Friend...
    if codingscheme == "S" and battledimension == "G" and functionid.startswith("E"):
        metadata_obj["dimension"] = mapping["dimension"][2]

    # Signal INTELLIGENCE Ground should have the same geometry as sea Friend...
    if codingscheme == "I" and battledimension == "G":
        metadata_obj["dimension"] = mapping["dimension"][2]

    # Some EMS symbosls should have the same geometry as sea Friend...
    if codingscheme == "E":
        if battledimension == "O" and functionid in [
            "AB----",
            "AE----",
            "AF----",
            "BB----",
            "CB----",
            "CC----",
            "DB----",
            "DDB---",
            "DEB---",
            "DFB---",
            "DGB---",
            "DHB---",
            "DIB---",
            "DJB---",
            "DLB---",
            "DMB---",
            "DOB---",
            "EA----",
            "EB----",
            "EC----",
            "ED----",
            "EE----",
        ]:
            metadata_obj["dimension"] = mapping["dimension"][2]
        elif battledimension == "F" and functionid in ["BA----", "MA----", "MC----"]:
            metadata_obj["dimension"] = mapping["dimension"][2]

    # Setting up Headquarters/task force/dummy
    if symbolmodifier11 in ["F", "G", "C", "D"] or (
        symbolmodifier11 == "H" and symbolmodifier12 == "B"
    ):
        metadata_obj["feintDummy"] = True

    if symbolmodifier11 in ["A", "B", "C", "D"]:
        metadata_obj["headquarters"] = True
    if battledimension == "G" and functionid == "UH----":
        metadata_obj["headquarters"] = True

    if symbolmodifier11 in ["E", "B", "G", "D"]:
        metadata_obj["taskForce"] = True

    # Setting up Echelon/Mobility/Towed Array Amplifier
    # mapping.echelonMobility is a dict or list? In ms.js it is likely a dict or array.
    # Usually index based, so list or dict with int keys.
    # In JS it's accessed via [11], etc.

    ech_mob = mapping.get("echelonMobility", {})

    if symbolmodifier12 == "A":
        metadata_obj["echelon"] = ech_mob.get("11")  # Team/Crew
    if symbolmodifier12 == "B" and symbolmodifier11 != "H":
        metadata_obj["echelon"] = ech_mob.get("12")  # Squad
    if symbolmodifier12 == "C":
        metadata_obj["echelon"] = ech_mob.get("13")  # Section
    if symbolmodifier12 == "D":
        metadata_obj["echelon"] = ech_mob.get("14")  # Platoon/detachment
    if symbolmodifier12 == "E":
        metadata_obj["echelon"] = ech_mob.get("15")  # Company/battery/troop
    if symbolmodifier12 == "F":
        metadata_obj["echelon"] = ech_mob.get("16")  # Battalion/squadron
    if symbolmodifier12 == "G":
        metadata_obj["echelon"] = ech_mob.get("17")  # Regiment/group
    if symbolmodifier12 == "H":
        metadata_obj["echelon"] = ech_mob.get("18")  # Brigade
    if symbolmodifier12 == "I":
        metadata_obj["echelon"] = ech_mob.get("21")  # Division
    if symbolmodifier12 == "J":
        metadata_obj["echelon"] = ech_mob.get("22")  # Corps/MEF
    if symbolmodifier12 == "K":
        metadata_obj["echelon"] = ech_mob.get("23")  # Army
    if symbolmodifier12 == "L" and symbolmodifier11 != "N":
        metadata_obj["echelon"] = ech_mob.get("24")  # Army Group/front
    if symbolmodifier12 == "M":
        metadata_obj["echelon"] = ech_mob.get("25")  # Region/Theater
    if symbolmodifier12 == "N":
        metadata_obj["echelon"] = ech_mob.get("26")  # Command

    if symbolmodifier11 == "M":
        mob_map = {
            "O": 31,
            "P": 32,
            "Q": 33,
            "R": 34,
            "S": 35,
            "T": 36,
            "U": 41,
            "V": 42,
            "W": 37,
            "X": 51,
            "Y": 52,
        }
        if symbolmodifier12 in mob_map:
            metadata_obj["mobility"] = ech_mob.get(mob_map[symbolmodifier12])
        else:
            metadata_obj["mobility"] = None

    if symbolmodifier11 == "N":
        if symbolmodifier12 == "S":
            metadata_obj["mobility"] = ech_mob.get(61)
        elif symbolmodifier12 == "L":
            metadata_obj["mobility"] = ech_mob.get(62)
        else:
            metadata_obj["mobility"] = None

    # Civilian stuff
    if (
        (battledimension == "A" and functionid.startswith("C"))
        or (battledimension == "G" and functionid.startswith("EVC"))
        or (battledimension == "S" and functionid.startswith("X"))
    ):
        metadata_obj["civilian"] = True

    # Colors will be have to be fixed in symbolColors
    if battledimension == "Z" or battledimension == "X":
        if affiliation in ["P", "U", "F", "N", "H", "A", "S", "G", "W"]:
            metadata_obj["dimensionUnknown"] = True

        if affiliation in ["F", "A"]:
            metadata_obj["dimension"] = "Sea"  # Hardcoded string in JS too

        if affiliation in ["D", "L", "M", "J", "K"]:
            metadata_obj["affiliation"] = "none"

    # Forcing unframing
    if battledimension == "S" and functionid in [
        "O-----",
        "ED----",
        "EP----",
        "EV----",
        "ZM----",
        "ZN----",
        "ZI----",
    ]:
        metadata_obj["frame"] = False

    if (
        codingscheme == "E"
        and battledimension == "N"
        and functionid
        in [
            "AA----",
            "AB----",
            "AC----",
            "AD----",
            "AE----",
            "AG----",
            "BB----",
            "BC----",
            "BF----",
            "BM----",
            "-C-----",
            "CA----",
            "CB----",
            "CC----",
            "CD----",
            "CE----",
        ]
    ):
        metadata_obj["frame"] = False

    if (
        codingscheme == "W"
        and battledimension == "S"
        and functionid
        in [
            "WSVE--",
            "WSD-LI",
            "WSFGSO",
            "WSGRL-",
            "WSR-LI",
            "WSDSLM",
            "WSS-LI",
            "WSTMH-",
            "WST-FC",
            "WSTSS-",
        ]
    ):
        metadata_obj["frame"] = False

    # Special symbols that should be unframed but filled
    if battledimension == "U" and functionid in [
        "WM----",
        "WMD---",
        "WMG---",
        "WMGD--",
        "WMGX--",
        "WMGE--",
        "WMGC--",
        "WMGR--",
        "WMGO--",
        "WMM---",
        "WMMD--",
        "WMMX--",
        "WMME--",
        "WMMC--",
        "WMMR--",
        "WMMO--",
        "WMF---",
        "WMFD--",
        "WMFX--",
        "WMFE--",
        "WMFC--",
        "WMFR--",
        "WMFO--",
        "WMO---",
        "WMOD--",
        "WMX---",
        "WME---",
        "WMA---",
        "WMC---",
        "WMR---",
        "WMB---",
        "WMBD--",
        "WMN---",
        "WMS---",
        "WMSX--",
        "WMSD--",
        "WD----",
        "WDM---",
        "WDMG--",
        "WDMM--",
        "ND----",
        "E-----",
        "V-----",
        "X-----",
        "NBS---",
        "NBR---",
        "NBW---",
        "NM----",
        "NA----",
    ]:
        if metadata_obj.get("STD2525"):
            metadata_obj["fill"] = False
            if functionid == "WD----":
                metadata_obj["fill"] = True
            if functionid in [
                "ND----",
                "NBS---",
                "NBR---",
                "NBW---",
                "NM----",
                "NA----",
            ]:
                metadata_obj["fill"] = True
                metadata_obj["frame"] = False
        else:
            metadata_obj["frame"] = False
            if functionid in ["E-----", "V-----", "X-----"]:
                metadata_obj["fill"] = False
                metadata_obj["frame"] = False

    # EMS and tactical graphics
    if sidc.startswith("WAS") or sidc.startswith("WOS") or codingscheme == "G":
        metadata_obj["frame"] = False

    # APP6 tactical points with frames
    if (
        codingscheme == "G"
        and battledimension == "O"
        and functionid[0] in ["V", "L", "P", "I"]
    ):
        metadata_obj["frame"] = True
        metadata_obj["dimension"] = mapping["dimension"][1]

    return metadata_obj
