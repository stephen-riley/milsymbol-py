from .iconparts_functions import defaultProperties, text, textm1, textm2


def ground(ms, iconParts, metadata, colors, STD2525, monoColor, alternateMedal):
    frame = metadata.get("frame")
    affiliation = metadata.get("affiliation", "Friend")
    metadata.get("baseGeometry")
    numberSIDC = metadata.get("numberSIDC")

    iconColor = colors["iconColor"][affiliation]
    iconFillColor = colors["iconFillColor"][affiliation]
    black = colors["black"][affiliation]
    white = colors["white"][affiliation]

    icn = {}

    icn["GR.IC.MILITARY"] = text("MIL")
    icn["GR.I.GOVERNMENT"] = text("GOV")
    icn["GR.IC.SUBMARINE NUCLEAR PROPULSION"] = {
        "type": "path",
        "d": "m 75,110 -10,-10 10,-10 0,-10 50,0 0,10 10,10 -10,10 z",
    }
    icn["GR.IC.FERRY"] = [
        {
            "type": "path",
            "fill": iconFillColor
            if STD2525
            else (iconFillColor if not frame else False),
            "d": "m 75,100 0,-35 50,0 0,35 20,0 -15,35 -60,0 -15,-35 z",
        },
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 103,
            "fontsize": 30,
            "text": "FE" if STD2525 else "F",
        },
    ]
    icn["GR.IC.ADMINISTRATIVE"] = text("ADM")
    icn["GR.IC.MANUAL TRACK"] = text("MAN")
    icn["GR.IC.AIR DEFENSE CHAPARRAL"] = [
        {
            "type": "path",
            "fill": False,
            "d": "m 85,80 30,0 c 5.54,0 10,4.46 10,10 l 0,5 c 0,5.54 -4.46,10 -10,10 l -30,0 c -5.54,0 -10,-4.46 -10,-10 l 0,-5 c 0,-5.54 4.46,-10 10,-10 z",
        },
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 95,
            "fontsize": 20,
            "text": "C",
        },
    ]
    icn["GR.IC.AIR DEFENSE COMPOSITE"] = {
        "type": "path",
        "d": "M85,120 C85,110 115,110 115,120 M90,115 L90,90 C90,80 110,80 110,90 L110,115 M100,112 l0,-30",
        "fill": False,
    }
    icn["GR.IC.AIR DEFENSE H/MAD"] = text("HMD")
    icn["GR.IC.AIR DEFENSE H/MAD HAWK"] = {
        "type": "text",
        "stroke": False,
        "x": 100,
        "y": 101,
        "fontsize": 20,
        "text": "H",
    }
    icn["GR.IC.AIR DEFENSE H/MAD PATRIOT"] = {
        "type": "text",
        "stroke": False,
        "x": 100,
        "y": 101,
        "fontsize": 20,
        "text": "P",
    }
    icn["GR.IC.AIR DEFENSE MISSILE"] = {
        "type": "path",
        "d": "M90,120 L90,90 C90,80 110,80 110,90 L110,120",
        "fill": False,
    }
    icn["GR.IC.FLOATING CRAFT"] = {
        "type": "path",
        "d": "m 90,75 20,0 0,-10 -5,0 0,-10 -10,0 0,10 -5,0 z",
        "stroke": False,
    }
    icn["GR.IC.AIR AND MISSILE DEFENSE"] = text("MD")
    icn["GR.IC.MILITARY HISTORY"] = text("MH")
    icn["GR.IC.AIR DEFENSE TARGETING UNIT"] = [
        {
            "type": "path",
            "d": "M80,100 l20,-15 0,15 20,-15 M75,80 C75,100 85,115 105,115",
            "fill": False,
        },
        {"type": "circle", "cx": 75, "cy": 110, "r": 5},
    ]
    icn["GR.IC.AIR DEFENSE THEATER MISSILE DEFENSE UNIT"] = text("TMD")
    icn["GR.IC.AIR DEFENSE SHORT RANGE"] = text("SRD")
    icn["GR.IC.AIR DEFENSE STINGER"] = [
        {
            "type": "path",
            "fill": False,
            "d": "m 85,80 30,0 c 5.54,0 10,4.46 10,10 l 0,5 c 0,5.54 -4.46,10 -10,10 l -30,0 c -5.54,0 -10,-4.46 -10,-10 l 0,-5 c 0,-5.54 4.46,-10 10,-10 z",
        },
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 95,
            "fontsize": 20,
            "text": "S",
        },
    ]
    icn["GR.IC.AIR DEFENSE VULCAN"] = [
        {
            "type": "path",
            "fill": False,
            "d": "m 85,80 30,0 c 5.54,0 10,4.46 10,10 l 0,5 c 0,5.54 -4.46,10 -10,10 l -30,0 c -5.54,0 -10,-4.46 -10,-10 l 0,-5 c 0,-5.54 4.46,-10 10,-10 z",
        },
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 95,
            "fontsize": 20,
            "text": "V",
        },
    ]
    icn["GR.IC.AIR DEFENSE GUN UNIT"] = {
        "type": "path",
        "d": "M100,80 L100,120 M92,90 l0,20 M108,90 l0,20",
        "fill": False,
    }
    icn["GR.IC.AIR TRAFFIC SERVICES"] = {
        "type": "path",
        "d": "m 100,95 0,25 m 7.5,-32.5 c 0,4.1 -3.4,7.5 -7.5,7.5 -4.1,0 -7.5,-3.4 -7.5,-7.5 0,-4.1 3.4,-7.5 7.5,-7.5 4.1,0 7.5,3.4 7.5,7.5 z M 60,85 l 40,15 40,-15 0,30 -40,-15 -40,15 z",
    }
    icn["GR.IC.AIRPORT OF DEBARKATION"] = [
        {
            "type": "path",
            "fill": False,
            "d": "M80,70 l40,0 M80,80 l25,-25 M100,80 l0,40 M81,90.5 l38,19 M81,109.5 l38,-19",
        },
        {"type": "circle", "cx": 100, "cy": 100, "r": 20, "fill": False},
    ]
    icn["GR.IC.ALLIED COMMAND EUROPE RAPID REACTION CORPS (ARRC)"] = text("ARRC")
    icn["GR.IC.ALLIED COMMAND OPERATIONS"] = text("ACO")
    icn["GR.IC.AMMUNITION"] = {
        "type": "path",
        "d": "m 90,117 0,-25 c 0,-15 20,-15 20,0 l 0,25 m -25,0 30,0",
        "fill": False,
    }
    icn["GR.IC.ARMOUR"] = {
        "type": "path",
        "d": "M125,80 C150,80 150,120 125,120 L75,120 C50,120 50,80 75,80 Z",
        "fill": False,
    }
    icn["GR.IC.ARMOR, WHEELED"] = [
        {
            "type": "path",
            "d": "m 120,80 c 25,0 25,30 0,30 l -40,0 C 55,110 55,80 80,80 Z",
            "fill": False,
        },
        {"type": "circle", "cx": 70, "cy": 115, "r": 5, "fill": False},
        {"type": "circle", "cx": 100, "cy": 115, "r": 5, "fill": False},
        {"type": "circle", "cx": 130, "cy": 115, "r": 5, "fill": False},
    ]
    icn["GR.IC.AVIATION ROTARY WING"] = {
        "type": "path",
        "stroke": False,
        "d": "M60,85 l40,15 40,-15 0,30 -40,-15 -40,15 z",
    }
    icn["GR.IC.AVIATION ROTARY WING 2525C"] = {
        "type": "path",
        "stroke": False,
        "d": "M100,100 L100,140",
    }
    icn["GR.IC.AVIATION FIXED WING"] = {
        "type": "path",
        "stroke": False,
        "d": "M100,100 L130,88 c15,0 15,24 0,24 L100,100 70,112 c-15,0 -15,-24 0,-24 Z",
    }
    icn["GR.IC.COMBATANT"] = [
        {
            "type": "path",
            "d": "m 86.9,110 c -3.6,2 -7.2,3.9 -10.8,5.9 2.1,2.9 6.7,3.9 10,2.1 2.6,-0.9 4.7,-3.8 3.1,-6.1 -0.8,-0.6 -1.5,-1.3 -2.3,-1.9 z m 26.3,0.1 c 3.6,2 7.2,3.9 10.8,5.9 -2.1,2.9 -6.7,3.9 -10,2.1 -2.6,-0.9 -4.7,-3.8 -3.1,-6.1 0.8,-0.6 1.5,-1.3 2.3,-1.9 z",
            "fill": False,
        },
        {
            "type": "path",
            "d": "m 112.9,110 c -5.6,-4 -11.3,-7.9 -16.1,-12.5 -4.2,-4.5 -7,-9.8 -9.2,-15.1 -0.8,4.4 -0.9,9.3 2.4,13.2 3.6,4.5 8.6,8.1 13.5,11.8 2.3,1.7 4.7,3.3 7.1,4.8 0.8,-0.7 1.5,-1.5 2.3,-2.2 m -25.7,0 c 5.6,-4 11.3,-7.9 16.1,-12.5 4.2,-4.5 7,-9.8 9.2,-15.1 0.8,4.4 0.9,9.3 -2.4,13.2 -3.6,4.5 -8.6,8.1 -13.5,11.8 -2.3,1.7 -4.7,3.3 -7.1,4.8 -0.8,-0.7 -1.5,-1.5 -2.3,-2.2",
            "fill": white,
            "strokewidth": 2,
        },
    ]
    icn["GR.IC.AVIATION COMPOSITE"] = {
        "type": "path",
        "stroke": False,
        "d": "m 100,100 15.7,7.9 c 11.8,0 11.8,-15.7 0,-15.7 z m 0,0 -15.7,-7.9 c -11.8,0 -11.8,15.7 0,15.7 z m -10,-20 10,20 -10,20 20,0 -10,-20 10,-20 z",
    }
    icn["GR.IC.AVIATION TACTICAL AIR CONTROL PARTY"] = text("TACP")
    icn["GR.IC.AVIATION FORWARD AIR CONTROLLER"] = text("FAC")
    icn["GR.IC.SPECIAL TROOPS"] = text("ST")
    icn["GR.IC.MULTI-DOMAIN"] = {
        "type": "path",
        "d": "m 79.3,98.2 v -7 h 7.1  M 100,112 79.3,91.2  M 76,107 l -5,5 5,6  m 24,-6 H 71  m 53,-5 5,5 -5,6  m -24,-6 h 29  M 114,91.2 h 7 v 7.1  M 100,112 121,91.2  m -26,-3.8 5,-5 5,5  M 100,112 V 82.4",
        "fill": False,
    }
    icn["GR.IC.RANGER"] = text("RGR")
    icn["GR.IC.BAND"] = text("BAND")
    icn["GR.IC.ARMY MUSIC"] = {
        "type": "path",
        "d": "m 99.6,110.5 c -4.8,-1.4 -10.9,2.2 -10.4,7.7 1,2.5 6.2,2.4 9.6,-0.2 1.9,-1.5 2.7,-3.8 2.3,-6.9 l -0.1,-21.3 c 12.7,5.8 7.6,14.8 5.6,20.7 4.7,-4.9 5.8,-13.2 1.5,-17.9 -4.4,-4.6 -5,-7 -8.4,-13 z",
        "strokewidth": 2,
    }
    icn[
        "GR.IC.BUREAU OF ALCOHOL, TOBACCO, FIREARMS AND EXPLOSIVES (ATF) (DEPARTMENT OF JUSTICE)"
    ] = text("ATF")
    icn["GR.IC.CBRN"] = [
        {
            "type": "path",
            "d": "m 74,120 c 0,-15 13.2,-32.9 65,-36  m -13,36 C 126,105 113,87.1 61.5,84",
            "fill": False,
        },
        {"type": "circle", "cx": 65, "cy": 90, "r": 6},
        {"type": "circle", "cx": 135, "cy": 90, "r": 6},
    ]
    icn["GR.CHEMICAL, BIOLOGICAL, RADIOLOGICAL, NUCLEAR, AND HIGH-YIELD EXPLOSIVES"] = [
        {
            "type": "path",
            "d": "M 89.5,82 H 111 l 10,18 -10,18 H 89.5 L 79,100 Z",
            "fill": iconFillColor,
        },
        {
            "type": "text",
            "stroke": False,
            "alignmentBaseline": "middle",
            "textanchor": "middle",
            "x": 100,
            "y": 102,
            "fontsize": 25,
            "text": "E",
        },
    ]
    icn["GR.IC.SPACE"] = [
        {
            "type": "path",
            "d": "M 97.5,104.2 92,108 96,102.5 85,100 96,98.53 92,93 98.09,96.98 100,80 102.5,96.98 109,93 l -5,5.53 11,1.47 -11,2.5 5,5.5 -6.5,-3.8 -2.5,15.8 z",
            "stroke": False,
        }
    ]
    icn["GR.IC.CIVIL AFFAIRS"] = text("CA")
    icn["GR.IC.CIVIL-MILITARY-COOPERATION"] = {
        "type": "path",
        "d": "m 65,85 h 69 v 15 c 0,20 -69,20 -69,0 z",
        "fill": False,
    }
    icn["GR.I.CIVILIAN"] = text("CIV")
    # Handling prop assignment
    icn["GR.I.CIVILIAN"]["fill"] = (
        iconFillColor
        if (STD2525 or numberSIDC)
        else (iconFillColor if not frame else False)
    )
    icn["GR.I.CIVILIAN"]["stroke"] = black
    icn["GR.I.CIVILIAN"]["strokewidth"] = 3

    icn["GR.IC.COMMAND AND CONTROL"] = text("")
    icn["GR.IC.COMBAT"] = text("CBT")
    icn["GR.IC.COMBAT SERVICE SUPPORT"] = text("CSS")
    icn["GR.IC.COMBAT SUPPORT"] = text("CS")
    icn["GR.IC.COMBAT SUPPORT (MANOEUVRE ENHANCEMENT)"] = {
        "type": "path",
        "d": "m 85,80 0,25 15,15 15,-15 0,-25 z",
    }
    icn["GR.IC.COMBINED ARMS"] = {
        "type": "path",
        "d": "m 70,80 60,40 m 0,-40 -60,40 m 55,-40 c 25,0 25,40 0,40 l -50,0 C 50,120 50,80 75,80 z",
        "fill": False,
    }
    icn["GR.IC.COUNTER-INTELLIGENCE"] = text("CI")
    icn["GR.IC.CRIMINAL INVESTIGATION DIVISION"] = text("CID")
    icn["GR.IC.CYBER"] = text("CYB")
    icn["GR.IC.DIVING"] = []
    icn["GR.IC.DOG"] = text("DOG")
    icn["GR.IC.DRILLING"] = {"type": "path", "d": "m 85,80 5,40 20,0 5,-40 z"}
    icn["GR.IC.DRUG ENFORCEMENT AGENCY (DEA)"] = text("DEA")
    icn["GR.IC.ELECTRONIC RANGING"] = {
        "type": "path",
        "d": "M 108,117 C 86,129 65,93 86.7,80.7 Z  M 97.2,99.1 118,88.7",
        "fill": iconFillColor if STD2525 else False,
    }
    icn["GR.IC.ELECTRONIC WARFARE"] = text("EW")
    icn["GR.IC.EMERGENCY MEDICAL OPERATION"] = {
        "type": "path",
        "d": "m 90,60 0,22.7 -19.7,-11.3 -10,17.3 L 80,100 l -19.7,11.3 10,17.3 L 90,117.3 90,140 l 20,0 0,-22.7 19.7,11.3 10,-17.3 L 120,100 l 19.7,-11.3 -10,-17.3 L 110,82.7 110,60 90,60 z",
    }
    icn["GR.IC.ENGINEER"] = {
        "type": "path",
        "fill": False,
        "d": "M 60,118 V 83 h 80 v 35  M 100,83 V 110",
    }
    icn["GR.IC.ENGINEER MECHANIZED"] = {
        "type": "path",
        "fill": False,
        "d": "m 100,90 0,15 m -25,5 0,-20 50,0 0,20 m 0,-30 c 25,0 25,40 0,40 l -50,0 C 50,120 50,80 75,80 Z",
    }
    icn["GR.IC.ENGINEER UTILITY VEHICLE"] = {
        "type": "path",
        "fill": False,
        "d": "m 100,100 0,10 m -15,5 0,-15 30,0 0,15 M 70,80 c 0,15 60,15 60,0 l 0,40 -60,0 z",
    }
    icn["GR.IC.ENVIRONMENTAL PROTECTION"] = {
        "type": "path",
        "d": "m 100,80 -10,15 5,0 -10,10 5,0 -10,10 15,0 0,5 10,0 0,-5 15,0 -10,-10 5,0 -10,-10 5,0 z",
        "fill": False,
    }
    icn["GR.IC.EXPLOSIVE ORDNANCE DISPOSAL"] = text("EOD")
    icn["GR.IC.FEDERAL BUREAU OF INVESTIGATION (FBI)"] = text("FBI")
    icn["GR.IC.FIELD ARTILLERY"] = {"type": "circle", "cx": 100, "cy": 100, "r": 15}
    icn["GR.IC.FIELD ARTILLERY OBSERVER"] = [
        {"type": "circle", "cx": 100, "cy": 108, "r": 5},
        {"type": "path", "d": "m 100,80 -25,40 50,0 z", "fill": False},
    ]
    icn["GR.IC.FIELD CAMP CONSTRUCTION"] = [
        icn["GR.IC.ENGINEER"],
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 72,
            "fontsize": 25,
            "text": "CAMP",
        },
    ]
    icn["GR.IC.FINANCE"] = {
        "type": "path",
        "d": "m 80,95 10,-10 20,0 10,10 m -40,0 0,20 40,0 0,-20 z",
        "fill": False,
    }
    icn["GR.IC.FIRE PROTECTION"] = {
        "type": "path",
        "d": "m 120,90 -5,5 -10,-10 5,-5 -20,0 5,5 -10,10 -5,-5 0,20 5,-5 10,10 -5,5 20,0 -5,-5 10,-10 5,5 z",
    }
    icn["GR.IC.FIXED WING MISO"] = [
        {
            "type": "path",
            "fill": iconFillColor if STD2525 else False,
            "stroke": black,
            "d": "M70,85 l40,0 10,-10 0,50 -10,-10 -40,0 z M120,85 l10,0 M120,95 l10,0 M120,105 l10,0 M120,115 l10,0",
        },
        {
            "type": "path",
            "d": "M 78.8 61.5 C 68.1 61.5 68.1 78.5 78.8 78.5 L 100 70 L 78.8 61.5 z M 100 70 L 121.3 78.5 C 131.9 78.5 131.9 61.5 121.3 61.5 L 100 70 z",
        },
    ]
    icn["GR.IC.GEOSPATIAL SUPPORT"] = text("GEO")
    icn["GR.IC.GOVERNMENT ORGANIZATION"] = text("GO")
    icn["GR.IC.GRENADE"] = {
        "type": "path",
        "d": "m 86,105 h 28  M 95,92 v -9 h 10 v 9  m 0,-5.3 a 19,19 0 0 1 14,18.3  m -5,0 A 14.3,14.3 0 0 1 99.9,119 14.3,14.3 0 0 1 85.6,105 14.3,14.3 0 0 1 99.9,90.7 14.3,14.3 0 0 1 114,105 Z",
        "fill": False,
    }
    icn["GR.IC.HUMAN RESOURCES"] = text("HR")
    icn["GR.IC.INFORMATION OPERATIONS"] = text(
        "IW" if (STD2525 and not numberSIDC) else "IO"
    )
    icn["GR.IC.INTERNATIONAL SECURITY ASSISTANCE FORCE (ISAF)"] = text("ISAF")
    icn["GR.IC.INTERROGATION"] = text("IPW")
    icn["GR.IC.ISOLATED PERSONNEL"] = [
        {
            "type": "path",
            "d": "M 100,100 88,88  m 12,12 12,-12  m -12,30 v -18  m -9.5,18 H 110",
            "fill": False,
        },
        {
            "type": "path",
            "d": "m 106,87.2 a 5.92,5.92 0 0 1 -6,5.9 5.92,5.92 0 0 1 -5.9,-5.9 5.92,5.92 0 0 1 5.9,-6 5.92,5.92 0 0 1 6,6 z",
            "stroke": False,
        },
    ]
    icn["GR.IC.JOINT FIRE SUPPORT"] = text("JFS")
    icn["GR.IC.JOINT INFORMATION BUREAU"] = text("JIB")
    icn["GR.IC.JOINT INTELLIGENCE CENTRE"] = text("JIC")
    icn["GR.IC.JUDGE ADVOCATE GENERAL"] = text("JAG")
    icn["GR.IC.LABOUR"] = {
        "type": "path",
        "d": "m 90,85 20,0 m -10,0 0,25 -10,0 10,10 10,-10 -10,0",
        "fill": False,
    }
    icn["GR.IC.LAUNDRY/BATH"] = {
        "type": "path",
        "d": "m 95,80 10,10 0,30 m 0,-30 -10,0 m 10,0 -10,10",
        "fill": False,
    }
    icn["GR.IC.LAW ENFORCEMENT"] = {
        "type": "path",
        "d": "m 82,82 c 6,7 12,7 18,0 6,7 12,7 18,0  m 0,0 c -3,13 6,27 -18,36 C 76,109 85,95 82,82",
        "fill": False,
    }
    icn["GR.IC.LAW ENFORCEMENT VESSEL"] = [
        {
            "type": "path",
            "fill": iconFillColor
            if STD2525
            else (iconFillColor if not frame else False),
            "d": "m 75,100 0,-35 50,0 0,35 20,0 -15,35 -60,0 -15,-35 z",
        },
        {"type": "path", "d": "m 135,100 -15,35 -10,0 15,-35 z"},
    ]
    icn["GR.IC.LIAISON"] = text("LO")
    icn["GR.IC.MAINTENANCE"] = {
        "type": "path",
        "d": "M70,90 c10,0 10,20 0,20 m10,-10 l40,0 m10,-10 c-10,0 -10,20 0,20",
        "fill": False,
    }
    icn["GR.IC.MATERIEL"] = text("MAT")
    icn["GR.IC.MEDICAL EVACUATION HELICOPTER"] = {
        "type": "path",
        "d": "M60,85 l40,15 40,-15 0,30 -40,-15 -40,15 z M95.5,80 l9,0 0,-9 9,0 0,-9 -9,0 0,-9 -9,0 0,9 -9,0 0,9 9,0 Z",
    }
    icn["GR.IC.MESSENGER"] = text("M")
    icn["GR.IC.METEOROLOGICAL"] = text("MET")
    icn["GR.IC.MILITARY INFORMATION SUPPORT OPERATIONS (MISO)"] = {
        "type": "path",
        "d": "M 83.7,89 H 106 l 8,-6.8 V 118 l -8,-8 H 83.7 Z  m 30.3,0.3 h 11  m -11,7.1 h 11  m -11,6.6 h 11  m -11,7 h 11",
    }
    icn["GR.IC.MILITARY INTELLIGENCE"] = text("MI")
    icn["GR.IC.MILITARY POLICE"] = text("MP")
    icn["GR.IC.MINE"] = {
        "type": "path",
        "d": "m 120,100 c 0,5.5 -9,10 -20,10 -11,0 -20,-4.5 -20,-10 0,-5.5 9,-10 20,-10 11,0 20,4.5 20,10 z m -5,-20 -30,40 m 0,-40 30,40 m -15,-40 0,40",
    }
    icn["GR.IC.MINE CLEARING"] = [
        icn["GR.IC.MINE"],
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 72,
            "fontsize": 25,
            "text": "CLR",
        },
    ]
    icn["GR.IC.MINE LAUNCHING"] = [
        icn["GR.IC.MINE"],
        {"type": "path", "d": "m 80,125 0,10 40,0 0,-10 z"},
    ]
    icn["GR.IC.MINE LAYING"] = [
        icn["GR.IC.MINE"],
        {"type": "path", "d": "m 80,65 0,10 40,0 0,-10 z"},
    ]
    icn["GR.IC.MISSILE"] = {
        "type": "path",
        "d": "M 100,82.62 V 120  M 90,120 V 90 c 0,-10 20,-10 20,0 v 30",
        "fill": False,
    }
    icn["GR.IC.MISSILE.LIGHT"] = {"type": "path", "d": "M90,90 L110,90"}
    icn["GR.IC.MISSILE.MEDIUM"] = {"type": "path", "d": "M90,90 L110,90 M90,97 L110,97"}
    icn["GR.IC.MISSILE.HEAVY"] = {
        "type": "path",
        "d": "M90,90 L110,90 M90,97 L110,97 M90,104 L110,104",
    }
    icn["GR.IC.MORALE, WELFARE, AND RECREATION"] = {
        "type": "text",
        "stroke": False,
        "x": 100,
        "y": 110,
        "fontsize": 30,
        "text": "MWR",
    }
    icn["GR.IC.MORTAR"] = [
        {"type": "circle", "cx": 100, "cy": 115, "r": 5, "fill": False},
        {"type": "path", "d": "M100,111 l0,-30 M90,90 l10,-10 10,10", "fill": False},
    ]
    icn["GR.IC.MORTUARY AFFAIRS"] = {
        "type": "path",
        "d": "m 70,85 h 60 v 30 H 70 Z  m 40,5 v 20  M 74.8,100 H 125",
        "fill": False,
    }
    icn["GR.IC.MULTINATIONAL (MN)"] = text("MN")
    icn["GR.IC.NAVAL"] = [
        {
            "type": "path",
            "d": "m 105,85 c 0,2.8 -2.2,5 -5,5 -2.8,0 -5,-2.2 -5,-5 0,-2.8 2.2,-5 5,-5 2.8,0 5,2.2 5,5 z m -20,5 30,0 m -15,0 0,30",
            "fill": False,
        },
        {
            "type": "path",
            "d": "m 114,110 -3,-2 7,-5 -1,9 -3,-2 c -8,12 -18.6,12 -28,0 l -3,2 -2,-10 8,6 -3,2 c 9.3,11 19,11 28,0 z",
        },
    ]
    icn["GR.IC.OBSERVER/OBSERVATION"] = {
        "type": "path",
        "d": "m 100,80 -25,40 50,0 z",
        "fill": False,
    }
    icn["GR.IC.ORDNANCE"] = {
        "type": "path",
        "d": "M 90,97 83,83 m 27,14 7,-14 M 95,95 90,81 m 15,14 5,-14 m 10,26.5 c 0,6.9 -9,12.5 -20,12.5 -11,0 -20,-5.6 -20,-12.5 0,-6.9 9,-12.5 20,-12.5 11,0 20,5.6 20,12.5 z",
        "fill": False,
    }
    icn["GR.IC.PERSONNEL SERVICES"] = text("PS")
    icn["GR.IC.PETROLEUM OIL LUBRICANTS"] = {
        "type": "path",
        "d": "m 100,119 0,-24 m 0,0 C 99,95 85,81 85,81 l 30,0 z",
        "fill": False,
    }
    icn["GR.IC.PIPELINE"] = {
        "type": "path",
        "d": "m 115,110 15,0 m -15,-15 15,0 m -45,15 -15,0 M 85,95 70,95 m 30,-15 0,10 -15,0 0,25 30,0 0,-25 -15,0 m -10,-10 20,0",
        "fill": False,
    }
    icn["GR.IC.POSTAL"] = {
        "type": "path",
        "d": "m 80,80 30,0 c -1.4,15.5 0,25 10,35 -20,0 -40,-20 -40,-35 z",
        "fill": False,
    }
    icn["GR.IC.PUBLIC AFFAIRS"] = text("PA")
    icn["GR.IC.PUBLIC AFFAIRS BROADCAST"] = text("BPAD")
    icn["GR.IC.PSYCHOLOGICAL OPERATIONS"] = {
        "type": "path",
        "fill": iconFillColor if STD2525 else False,
        "stroke": black,
        "d": "M70,85 l40,0 10,-10 0,50 -10,-10 -40,0 z M120,85 l10,0 M120,95 l10,0 M120,105 l10,0 M120,115 l10,0",
    }
    icn["GR.IC.QUARTERMASTER"] = {
        "type": "path",
        "fill": False,
        "d": "m 115,95 c 0,15 15,15 15,0 0,-15 -15,-15 -15,0 z m 0,0 -45,0 0,10 10,0 0,-10",
    }
    icn["GR.IC.RADAR"] = {
        "type": "path",
        "d": "M72,95 l30,-25 0,25 30,-25 M70,70 c0,35 15,50 50,50",
        "fill": False,
    }
    icn["GR.IC.RADIO"] = [
        {
            "type": "path",
            "fill": False,
            "d": "M 100,108 V 82.5  m -12.5,4.1 4.1,-4.1 4.2,4.1 4.2,-4.1 4,4.1 4,-4.1 5,4.1  M 100,107 c -3.2,0 -5.9,3 -5.9,6 0,3 2.7,6 5.9,6 3,0 6,-3 6,-6 0,-3 -3,-6 -6,-6 z",
        }
    ]
    icn["GR.IC.RADIO RELAY"] = [
        {
            "type": "path",
            "fill": False,
            "d": "m 85,83 h 30  m -15,25 V 82.5  m 0,24.5 c -3.2,0 -5.9,3 -5.9,6 0,3 2.7,6 5.9,6 3,0 6,-3 6,-6 0,-3 -3,-6 -6,-6 z",
        }
    ]
    icn["GR.IC.RADIO TELETYPE CENTRE"] = [
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 110,
            "fontsize": 30,
            "text": "C",
        },
        {
            "type": "path",
            "fill": False,
            "d": "M 100,120 V 82  M 85.8,82 H 114  M 90.5,86.7 H 109",
        },
    ]
    icn["GR.IC.RAILHEAD"] = [
        {
            "type": "path",
            "fill": False,
            "d": "M100,80 l0,40 M81,90.5 l38,19 M81,109.5 l38,-19",
        },
        {"type": "circle", "cx": 100, "cy": 100, "r": 20, "fill": False},
        ms._translate(
            0,
            -50,
            [
                {"type": "path", "d": "M60,120 l80,0", "fill": False},
                {"type": "circle", "fill": False, "cx": 65, "cy": 125, "r": 5},
                {"type": "circle", "fill": False, "cx": 75, "cy": 125, "r": 5},
                {"type": "circle", "fill": False, "cx": 125, "cy": 125, "r": 5},
                {"type": "circle", "fill": False, "cx": 135, "cy": 125, "r": 5},
            ],
        ),
    ]
    icn["GR.IC.RELIGIOUS SUPPORT"] = text("REL")
    icn["GR.IC.REPLACEMENT HOLDING UNIT"] = text("RHU")
    icn["GR.IC.SEA-AIR-LAND"] = text("SEAL")
    icn["GR.IC.SUPPORT"] = text("SPT")
    icn["GR.IC.ARMY FIELD SUPPORT"] = text("AFS")
    icn["GR.IC.CONTRACTING SERVICES"] = text("KS")
    icn["GR.IC.SEAPORT OF DEBARKATION"] = [
        {
            "type": "path",
            "fill": False,
            "d": "M100,80 l0,40 M81,90.5 l38,19 M81,109.5 l38,-19",
        },
        {"type": "circle", "cx": 100, "cy": 100, "r": 20, "fill": False},
        ms._translate(0, -35, ms._scale(0.6, icn["GR.IC.NAVAL"], True)),
    ]
    icn["GR.IC.SECURITY"] = text("SEC")
    icn["GR.IC.SECURITY POLICE (AIR)"] = [
        text("SP"),
        {
            "type": "path",
            "d": "M 78.8 121.5 C 68.1 121.5 68.1 138.5 78.8 138.5 L 100 130 L 78.8 121.5 z M 100 130 L 121.3 138.5 C 131.9 138.5 131.9 121.5 121.3 121.5 L 100 130 z",
        },
    ]
    icn["GR.IC.SENSOR"] = {
        "type": "path",
        "d": "m 100,80 c 0,7.5 12.5,20 20,20 -7.5,0 -20,12.5 -20,20 0,-7.5 -12.5,-20 -20,-20 7.5,0 20,-12.5 20,-20 z",
    }
    icn["GR.IC.SHORE PATROL"] = text("SP")
    icn["GR.IC.SNIPER"] = {
        "type": "path",
        "fill": False,
        "d": "M 60 85 L 90 85 L 60 85 z M 110 85 L 140 85 L 110 85 z M 100 90 L 100 115 L 100 90 z",
    }
    icn["GR.IC.PARACHUTE RIGGER"] = {
        "type": "path",
        "fill": False,
        "d": "m 120,100 -20,20 -20,-20 m 0,0 c 0,-25 40,-25 40,0 l -40,0",
    }
    icn["GR.IC.SPECIAL FORCES"] = text("SF")
    icn["GR.IC.SPECIAL OPERATIONS FORCES"] = text("SOF")
    icn["GR.IC.SURVEILLANCE"] = {
        "type": "path",
        "stroke": False,
        "d": "m 100,80 -25,40 50,0 z",
    }
    icn["GR.IC.SURVEY"] = [
        {"type": "path", "d": "M85,120 l15,-15 15,15 ", "fill": False},
        {
            "type": "path",
            "d": "M100,105 l0,-25 20,12.5 z",
            "fill": iconFillColor if STD2525 else False,
        },
    ]
    icn["GR.IC.SUSTAINMENT"] = text("SUST")
    icn["GR.IC.TELEPHONE SWITCH"] = [
        {
            "type": "text",
            "stroke": False,
            "x": 100,
            "y": 135,
            "fontsize": 30,
            "text": "C",
        },
        {"type": "path", "fill": False, "d": "M100,140 l0,-80  M70,60 l60,0"},
    ]
    icn["GR.IC.TOPOGRAPHIC"] = {
        "type": "path",
        "fill": False,
        "d": "m 85,105 c 10,5 20,5 30,0 m -15,-15 15,30 m -30,0 15,-30 0,-10",
    }
    icn["GR.IC.TRANSPORTATION"] = [
        {
            "type": "path",
            "fill": False,
            "d": "M 119,100 A 18.5,18.3 0 0 1 99.4,118 18.5,18.3 0 0 1 81.2,100 18.5,18.3 0 0 1 99.4,81.8 18.5,18.3 0 0 1 119,100 Z  M 100,81.9 V 118  M 82.9,91.2 117,108  M 82.9,108 117,91.2",
        }
    ]
    icn["GR.IC.TRANSPORTATION SECURITY AGENCY (TSA)"] = text("TSA")
    icn["GR.IC.UNMANNED SYSTEMS"] = {
        "type": "path",
        "d": "m 60,84 40,20 40,-20 0,8 -40,25 -40,-25 z",
        "stroke": False,
    }
    icn["GR.IC.SEARCH AND RESCUE"] = text("SAR")
    icn["GR.IC.DIVER, CIVILIAN"] = {
        "type": "path",
        "fill": iconFillColor,
        "d": "M 114.3,94 C 114.3,102.3 107.9,109 100,109 c -7.9,0 -14.2,-6.7 -14.2,-15 0,-8.3 6.4,-15 14.2,-15 7.9,0 14.3,6.7 14.3,15 z m 0,27 14.3,15 -57,0 14.3,-15 M 125.7,79 l 14.3,0 0,30 -14.3,0 m -51.3,0 -14.3,0 0,-30 14.3,0 m 54.2,15 c 0,16.6 -12.8,30 -28.5,30 -15.7,0 -28.5,-13.4 -28.5,-30 C 71.5,77.4 84.3,64 100,64 115.7,64 128.5,77.4 128.5,94 z",
    }
    icn["GR.IC.VIDEO IMAGERY"] = {
        "type": "path",
        "fill": False,
        "d": "m 140,110 -26,0 m 7,-20 19,0 m -15,-10 -65,0 0,40 50,0 z m 15,5 0,30",
    }
    icn["GR.IC.UNITED STATES SECRET SERVICE(TREAS) (USSS)"] = text("USSS")
    icn["GR.IC.WATER"] = {
        "type": "path",
        "d": "m 65,90 50,0 c 10,0 20,10 20,20 m -40,-30 20,0 m -10,0 0,10",
        "fill": False,
    }
    icn["GR.IC.WATER PURIFICATION"] = [
        icn["GR.IC.WATER"],
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 90,
            "y": 105,
            "fontsize": 20,
            "text": "PURE",
        },
    ]
    icn["GR.IC.FF.AIR ASSAULT WITH ORGANIC LIFT"] = {
        "Unknown": {
            "type": "path",
            "d": "M35,120 L 85,120 l15,15 15,-15 L165,120",
            "fill": False,
        },
        "Friend": {
            "type": "path",
            "d": "M25,120 L 85,120 l15,15 15,-15L175,120",
            "fill": False,
        },
        "Neutral": {
            "type": "path",
            "d": "M45,120 L 85,120 l15,15 15,-15 L155,120",
            "fill": False,
        },
        "Hostile": {
            "type": "path",
            "d": "M50,120 L 85,120 l15,15 15,-15 L150,120",
            "fill": False,
        },
    }.get(affiliation)
    icn["GR.IC.FF.AIR DEFENCE"] = {
        "Unknown": {
            "type": "path",
            "d": "m 55,135 c 10,-20 80,-20 90,0",
            "fill": False,
        },
        "Friend": {
            "type": "path",
            "d": "M25,150 C25,110 175,110 175,150",
            "fill": False,
        },
        "Neutral": {
            "type": "path",
            "d": "M45,150 C45,110 155,110 155,150",
            "fill": False,
        },
        "Hostile": {
            "type": "path",
            "d": "M70,140 C70,115 130,115 130,140",
            "fill": False,
        },
    }.get(affiliation)
    icn["GR.IC.FF.AIR AND NAVAL GUNFIRE LIAISON COMPANY"] = []

    icn["GR.IC.FF.NATO SUPPLY CLASS ALL"] = text("ALL")
    icn["GR.IC.FF.CLASS VI"] = [
        {"type": "circle", "cx": 100, "cy": 85, "r": 5, "fill": False},
        {
            "type": "path",
            "d": "m 85,95 30,0 m -15,15 0,-20 m -10,30 10,-10 10,10",
            "fill": False,
        },
    ]
    icn["GR.IC.FF.CLASS VII"] = [
        {"type": "circle", "cx": 75, "cy": 100, "r": 7},
        {"type": "circle", "cx": 125, "cy": 100, "r": 7},
        {"type": "path", "d": "M75,100 c0,-20 50,-20 50,0", "fill": False},
    ]
    icn["GR.IC.FF.CLASS VIII"] = {
        "Unknown": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-90 M165,80 l-130,0",
        },
        "Friend": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-70 M175,80 l-150,0",
        },
        "Neutral": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-75 M155,80 l-110,0",
        },
        "Hostile": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-92 M153,80 l-106,0",
        },
    }.get(affiliation)
    icn["GR.IC.FF.CLASS VIII.THEATER"] = {
        "Unknown": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-90 M155,80 l-110,0",
        },
        "Friend": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-70 M155,80 l-110,0",
        },
        "Neutral": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-75 M145,80 l-90,0",
        },
        "Hostile": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-92 M153,80 l-106,0",
        },
    }.get(affiliation)
    icn["GR.IC.FF.CLASS VIII.CORPS"] = {
        "Unknown": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-90 M155,80 l-120,0",
        },
        "Friend": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-70 M155,80 l-130,0",
        },
        "Neutral": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-75 M145,80 l-100,0",
        },
        "Hostile": {
            "type": "path",
            "fill": False,
            "d": "M100,120 l0,-92 M153,80 l-106,0",
        },
    }.get(affiliation)
    icn["GR.IC.FF.CLASS IX"] = [
        {"type": "circle", "cx": 100, "cy": 100, "r": 10, "fill": False},
        {
            "type": "path",
            "d": "m 100,110 0,10 m 0,-30 0,-10 m 8.7,14.2 8.4,-4.8 m -8.4,15.9 8,5.4 m -25.4,-5.4 -8.2,5.4 m 8.2,-16.3 -8,-5.4",
            "fill": False,
        },
    ]
    icn["GR.IC.EQUIPMENT MANUFACTURE"] = [
        {"type": "circle", "cx": 100, "cy": 100, "r": 20, "fill": False},
        {
            "type": "path",
            "d": "m 100,120 0,20 m 0,-60 0,-20 m 18.1,28.4 16,-9.6 m -16,31.2 16,12 M 82.5,110 66.1,122 M 82.5,88.8 66.5,78",
            "fill": False,
        },
    ]
    icn["GR.IC.FF.CLASS X"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 100,
        "y": 100,
        "fontsize": 30,
        "text": "CA",
    }
    icn["GR.IC.FF.THEATRE SUPPORT"] = {
        "Unknown": {
            "type": "path",
            "d": "M40,75 l15,25 -15,25 M160,75 l-15,25 15,25",
            "fill": False,
        },
        "Friend": {
            "type": "path",
            "d": "M25,50 l30,50 -30,50 M175,50 l-30,50 30,50",
            "fill": False,
        },
        "Neutral": {
            "type": "path",
            "d": "M45,50 l20,50 -20,50 M155,50 l-20,50 20,50",
            "fill": False,
        },
        "Hostile": {
            "type": "path",
            "d": "M50,80 l15,20 -15,20 M150,80 l-15,20 15,20",
            "fill": False,
        },
    }.get(affiliation)
    icn["GR.IC.FF.US MARSHALS SERVICE"] = {
        "type": "path",
        "stroke": False,
        "d": "m 100,84.25 3.7,10.66 11.3,0.21 -8.9,6.88 3.2,10.8 -9.3,-6.5 -9.24,6.5 3.26,-10.8 -8.98,-6.88 11.23,-0.21 z  m 0,-2.62 c -10.13,0 -18.37,8.24 -18.37,18.37 0,10.2 8.24,18.4 18.37,18.4 10.2,0 18.4,-8.2 18.4,-18.4 0,-10.13 -8.2,-18.37 -18.4,-18.37 z  m 0,2.62 c 8.8,0 15.7,7.04 15.7,15.75 0,8.8 -6.9,15.7 -15.7,15.7 -8.71,0 -15.75,-6.9 -15.75,-15.7 0,-8.71 7.04,-15.75 15.75,-15.75 z",
    }
    icn["GR.M1.ACCIDENT"] = textm1("ACC")
    icn["GR.M1.AIRMOBILE/AIR ASSAULT"] = {
        "type": "path",
        "fill": False,
        "d": "M85,55 L100,75 115,55",
    }
    icn["GR.M1.ARMORED"] = {
        "type": "path",
        "fill": False,
        "d": "m 90,60 20,0 c 10,0 10,15 0,15 L 90,75 C 80,75 80,60 90,60",
    }
    icn["GR.M1.CARGO"] = {
        "type": "path",
        "fill": False,
        "d": "m 100,60 0,15 -15,0 0,-15 30,0 0,15 -15,0",
    }
    icn["GR.M1.AMMUNITION"] = {
        "type": "path",
        "d": "M95,75 L95,60 C95,55 105,55 105,60 L105,75 M90,75 L110,75",
        "fill": False,
    }
    icn["GR.M1.AMPHIBIOUS WARFARE SHIP "] = {
        "type": "path",
        "d": "M 113,75 100,75 90,64.3 95,65 l 0,-8 10,0 0,8 5.5,-0.6 L 100,75",
    }
    icn["GR.M1.ANTISUBMARINE WARFARE"] = textm1("P")
    icn["GR.M1.AREA"] = textm1("AREA")
    icn["GR.M1.ARMY"] = {
        "type": "path",
        "fill": False,
        "d": "m 132,64.9 -13,12.7  m 0,-12.7 13,12.7  M 115,64.9 102,77.6  m 0,-12.7 13,12.7  M 97.9,64.9 85.2,77.6  m 0,-12.7 12.7,12.7  M 80.9,64.9 68.2,77.6  m 0,-12.7 12.7,12.7",
    }
    icn["GR.M1.ATTACK"] = textm1("A")
    icn["GR.M1.AVIATION"] = {"type": "path", "d": "m 75,60 0,15 50,-15 0,15 z"}
    icn["GR.M1.BATTALION"] = {
        "type": "path",
        "fill": False,
        "d": "m 105,60 v 18 0  M 95,60 v 18",
    }
    icn["GR.M1.BIOLOGICAL"] = textm1("B")
    icn["GR.M1.BORDER"] = textm1("BOR")
    icn["GR.M1.BRIDGING"] = {
        "type": "path",
        "fill": False,
        "d": "m 80,80 5,-5 30,0 5,5 m -40,-20 5,5 30,0 5,-5",
    }
    icn["GR.M1.BRIGADE"] = {
        "type": "path",
        "fill": False,
        "d": "m 107.5,62.5 -15,15  m 0,-15 15,15",
    }
    icn["GR.M1.CHEMICAL"] = textm1("C")
    icn["GR.M1.INTRUSION"] = textm1("I")
    icn["GR.M1.CHEMICAL SURVEILLANCE"] = textm1("RS")
    icn["GR.M1.CIVILIAN"] = textm1("CIV")
    icn["GR.M1.CLOSE PROTECTION"] = textm1("CLP")
    icn["GR.M1.COMBAT"] = textm1("CBT")
    icn["GR.M1.COMMAND AND CONTROL"] = textm1("C2")
    icn["GR.M1.COMMAND AND CONTROL ROTARY WING"] = (
        textm1("Y") if STD2525 else textm1("C2")
    )
    icn["GR.M1.TILT-ROTOR"] = textm1("TR")
    icn["GR.M1.COMMANDER"] = textm1("CDR")
    icn["GR.M1.COMMAND POST NODE"] = textm1("CPN")
    icn["GR.M1.COMMUNICATIONS CONTINGENCY PACKAGE"] = textm1("CCP")
    icn["GR.M1.CONSTRUCTION"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 100,
        "y": 70,
        "fontsize": 20,
        "text": "CONST",
    }
    icn["GR.M1.COMPANY"] = {"type": "path", "fill": False, "d": "M 100,59.6 V 78"}
    icn["GR.M1.CORPS"] = {
        "type": "path",
        "fill": False,
        "d": "m 127.5,62.5 -15,15  m 0,-15 15,15  m -20,-15 -15,15  m 0,-15 15,15  m -20,-15 -15,15  m 0,-15 15,15",
    }
    icn["GR.M1.CROSS CULTURAL COMMUNICATION"] = textm1("CCC")
    icn["GR.M1.CROWD AND RIOT CONTROL"] = textm1("CRC")
    icn["GR.M1.DECONTAMINATION"] = textm1("D")
    icn["GR.M1.DEMOLITION"] = textm1("DEM")
    icn["GR.M1.DETENTION"] = textm1("DET")
    icn["GR.M1.DEPUTY"] = textm1("DEP")
    icn["GR.M1.DIRECT COMMUNICATIONS"] = {
        "type": "path",
        "fill": False,
        "d": "m 95,65 -5,5 5,5 m 10,-10 5,5 -5,5 M 90,70 c 20,0 20,0 20,0 m 15,0 c 0,2.8 -2.2,5 -5,5 -2.8,0 -5,-2.2 -5,-5 0,-2.8 2.2,-5 5,-5 2.8,0 5,2.2 5,5 z m -40,0 c 0,2.8 -2.2,5 -5,5 -2.8,0 -5,-2.2 -5,-5 0,-2.8 2.2,-5 5,-5 2.8,0 5,2.2 5,5 z",
    }
    icn["GR.M1.DIVING"] = {
        "type": "path",
        "fill": False,
        "d": "m 104.6,64.8 c 0,2.7 -2.1,4.8 -4.6,4.8 -2.5,0 -4.6,-2.2 -4.6,-4.8 0,-2.7 2.1,-4.8 4.6,-4.8 2.5,0 4.6,2.2 4.6,4.8 z m 0,8.7 4.6,4.8 -18.3,0 4.6,-4.8 M 108.3,60 l 4.6,0 0,9.6 -4.6,0 m -16.5,0 -4.6,0 0,-9.6 4.6,0 m 17.4,4.8 c 0,5.3 -4.1,9.6 -9.2,9.6 -5.1,0 -9.2,-4.3 -9.2,-9.6 0,-5.3 4.1,-9.6 9.2,-9.6 5.1,0 9.2,4.3 9.2,9.6 z",
    }
    icn["GR.M1.DIVISION"] = {
        "type": "path",
        "fill": False,
        "d": "m 117.5,62.5 -15,15  m 0,-15 15,15  m -20,-15 -15,15  m 0,-15 15,15",
    }
    icn["GR.M1.MARINE DIVISION"] = textm1("D")
    icn["GR.M1.DESIGNATED MARKSMAN"] = textm1("DM")
    icn["GR.M1.DOG"] = textm1("DOG")
    icn["GR.M1.DRILLING"] = {"type": "path", "d": "m 90,60 5,15 10,0 5,-15 z"}
    icn["GR.M1.ELECTRO-OPTICAL"] = textm1("EO")
    icn["GR.M1.ENHANCED"] = textm1("ENH")
    icn["GR.M1.EXPLOSIVE ORDNANCE DISPOSAL"] = textm1("EOD")
    icn["GR.M1.EARLY WARNING RADAR"] = textm1("EWR")
    icn["GR.M1.FIELD ARTILLERY OBSERVER"] = [
        {"type": "circle", "cx": 100, "cy": 68, "r": 3},
        {"type": "path", "d": "M 100,53.1 85.8,75.9 H 114 Z", "fill": False},
    ]
    icn["GR.M1.FIRE DIRECTION CENTRE"] = textm1("FDC")
    icn["GR.M1.FORCE"] = textm1("F")
    icn["GR.M1.FORWARD"] = textm1("FWD")
    icn["GR.M1.GROUND STATION MODULE"] = textm1("GSM")
    icn["GR.M1.HIJACKING"] = textm1("H")
    icn["GR.M1.INDIVIDUAL"] = {"type": "path", "fill": False, "d": "M85,65 l30,0"}
    icn["GR.M1.INFANTRY"] = textm1("IN")
    icn["GR.M1.INTRUSION"] = textm1("I")
    icn["GR.M1.J1"] = textm1("J1")
    icn["GR.M1.J2"] = textm1("J2")
    icn["GR.M1.J3"] = textm1("J3")
    icn["GR.M1.J4"] = textm1("J4")
    icn["GR.M1.J5"] = textm1("J5")
    icn["GR.M1.J6"] = textm1("J6")
    icn["GR.M1.J7"] = textm1("J7")
    icn["GR.M1.J8"] = textm1("J8")
    icn["GR.M1.J9"] = textm1("J9")
    icn["GR.M1.JOINT FIRE SUPPORT"] = textm1("JFS")
    icn["GR.M1.JOINT NETWORK NODE"] = textm1("JNN")
    icn["GR.M1.LANDING SUPPORT"] = textm1("LS")
    icn["GR.M1.LARGE COMMUNICATIONS CONTINGENCY PACKAGE"] = textm1("LCCP")
    icn["GR.M1.LARGE EXTENSION NODE"] = textm1("LEN")
    icn["GR.M1.LIAISON"] = textm1("LO")
    icn["GR.M1.LOAD HANDLING SYSTEM"] = textm1("LHS")
    icn["GR.M1.MAINTENANCE"] = {
        "type": "path",
        "fill": False,
        "d": "m 83,70 h 34  m 8,-7 c -10,0 -10,14 0,14  M 75,63 c 10,0 10,14 0,14",
    }
    icn["GR.M1.MEDEVAC"] = {
        "type": "path",
        "stroke": False,
        "d": "M95.5,80 l9,0 0,-9 9,0 0,-9 -9,0 0,-9 -9,0 0,9 -9,0 0,9 9,0 Z",
    }
    icn["GR.M1.MESSENGER"] = textm1("MSG")
    icn["GR.M1.METEOROLOGICAL"] = textm1("MET")
    icn["GR.M1.MILITARY POLICE"] = textm1("MP")
    icn["GR.M1.MINE COUNTERMEASURE"] = textm1("MCM")
    icn["GR.M1.MISSILE"] = {
        "type": "path",
        "d": "M 95,78 V 58 c 0,-5 10,-5 10,0 v 20",
        "fill": False,
    }
    icn["GR.M1.(MOBILE) ADVISOR AND SUPPORT"] = {
        "type": "path",
        "d": "m 105,65 5,5 -5,5 M 90,70 c 20,0 20,0 20,0 m 15,0 c 0,2.8 -2.2,5 -5,5 -2.8,0 -5,-2.2 -5,-5 0,-2.8 2.2,-5 5,-5 2.8,0 5,2.2 5,5 z m -40,0 c 0,2.8 -2.2,5 -5,5 -2.8,0 -5,-2.2 -5,-5 0,-2.8 2.2,-5 5,-5 2.8,0 5,2.2 5,5 z",
        "fill": False,
    }
    icn["GR.M1.MOBILE SUBSCRIBER EQUIPMENT"] = textm1("MSE")
    icn["GR.M1.MOBILITY ASSAULT"] = textm1("MA")
    icn["GR.M1.MOBILITY SUPPORT"] = textm1("MS")
    icn["GR.M1.MOVEMENT CONTROL CENTRE"] = textm1("MCC")
    icn["GR.M1.MULTI-DOMAIN"] = {
        "type": "path",
        "d": "m 85.9,65.6 v -4.7 h 4.9  M 100,75 85.9,60.9  m -2.2,10.7 -3.4,3.4 3.4,4.1  M 100,75 H 80.3  m 35.7,-3.4 3,3.4 -3,4.1  M 100,75 h 19  M 109,60.9 h 5 v 4.8  M 100,75 114,60.9  m -17.4,-2.6 3.4,-3.4 3,3.4  M 100,75 V 54.9",
        "fill": False,
    }
    icn["GR.M1.MULTINATIONAL"] = textm1("MN")
    icn["GR.M1.MULTINATIONAL SPECIALIZED UNIT"] = textm1("MSU")
    icn["GR.M1.MULTIPLE ROCKET LAUNCHER"] = {
        "type": "path",
        "d": "M85,75 l15,-15 15,15 M85,67 l15,-15 15,15",
        "fill": False,
    }
    icn["GR.M1.NATO MEDICAL ROLE 1"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 120,
        "y": 72,
        "fontsize": 25,
        "text": "1",
    }
    icn["GR.M1.NATO MEDICAL ROLE 2"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 120,
        "y": 72,
        "fontsize": 25,
        "text": "2",
    }
    icn["GR.M1.NATO MEDICAL ROLE 2 BASIC"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 120,
        "y": 72,
        "fontsize": 25,
        "text": "2B",
    }
    icn["GR.M1.NATO MEDICAL ROLE 2 ENHANCED"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 120,
        "y": 72,
        "fontsize": 25,
        "text": "2E",
    }
    icn["GR.M1.NATO MEDICAL ROLE 2 FORWARD"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 120,
        "y": 72,
        "fontsize": 25,
        "text": "2E",
    }
    icn["GR.M1.NATO MEDICAL ROLE 3"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 120,
        "y": 72,
        "fontsize": 25,
        "text": "3",
    }
    icn["GR.M1.NATO MEDICAL ROLE 4"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 120,
        "y": 72,
        "fontsize": 25,
        "text": "4",
    }
    icn["GR.M1.NAVAL"] = ms._translate(0, -35, ms._scale(0.6, icn["GR.IC.NAVAL"], True))
    icn["GR.M1.NODE CENTRE"] = textm1("NC")
    icn["GR.M1.NUCLEAR"] = textm1("N")
    icn["GR.M1.OBSERVER"] = [
        {"type": "path", "d": "M 100,53.1 85.8,75.9 H 114 Z", "fill": False}
    ]
    icn["GR.M1.OF-1"] = textm1("O-1/O-2") if not STD2525 else textm1("OF-1")
    icn["GR.M1.OF-2"] = textm1("O-3") if STD2525 else textm1("OF-2")
    icn["GR.M1.OF-3"] = textm1("O-4") if STD2525 else textm1("OF-3")
    icn["GR.M1.OF-4"] = textm1("O-5") if STD2525 else textm1("OF-4")
    icn["GR.M1.OF-5"] = textm1("O-6") if STD2525 else textm1("OF-5")
    icn["GR.M1.OF-6"] = textm1("O-7") if STD2525 else textm1("OF-6")
    icn["GR.M1.OF-7"] = textm1("O-8") if STD2525 else textm1("OF-7")
    icn["GR.M1.OF-8"] = textm1("O-9") if STD2525 else textm1("OF-8")
    icn["GR.M1.OF-9"] = textm1("O-10") if STD2525 else textm1("OF-9")
    icn["GR.M1.OF-10"] = textm1("O-11") if STD2525 else textm1("OF-10")
    icn["GR.M1.OF-D"] = textm1("") if STD2525 else textm1("OF-D")
    icn["GR.M1.OPERATIONS"] = textm1("OPS")
    icn["GR.M1.OPTICAL"] = textm1("OPT")
    icn["GR.M1.OR-1"] = textm1("E-1") if STD2525 else textm1("OR-1")
    icn["GR.M1.OR-2"] = textm1("E-2") if STD2525 else textm1("OR-2")
    icn["GR.M1.OR-3"] = textm1("E-3") if STD2525 else textm1("OR-3")
    icn["GR.M1.OR-4"] = textm1("E-4") if STD2525 else textm1("OR-4")
    icn["GR.M1.OR-5"] = textm1("E-5") if STD2525 else textm1("OR-5")
    icn["GR.M1.OR-6"] = textm1("E-6") if STD2525 else textm1("OR-6")
    icn["GR.M1.OR-7"] = textm1("E-7") if STD2525 else textm1("OR-7")
    icn["GR.M1.OR-8"] = textm1("E-8") if STD2525 else textm1("OR-8")
    icn["GR.M1.OR-9"] = textm1("E-9") if STD2525 else textm1("OR-9")
    icn["GR.M1.OTHER"] = textm1("OTH")
    icn["GR.M1.PALLETIZED LOAD SYSTEM"] = textm1("PLS")
    icn["GR.M1.PERSONNEL RECOVERY"] = textm1("H")
    icn["GR.M1.PLATOON"] = [
        {"type": "circle", "stroke": False, "cx": 80, "cy": 68, "r": 8},
        {"type": "circle", "stroke": False, "cx": 100, "cy": 68, "r": 8},
        {"type": "circle", "stroke": False, "cx": 120, "cy": 68, "r": 8},
    ]
    icn["GR.M1.POLICE"] = {
        "type": "path",
        "fill": False,
        "d": "m 90.3,57.8 c 1.6,7 -3.4,14.7 9.7,19.6 13,-4.9 8,-12.6 10,-19.6  m 0,0 c -3,3.8 -7,3.8 -10,0  m 0,0 c -3.2,3.8 -6.5,3.8 -9.7,0",
    }
    icn["GR.M1.RADAR"] = {
        "type": "path",
        "fill": False,
        "d": "m 85,55 c 0.1,21.4 11.7,24.6 25,25 M 116,55 101,67.5 101,55 86.6,66.9",
    }
    icn["GR.M1.RADIO FREQUENCY IDENTIFICATION (RFID) INTERROGATOR/ SENSOR"] = textm1(
        "RF"
    )
    icn["GR.M1.RAILROAD"] = ms._translate(
        0,
        -50,
        [
            {"type": "path", "d": "M60,120 l80,0", "fill": False},
            {"type": "circle", "fill": False, "cx": 65, "cy": 125, "r": 5},
            {"type": "circle", "fill": False, "cx": 75, "cy": 125, "r": 5},
            {"type": "circle", "fill": False, "cx": 125, "cy": 125, "r": 5},
            {"type": "circle", "fill": False, "cx": 135, "cy": 125, "r": 5},
        ],
    )
    icn["GR.M1.RADIOLOGICAL"] = textm1("RAD")
    icn["GR.M1.RANGER"] = textm1("RGR")
    icn["GR.M1.RECON"] = textm1("R")
    icn["GR.M1.RECONNAISSANCE"] = textm1("REC")
    icn["GR.M1.REGIMENT"] = {
        "type": "path",
        "fill": False,
        "d": "m 110,60 v 18 0  M 90,60 v 18  m 10,-18 v 18",
    }
    icn["GR.M1.RETRANSMISSION SITE"] = textm1("RTNS")
    icn["GR.M1.ROBOTIC"] = {
        "type": "path",
        "d": "m 100,52.7 14.9,14.8 c 0.4,-0.3 0.9,-0.4 1.4,-0.4 1.5,0 2.7,1.2 2.7,2.7 0,1.4 -1.2,2.7 -2.7,2.7 -1.5,0 -2.7,-1.3 -2.7,-2.7 0,-0.4 0.1,-0.7 0.2,-1 l -10.4,-5.2 -2.5,8.6 c 0.2,0.1 0.4,0.2 0.6,0.3 0.7,0.5 1.2,1.3 1.2,2.3 0,1.5 -1.2,2.7 -2.7,2.7 -0.55,0 -1.06,-0.2 -1.49,-0.5 -0.73,-0.4 -1.22,-1.3 -1.22,-2.2 0,-1.2 0.77,-2.2 1.85,-2.6 l -2.53,-8.6 -10.42,5.2 c 0.12,0.3 0.18,0.6 0.18,1 0,1.5 -1.21,2.7 -2.7,2.7 -1.49,0 -2.7,-1.2 -2.7,-2.7 0,-1.5 1.21,-2.7 2.7,-2.7 0.52,0 1.01,0.1 1.42,0.4 l 14.9,-14.8 0,0 0,0 z",
        "stroke": False,
    }
    icn["GR.M1.SECOND IN COMMAND"] = textm1("SIC")
    icn["GR.M1.SIGNALER"] = textm1("SIG")
    icn["GR.M1.ASSAULT"] = textm1("ASLT")
    icn["GR.M1.WEAPON"] = textm1("WPN")
    icn["GR.M1.WEAPONS"] = textm1("W")
    icn["GR.M1.CRIMINAL INVESTIGATION DIVISION"] = textm1("CID")
    icn["GR.M1.DIGITAL"] = textm1("DIG")
    icn["GR.M1.NETWORK OR NETWORK OPERATIONS"] = textm1("NET")
    icn["GR.M1.AIRFIELD, AERIAL PORT OF DEBARKATION, OR AERIAL PORT OF EMBARKATION"] = {
        "type": "path",
        "d": "m 80,70 40,0 M 80,80 111,55",
        "fill": False,
    }
    icn["GR.M1.PIPELINE"] = {
        "type": "path",
        "d": "m 92,66 -12,0 m 12,8 -12,0 m 28,0 12,0 m -12,-8 12,0 m -20,-11 0,7 m -5,-7 10,0 m -13,7 0,16 16,0 0,-16 -16,0",
        "fill": False,
    }
    icn["GR.M1.POSTAL"] = {
        "type": "path",
        "d": "m 90,60 15,0 c 0,5 0,10 10,15 -15,0 -20,0 -25,-15",
        "fill": False,
    }
    icn["GR.M1.WATER"] = {
        "type": "path",
        "d": "m 92,59 h 16  m -8,9.7 V 59  M 75,69 h 40 c 10,0 15,5 15,10",
        "fill": False,
    }
    icn["GR.M1.INDEPENDENT COMMAND"] = {
        "type": "path",
        "d": "m 110,59 v 16  m -8,-8 h 16  M 90,59 v 16  m 8,-8 H 82",
        "fill": False,
    }
    icn["GR.M1.MULTI-PURPOSE BLADE"] = {
        "type": "path",
        "d": "m 80,65 20,-10 20,10 m -20,15 0,-25",
        "fill": False,
    }
    icn["GR.M1.TANK-WIDTH MINE PLOW"] = {
        "type": "path",
        "d": "m 80,65 5,-2.5 m 5,-2.5 5,-2.5 m 10,0 5,2.5 m 5,2.5 5,2.5 m -20,15 0,-20",
        "fill": False,
    }
    icn["GR.M1.ROUTE, RECONNAISSANCE, AND CLEARANCE"] = textm1("RRC")
    icn["GR.M1.SEARCH AND RESCUE"] = textm1("SAR")
    icn["GR.M1.SECTION"] = [
        {"type": "circle", "stroke": False, "cx": 90, "cy": 68, "r": 8},
        {"type": "circle", "stroke": False, "cx": 110, "cy": 68, "r": 8},
    ]
    icn["GR.M1.SECURITY"] = textm1("SEC")
    icn["GR.M1.SENSOR"] = {
        "type": "path",
        "d": "m 100,55 c -2,5 -5,8 -10,10 5,2 8,5 10,10 2,-5 5,-8 10,-10 -5,-2 -8,-5 -10,-10 z",
    }
    icn["GR.M1.SENSOR CONTROL MODULE"] = textm1("SCM")
    icn["GR.M1.SIGNALS INTELLIGENCE"] = {
        "type": "path",
        "fill": False,
        "d": "m 100,55 0,23 m -15,-18 5,-5 5,5 5,-5 5,5 5,-5 5,5",
    }
    icn["GR.M1.SIGNAL SUPPORT"] = textm1("SPT")
    icn["GR.M1.SINGLE SHELTER SWITCH"] = textm1("SSS")
    icn["GR.M1.SINGLE ROCKET LAUNCHER"] = {
        "type": "path",
        "d": "M85,75 l15,-15 15,15",
        "fill": False,
    }
    icn["GR.M1.SMALL EXTENSION NODE"] = textm1("SEN")
    icn["GR.M1.SMOKE"] = textm1("S")
    icn["GR.M1.SMOKE/DECON"] = textm1("SD")
    icn["GR.M1.SNIPER"] = {
        "type": "path",
        "d": "m 75,62 h 20  m 5,16 V 62.1  M 125,62 h -20",
        "fill": False,
    }
    icn["GR.M1.SOUND RANGING"] = textm1("SDR")
    icn["GR.M1.SPECIAL OPERATIONS FORCES (SOF)"] = textm1("SOF")
    icn["GR.M1.SPECIAL WEAPONS AND TACTICS"] = {
        "type": "text",
        "stroke": False,
        "x": 100,
        "y": 77,
        "fontsize": 23,
        "text": "SWAT",
    }
    icn["GR.M1.SQUAD"] = {
        "type": "circle",
        "stroke": False,
        "cx": 100,
        "cy": 68,
        "r": 8,
    }
    icn["GR.M1.SUPPORT"] = textm1("SPT")
    icn["GR.M1.SURVEY"] = {
        "type": "path",
        "d": "m 108,78 -8,-8 m 0,0 -8,8 m 8,-8 0,-15 15,8 z",
    }
    icn["GR.M1.TACTICAL EXPLOITATION"] = textm1("TE")
    icn["GR.M1.TARGET ACQUISITION"] = textm1("TA")
    icn["GR.M1.TEAM"] = [
        {"type": "circle", "fill": False, "cx": 100, "cy": 65, "r": 10},
        {"type": "path", "d": "m 90,75 l20,-20"},
    ]
    icn["GR.M1.THEATRE"] = {
        "type": "path",
        "fill": False,
        "d": "m 135,66.6 -11,11  m 0,-11 11,11  m -15,-11 -12,11  m 0,-11 12,11  m -15,-11 -10.7,11  m 0,-11 10.7,11  m -14.3,-11 -11.1,11  m 0,-11 11.1,11  m -14.9,-11 -11.1,11  m 0,-11 11.1,11",
    }
    icn["GR.M1.TOPOGRAPHIC"] = {
        "type": "path",
        "fill": False,
        "d": "m 92,65 c 6,3 10,3 16,0 m -18,13 10,-23 10,23",
    }
    icn["GR.M1.TRAINING CAMP"] = textm1("TNG")
    icn["GR.M1.HIJACKER"] = textm1("HJ")
    icn["GR.M1.UNMANNED AERIAL VEHICLE"] = {
        "type": "path",
        "stroke": False,
        "d": "m 80,65 20,13 20,-13 0,-5 -20,10 -20,-10 z",
    }
    icn["GR.M1.UPGRADED EARLY WARNING RADAR"] = textm1("UEW")
    icn["GR.M1.UTILITY"] = textm1("U")
    icn["GR.M1.VIDEO IMAGERY"] = {
        "type": "path",
        "fill": False,
        "d": "m 120,65 -11,0 m 11,10 -14,0 m 4,-14 -30,0 0,18 25,0 z m 10,2 0,14",
    }
    icn["GR.M1.WO-1"] = textm1("WO-1")
    icn["GR.M1.WO-2"] = textm1("WO-2")
    icn["GR.M1.WO-3"] = textm1("WO-3")
    icn["GR.M1.WO-4"] = textm1("WO-4")
    icn["GR.M1.WO-5"] = textm1("WO-5")
    icn["GR.M1.YARD"] = textm1("YRD")
    icn["GR.M2.AIRBORNE"] = {
        "type": "path",
        "d": "M75,140 C75,125 100,125 100,140 C100,125 125,125 125,140",
        "fill": False,
    }
    icn["GR.M2.ARCTIC"] = {
        "type": "path",
        "d": "M115,125 C125,125 125,135 115,135 L85,135 C75,135 75,125 85,125",
        "fill": False,
    }
    icn["GR.M2.ATTACK"] = textm2("A")
    icn["GR.M2.BLOOD"] = {
        "type": "path",
        "d": "m 120,121 c -2,7 -6,10 -6,13 0,3 2,6 6,6 4,0 6,-3 6,-6 0,-3 -4,-6 -6,-13 z",
        "stroke": False,
    }

    icn["GR.M2.ATTACK"] = textm2("A")
    icn["GR.M2.BLOOD"] = {
        "type": "path",
        "d": "m 120,121 c -2,7 -6,10 -6,13 0,3 2,6 6,6 4,0 6,-3 6,-6 0,-3 -4,-6 -6,-13 z",
        "stroke": False,
    }
    icn["GR.M2.COMBAT AND OPERATIONAL STRESS CONTROL"] = {
        "type": "path",
        "d": "m 118.5,132.9 v -8 q 0,-1.1 -0.4,-1.6 -0.5,-0.5 -2,-0.5 v -0.5 h 7.7 v 0.5 q -1.5,0 -2.1,0.5 -0.4,0.5 -0.4,1.6 v 8 q 2.4,-0.1 3.2,-1 0.8,-0.9 0.8,-3.4 v -2.2 q 0,-2.3 0.8,-3.2 0.7,-1 2.6,-1 0.4,0 0.7,0.1 0.3,0 0.6,0 v 0.6 h -0.5 q -0.8,0 -1.1,0.5 -0.2,0.5 -0.2,2.2 v 2.7 q 0,2.7 -1.7,4 -1.8,1.4 -5.1,1.6 v 2.4 q 0,1.2 0.4,1.7 0.6,0.6 2.1,0.6 v 0.5 h -7.7 v -0.5 q 1.5,0 2,-0.6 0.4,-0.4 0.4,-1.7 v -2.4 q -3.4,-0.2 -5.1,-1.6 -1.7,-1.3 -1.7,-4 v -2.7 q 0,-1.7 -0.2,-2.2 -0.3,-0.5 -1.2,-0.5 h -0.5 v -0.6 q 0.3,0 0.6,0 0.5,-0.1 0.7,-0.1 1.8,0 2.5,1 0.9,0.9 0.9,3.2 v 2.2 q 0,2.5 0.8,3.4 0.9,0.9 3.1,1 z",
        "stroke": False,
    }
    icn["GR.M2.LANDING CRAFT"] = textm2("LC")
    icn["GR.M2.LANDING SHIP"] = textm2("LS")
    icn["GR.M2.SERVICE CRAFT/YARD"] = textm2("YY")
    icn["GR.M2.TUG HARBOR"] = textm2("YT")
    icn["GR.M2.OCEAN GOING TUG BOAT"] = textm2("AT")
    icn["GR.M2.SURFACE DEPLOYMENT AND DISTRIBUTION COMMAND"] = textm2("SDDC")
    icn["GR.M2.COMPOSITE"] = textm2("COMP")
    icn["GR.M2.LIGHT AND MEDIUM"] = textm2("L/M")
    icn["GR.M2.BATTLE DAMAGE REPAIR"] = textm2("BDR")
    icn["GR.M2.BICYCLE EQUIPPED"] = {
        "type": "circle",
        "cx": 100,
        "cy": 132,
        "r": 11,
        "fill": False,
    }
    icn["GR.M2.CASUALTY STAGING"] = {
        "type": "text",
        "stroke": False,
        "textanchor": "middle",
        "alignmentBaseline": "middle",
        "x": 122,
        "y": 133,
        "fontsize": 18,
        "text": "CS",
    }
    icn["GR.M2.CLEARING"] = textm2("CLR")
    icn["GR.M2.CLOSE RANGE"] = textm2("CR")
    icn["GR.M2.COMBAT SEARCH AND RESCUE"] = textm2("CSAR")
    icn["GR.M2.CONTROL"] = {
        "type": "path",
        "d": "m 98,130 2,-4 2,4 m -8,8 -4,-2 4,-2 m 8,8 -2,4 -2,-4 m 8,-8 4,2 -4,2 m -14,-2 16,0 m -8,-8 0,16",
        "fill": False,
    }
    icn["GR.M2.NONCOMBATANT GENERIC VESSEL"] = {
        "type": "path",
        "d": "m 95,135 0,-10 10,0 0,10 5,0 0,10 -20,0 0,-10 z",
        "stroke": False,
    }
    icn["GR.M2.SHELTER"] = {
        "type": "path",
        "d": "m 85,140 30,0 -5,-15 -10,-5 -10,5 z",
        "stroke": False,
    }
    icn["GR.M2.SELF-PROPELLED"] = {
        "type": "path",
        "d": "m 85,125 30,0 c 10,0 10,15 0,15 l -30,0 c -10,0 -10,-15 0,-15",
        "fill": False,
    }
    icn["GR.M2.SURGICAL"] = {
        "type": "path",
        "d": "m 114,126 21,6 -21,6  m 0,-12 a 3.89,3.89 0 0 1 -3,3 3.89,3.89 0 0 1 -4,-3 3.89,3.89 0 0 1 4,-4 3.89,3.89 0 0 1 3,4 z  m 0,12 a 3.89,3.89 0 0 1 -3,4 3.89,3.89 0 0 1 -4,-4 3.89,3.89 0 0 1 4,-4 3.89,3.89 0 0 1 3,4 z",
        "fill": False,
    }
    icn["GR.M2.CROSS-COUNTRY TRUCK"] = [
        {"type": "path", "d": "M60,120 l80,0", "fill": False},
        {"type": "circle", "fill": False, "cx": 65, "cy": 125, "r": 5},
        {"type": "circle", "fill": False, "cx": 100, "cy": 125, "r": 5},
        {"type": "circle", "fill": False, "cx": 135, "cy": 125, "r": 5},
    ]
    icn["GR.M2.CAVALRY"] = {
        "type": "text",
        "stroke": False,
        "x": 110,
        "y": 140,
        "fontsize": 25,
        "text": "CAV",
    }
    icn["GR.M2.DECONTAMINATION"] = textm2("D")
    icn["GR.M2.DEMOLITION"] = textm2("DEM")
    if metadata.get("edition") == "E":
        icn["GR.M2.DENTAL"] = {
            "type": "path",
            "d": "m 108.8,142 c -0.1,0 -0.2,0 -0.2,0 0,0 0,0 0,0 -0.3,-0.1 -0.5,-0.3 -0.6,-0.6 0,-0.1 -0.2,-0.1 -0.2,-0.2 -0.5,-1.2 -0.8,-2.5 -1,-3.9 -0.1,-1.1 -0.1,-2.2 -0.2,-3.3 0,-1 -0.1,-2 -0.1,-3 0,-0.3 -0.1,-0.5 -0.2,-0.7 -0.1,-0.3 -0.2,-0.5 -0.3,-0.7 -0.4,-1 -0.8,-2 -0.9,-3.1 -0.1,-1 0,-2 0.5,-2.8 0.4,-0.7 0.9,-1.3 1.6,-1.6 0.3,-0.1 0.5,-0.2 0.8,-0.3 0.2,0 0.4,0 0.5,0 0.2,0 0.2,0 0.3,0 0.6,0.1 1.2,0.2 1.8,0.3 0.7,0.2 1.4,0.2 2.2,0.1 0.6,-0.1 1.2,-0.2 1.8,-0.3 0.4,-0.1 0.8,-0.1 1.3,0 0.6,0.1 1.1,0.4 1.6,0.9 0.8,0.8 1.1,1.9 1.2,3 0,0.6 -0.1,1.2 -0.2,1.7 -0.3,0.9 -0.6,1.7 -0.9,2.5 -0.2,0.4 -0.3,0.8 -0.3,1.3 0,0.6 -0.1,1.3 -0.1,2 0,0.9 -0.1,1.9 -0.2,2.9 0,0.5 -0.1,1 -0.1,1.4 -0.1,1 -0.4,2 -0.7,2.9 -0.1,0.4 -0.3,0.7 -0.5,1.1 -0.1,0.2 -0.3,0.4 -0.5,0.4 0,0 -0.1,0 -0.1,0 0,0 -0.1,0 -0.1,0 0,0 -0.1,0 -0.1,0 -0.3,-0.1 -0.4,-0.2 -0.5,-0.4 0,-0.2 0,-0.2 0,-0.3 -0.1,-0.7 -0.1,-1.3 -0.2,-2 -0.1,-1 -0.3,-2 -0.5,-2.9 -0.2,-0.7 -0.4,-1.3 -0.7,-1.8 -0.2,-0.4 -0.5,-0.7 -0.8,-0.9 -0.3,-0.2 -0.4,-0.2 -0.6,0 -0.3,0.1 -0.4,0.3 -0.6,0.6 -0.3,0.4 -0.6,0.9 -0.7,1.4 -0.5,1.5 -0.7,2.9 -0.8,4.4 0,0.4 -0.1,0.8 -0.1,1.2 0,0.4 -0.2,0.6 -0.6,0.7 z",
            "stroke": False,
        }
    else:
        icn["GR.M2.DENTAL"] = {
            "type": "text",
            "stroke": False,
            "textanchor": "middle",
            "alignmentBaseline": "middle",
            "x": 122,
            "y": 133,
            "fontsize": 18,
            "text": "D",
        }
    icn["GR.M2.DIGITAL"] = textm2("DIG")
    icn["GR.M2.ENHANCED POSITION LOCATION REPORTING SYSTEM"] = {
        "type": "path",
        "d": "m 87,142 13,-12 13,12 m -13,-20 0,20 0,0",
        "fill": False,
    }
    icn["GR.M2.EQUIPMENT"] = textm2("E")
    icn["GR.M2.EQUIMENT/TROOP"] = textm2("E/T")
    icn["GR.M2.HEAVY"] = textm2("H")
    icn["GR.M2.HIGH ALTITUDE"] = textm2("HA")
    icn["GR.M2.HIGH TO MEDIUM ALTITUDE"] = textm2("HMA")
    icn["GR.M2.HIGH TO LOW ALTITUDE"] = textm2("HLA")
    icn["GR.M2.JAMMING"] = {
        "Unknown": {
            "type": "path",
            "d": "M 40.019,126.84 C 40.121,124.78 40.776,123 45,123 c 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 9.16,0 1.54,8.38 7.87,9.8  m -91.625,4.1 c 0.734,-0.56 1.901,-0.9 3.755,-0.9 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 0.29,0 0.56,-0 0.81,-0",
            "fill": False,
        },
        "Friend": {
            "type": "path",
            "d": "m 25,123 c 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10  m -150,3 c 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10",
            "fill": False,
        },
        "Neutral": {
            "type": "path",
            "d": "m 45,123 v 0 c 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10  m -110,3 v 0 c 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10",
            "fill": False,
        },
        "Hostile": {
            "type": "path",
            "d": "M 59.401,131.4 C 61.215,128.57 57.535,123 65,123 c 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 1.55,0 2.62,0.24 3.36,0.65  m -74.484,22.3 c 0.343,0 0.717,0.1 1.124,0.1 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 5.66,0 4.91,3.21 5.01,5.99",
            "fill": False,
        },
    }.get(affiliation)
    icn["GR.M1.CYBERSPACE"] = textm1("CYB")
    icn["GR.M2.AIR ASSAULT"] = {
        "type": "path",
        "fill": False,
        "d": "m 85,125 15,20 15,-20",
    }
    icn["GR.M2.VERY HEAVY"] = textm2("VH")
    icn["GR.M2.CYBERSPACE"] = textm2("CYB")
    icn["GR.M2.NAVY BARGE, SELF-PROPELLED"] = textm2("YS")
    icn["GR.M2.NAVY BARGE, NOT SELF-PROPELLED"] = textm2("YB")
    icn["GR.M2.LAUNCH"] = textm2("YFT")
    icn["GR.M1.TACTICAL SATELLITE COMMUNICATIONS"] = [
        {
            "type": "path",
            "d": "m 105,65 10,0 m -30,0 10,0 M 85,77 c 10,-7 20,-7 30,0",
            "fill": False,
        },
        {
            "type": "path",
            "d": "m 75.4,60.9 0,9.1 13.1,0 0,-9.1 z m 36,0 0,9.1 13.1,0 0,-9.1 z m -18,0 0,9.1 13.1,0 0,-9.1 z",
            "stroke": False,
        },
    ]
    icn["GR.M2.INTERMODAL"] = {
        "type": "path",
        "d": "m 80,125 40,0 0,-4 8,9 -8,9 0,-4 -40,0 0,4 -8,-9 8,-9 z",
        "fill": False,
    }
    icn["GR.M2.INTENSIVE CARE"] = {
        "type": "text",
        "stroke": False,
        "textanchor": "middle",
        "alignmentBaseline": "middle",
        "x": 122,
        "y": 133,
        "fontsize": 18,
        "text": "IC",
    }
    icn["GR.M2.J1"] = textm2("J1")
    icn["GR.M2.J2"] = textm2("J2")
    icn["GR.M2.J3"] = textm2("J3")
    icn["GR.M2.J4"] = textm2("J4")
    icn["GR.M2.J5"] = textm2("J5")
    icn["GR.M2.J6"] = textm2("J6")
    icn["GR.M2.J7"] = textm2("J7")
    icn["GR.M2.J8"] = textm2("J8")
    icn["GR.M2.J9"] = textm2("J9")
    icn["GR.M2.LIGHT"] = textm2("L")
    icn["GR.M2.LABORATORY"] = textm2("LAB")
    icn["GR.M2.LAUNCHER"] = {
        "type": "path",
        "fill": False,
        "d": "M80,140 L115,120 120,140",
    }
    icn["GR.M2.LONG RANGE"] = textm2("LR")
    icn["GR.M2.LONG RANGE SURVEILLANCE"] = {
        "type": "text",
        "stroke": False,
        "x": 110,
        "y": 140,
        "fontsize": 25,
        "text": "LRS",
    }
    icn["GR.M2.LOW ALTITUDE"] = textm2("LA")
    icn["GR.M2.MEDIUM"] = textm2("M")
    icn["GR.M2.MEDIUM ALTITUDE"] = textm2("MA")
    icn["GR.M2.MEDIUM TO LOW ALTITUDE"] = textm2("MLA")
    icn["GR.M2.MEDIUM RANGE"] = textm2("MR")
    icn["GR.M2.MOUNTAIN"] = {
        "type": "path",
        "stroke": False,
        "d": "m 87,142 10,-20 5,10 3,-5 8,15",
    }
    icn["GR.M2.MULTIPLE ALTITUDES"] = textm2("H/MA")
    icn["GR.M2.MULTI-CHANNEL"] = textm2("MC")
    icn["GR.M2.OF-1"] = textm2("O-1/O-2") if not STD2525 else textm2("OF-1")
    icn["GR.M2.OF-2"] = textm2("O-3") if STD2525 else textm2("OF-2")
    icn["GR.M2.OF-3"] = textm2("O-4") if STD2525 else textm2("OF-3")
    icn["GR.M2.OF-4"] = textm2("O-5") if STD2525 else textm2("OF-4")
    icn["GR.M2.OF-5"] = textm2("O-6") if STD2525 else textm2("OF-5")
    icn["GR.M2.OF-6"] = textm2("O-7") if STD2525 else textm2("OF-6")
    icn["GR.M2.OF-7"] = textm2("O-8") if STD2525 else textm2("OF-7")
    icn["GR.M2.OF-8"] = textm2("O-9") if STD2525 else textm2("OF-8")
    icn["GR.M2.OF-9"] = textm2("O-10") if STD2525 else textm2("OF-9")
    icn["GR.M2.OF-10"] = textm2("O-11") if STD2525 else textm2("OF-10")
    icn["GR.M2.OF-D"] = textm2("OF-D")
    icn["GR.M2.OPTICAL"] = textm2("OPT")
    icn["GR.M2.OPTOMETRY"] = [
        {
            "type": "path",
            "d": "m 135,129 c -1.68,-1.82 -7.72,-7.76 -15.11,-7.83 h -0.15 c -7.32,0 -13.42,5.74 -15.12,7.52 -0.44,0.45 -0.45,1.18 0,1.65 1.67,1.82 7.72,7.76 15.11,7.84 h 0.15 c 7.32,0 13.42,-5.75 15.12,-7.52 0.44,-0.46 0.45,-1.19 0,-1.66 z  m -15.14,7.92 h -0.14 c -6.89,-0.1 -12.61,-5.71 -14.2,-7.36 1.62,-1.68 7.39,-7.14 14.22,-7.14 h 0.14 c 6.84,0.1 12.53,5.64 14.16,7.4 -1.65,1.72 -7.39,7.1 -14.18,7.1 z",
            "strokewidth": 2,
        },
        {
            "type": "path",
            "d": "m 123.71,130.25 a 3.908,3.908 0 0 1 -3.91,3.91 3.908,3.908 0 0 1 -3.91,-3.91 3.908,3.908 0 0 1 3.91,-3.91 3.908,3.908 0 0 1 3.91,3.91 z",
            "stroke": False,
        },
    ]
    icn["GR.M2.OR-1"] = textm2("E-1") if STD2525 else textm2("OR-1")
    icn["GR.M2.OR-2"] = textm2("E-2") if STD2525 else textm2("OR-2")
    icn["GR.M2.OR-3"] = textm2("E-3") if STD2525 else textm2("OR-3")
    icn["GR.M2.OR-4"] = textm2("E-4") if STD2525 else textm2("OR-4")
    icn["GR.M2.OR-5"] = textm2("E-5") if STD2525 else textm2("OR-5")
    icn["GR.M2.OR-6"] = textm2("E-6") if STD2525 else textm2("OR-6")
    icn["GR.M2.OR-7"] = textm2("E-7") if STD2525 else textm2("OR-7")
    icn["GR.M2.OR-8"] = textm2("E-8") if STD2525 else textm2("OR-8")
    icn["GR.M2.OR-9"] = textm2("E-9") if STD2525 else textm2("OR-9")
    icn["GR.M2.GUERILLA"] = textm2("G")
    icn["GR.M2.AMPHIBIOUS"] = {
        "Unknown": {
            "type": "path",
            "d": "M 64 144.9 C 80.4 143.9 63.1 125 81.4 125 C 100.2 125 81.4 145 100.2 145 C 119 145 100.2 125 119 125 C 137.1 125 120.2 143.6 135.9 144.9",
            "fill": False,
        },
        "Friend": {
            "type": "path",
            "d": "m 25,145 c 18.8,0 0,-20 18.8,-20 18.8,0 0,20 18.8,20 18.8,0 0,-20 18.8,-20 18.8,0 0,20 18.8,20 18.8,0 0,-20 18.8,-20 18.8,0 0,20 20,20",
            "fill": False,
        },
        "Neutral": {
            "type": "path",
            "d": "M 45 125 C 61.7 125.9 44.2 145 62.6 145 C 81.4 145 62.6 125 81.4 125 C 100.2 125 81.4 145 100.2 145 C 119 145 100.2 125 119 125 C 137.8 125 119 145 137.8 145 C 155.9 145 138.9 126.2 154.8 125 ",
            "fill": False,
        },
        "Hostile": {
            "type": "path",
            "d": "M 70.4 142.4 C 74.8 137 66.8 125 81.4 125 C 100.2 125 81.4 145 100.2 145 C 119 145 100.2 125 119 125 C 133.3 125 125.7 136.6 129.7 142.1 ",
            "fill": False,
        },
    }.get(affiliation)
    icn["GR.M2.PACK ANIMAL"] = {
        "type": "path",
        "d": "m 84,140 9,-15 7,15 7,-15 9,15",
        "fill": False,
    }
    icn["GR.M2.PATIENT EVACUATION COORDINATION"] = {
        "type": "text",
        "stroke": False,
        "x": 122,
        "y": 135,
        "fontsize": 16,
        "text": "PEC",
    }
    icn["GR.M2.PREVENTIVE MEDICIN"] = {
        "type": "path",
        "d": "m 116.6,121.74 -6.47,9.88 h 4.51 l 1.23,-4.5 2.93,6.75 0.9,-2.21 h 3.32 z  m -0.45,9.11 -0.56,2.04 h -6.27 l -3.54,5.4 h 21.44 l -3.4,-5.29 h -3.29 l -1.68,4.15 z",
        "stroke": False,
    }
    icn["GR.M2.PREVENTIVE MAINTENANCE"] = textm2("PM")
    icn["GR.M2.PSYCHOLOGICAL"] = {
        "type": "text",
        "textanchor": "middle",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 115,
        "y": 135,
        "fontsize": 28,
        "text": "P",
    }
    icn["GR.M2.RADIO RELAY LINE OF SIGHT"] = [
        {
            "type": "circle",
            "cx": 100,
            "cy": 132,
            "r": 11,
            "fill": False,
            "strokewidth": 3,
        },
        {
            "type": "path",
            "d": "M 90.8 128.2 C 90.3 129.3 90 130.6 90 132 C 90 133.4 90.3 134.7 90.8 135.8 L 100 132 L 90.8 128.2 z M 100 132 L 109.3 135.8 C 109.7 134.7 110 133.4 110 132 C 110 130.6 109.7 129.3 109.3 128.2 L 100 132 z",
        },
    ]
    icn["GR.M2.RAILROAD"] = [
        {"type": "path", "d": "M65,125 l70,0", "fill": False},
        {"type": "circle", "fill": False, "cx": 70, "cy": 130, "r": 5},
        {"type": "circle", "fill": False, "cx": 80, "cy": 130, "r": 5},
        {"type": "circle", "fill": False, "cx": 120, "cy": 130, "r": 5},
        {"type": "circle", "fill": False, "cx": 130, "cy": 130, "r": 5},
    ]
    icn["GR.M2.TRACTOR TRAILER"] = [
        {"type": "path", "d": "M60,120 l80,0", "fill": False},
        {"type": "circle", "fill": False, "cx": 65, "cy": 125, "r": 5},
        {"type": "circle", "fill": False, "cx": 75, "cy": 125, "r": 5},
        {"type": "circle", "fill": False, "cx": 135, "cy": 125, "r": 5},
    ]
    icn["GR.M2.RECOVERY (UNMANNED SYSTEMS)"] = {
        "type": "path",
        "d": "m 70,125 c0,20 60,20 60,0",
        "fill": False,
    }
    icn["GR.M2.RECOVERY (MAINTENANCE)"] = {
        "type": "path",
        "fill": False,
        "d": "M75,125 c8,0 8,16 0,16 m8,-8 l35,0 m8,-8 c-8,0 -8,16 0,16",
    }
    icn["GR.M2.REFUEL"] = textm2("K")
    icn["GR.M2.RESCUE COORDINATION CENTRE"] = {
        "type": "text",
        "stroke": False,
        "textanchor": "middle",
        "alignmentBaseline": "middle",
        "x": 122,
        "y": 132,
        "fontsize": 16,
        "text": "RCC",
    }
    icn["GR.M2.RIVERINE"] = {
        "type": "path",
        "d": "m 70.1,123 c 0,17 59.9,17 59.9,0 z",
        "fill": False,
    }
    icn["GR.M2.ROBOTIC"] = {
        "type": "path",
        "d": "M100,121.68L114.895,136.459C115.309,136.201 115.798,136.052 116.321,136.052C117.812,136.052 119.022,137.262 119.022,138.753C119.022,140.243 117.812,141.454 116.321,141.454C114.831,141.454 113.62,140.243 113.62,138.753C113.62,138.407 113.686,138.076 113.805,137.772L103.378,132.6L100.851,141.224C101.072,141.298 101.28,141.4 101.471,141.526C102.211,142.008 102.701,142.843 102.701,143.791C102.701,145.281 101.491,146.492 100,146.492C99.451,146.492 98.939,146.327 98.512,146.045C97.776,145.562 97.29,144.73 97.29,143.785C97.29,142.592 98.064,141.579 99.138,141.222L96.613,132.606L86.186,137.778C86.305,138.082 86.37,138.413 86.37,138.759C86.37,140.25 85.16,141.46 83.669,141.46C82.179,141.46 80.969,140.25 80.969,138.759C80.969,137.268 82.179,136.058 83.669,136.058C84.193,136.058 84.681,136.207 85.095,136.465L99.991,121.671L100,121.662L100,121.68Z",
        "stroke": False,
    }
    icn["GR.M2.SECURITY FORCE ASSISTANCE"] = textm2("SFA")
    icn["GR.M2.SINGLE CHANNEL"] = textm2("SC")
    icn["GR.M2.SKI"] = {
        "type": "path",
        "d": "m 95,145 -9,-8 m 28,0 -9,8 m -15,-24 20,20 m 0,-20 -20,20",
        "fill": False,
    }
    icn["GR.M2.SHORT RANGE"] = textm2("SR")
    icn["GR.M2.STRATEGIC"] = textm2("STR")
    icn["GR.M2.STRATEGIC MISSILE"] = textm2("S")
    icn["GR.M2.SUPPORT"] = textm2("SPT")
    icn["GR.M2.TACTICAL"] = textm2("TAC")
    icn["GR.M2.TACTICAL MISSILE"] = textm2("T")
    icn["GR.M2.TARGET ACQUISITION"] = textm2("TA")
    icn["GR.M2.TOWED"] = [
        {"type": "path", "d": "M82,130 l36,0", "fill": False},
        {"type": "circle", "fill": False, "cx": 75, "cy": 130, "r": 7},
        {"type": "circle", "fill": False, "cx": 125, "cy": 130, "r": 7},
    ]
    icn["GR.M2.TROOP"] = textm2("TR")
    icn["GR.M2.TRACKED"] = {
        "type": "path",
        "d": "m 90,125 h 20 c 10,0 10,15 0,15 H 90 c -10,0 -10,-15 0,-15",
        "fill": False,
    }
    icn["GR.M2.TRUCK"] = [
        {"type": "path", "d": "M60,120 l80,0", "fill": False},
        {"type": "circle", "fill": False, "cx": 65, "cy": 125, "r": 5},
        {"type": "circle", "fill": False, "cx": 135, "cy": 125, "r": 5},
    ]
    icn["GR.M2.UTILITY"] = textm2("U")
    icn["GR.M2.VIDEO IMAGERY"] = {
        "type": "path",
        "fill": False,
        "d": "m 120,126 h -11  m 11,10 h -14  m 4,-14 H 80 v 18 h 25 z  m 10,2 v 14",
    }
    icn["GR.M2.VERTICAL OR SHORT TAKE-OFF AND LANDING "] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 100,
        "y": 130,
        "fontsize": 20,
        "text": "VTOL",
    }
    icn["GR.M2.VETERINARY"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 115,
        "y": 137,
        "fontsize": 28,
        "text": "V",
    }
    icn["GR.M2.WHEELED"] = [
        {"type": "circle", "cx": 75, "cy": 130, "r": 7, "fill": False},
        {"type": "circle", "cx": 100, "cy": 130, "r": 7, "fill": False},
        {"type": "circle", "cx": 125, "cy": 130, "r": 7, "fill": False},
    ]
    icn["GR.M2.WHEELED LIMITED"] = [
        {"type": "circle", "cx": 80, "cy": 130, "r": 7, "fill": False},
        {"type": "circle", "cx": 120, "cy": 130, "r": 7, "fill": False},
    ]
    icn["GR.M2.WO-1"] = textm2("WO-1")
    icn["GR.M2.WO-2"] = textm2("WO-2")
    icn["GR.M2.WO-3"] = textm2("WO-3")
    icn["GR.M2.WO-4"] = textm2("WO-4")
    icn["GR.M2.WO-5"] = textm2("WO-5")
    # Ground Equipment --------------------------------------------------------------
    icn["GR.EQ.SHORT RANGE"] = {"type": "path", "d": "m 85,100 30,0", "fill": False}
    icn["GR.EQ.INTERMEDIATE RANGE"] = {
        "type": "path",
        "d": "m 85,105 30,0 m -30,-10 30,0",
        "fill": False,
    }
    icn["GR.EQ.LONG RANGE"] = {
        "type": "path",
        "d": "m 85,110 30,0 m -30,-20 30,0 m -30,10 30,0",
        "fill": False,
    }
    icn["GR.EQ.WEAPON"] = {"type": "path", "d": "m 100,60 0,80", "fill": False}
    icn["GR.EQ.RIFLE"] = {
        "type": "path",
        "d": "m 100,60 0,80 M 85,75 100,60 115,75",
        "fill": False,
    }
    icn["GR.EQ.RIFLE DISMOUNTED1"] = {
        "type": "path",
        "d": "m 90,90 10,-10 10,10 m -10,-10 0,40",
        "fill": False,
    }
    icn["GR.EQ.MACHINE GUN"] = {
        "type": "path",
        "d": "m 100,60 0,80 M 85,75 100,60 115,75 M 80,140 120,140",
        "fill": False,
    }
    icn["GR.EQ.GRENADE LAUNCHER"] = [
        icn["GR.EQ.RIFLE"],
        {"type": "circle", "cx": 100, "cy": 90, "r": 10, "fill": False},
    ]
    icn["GR.EQ.FLAME THROWER"] = {
        "type": "path",
        "fill": False,
        "d": "m 90,135 0,-70 c 0,-15 20,-15 20,0",
    }
    icn["GR.EQ.AIR DEFENCE GUN"] = [
        {
            "type": "path",
            "d": "m 85,140 30,0 c 0,-20 -30,-20 -30,0 z m 15,-80 0,65 m 15,-45 0,40 m -30,-40 0,40",
            "fill": False,
        }
    ]
    if not STD2525 and not numberSIDC:
        icn["GR.EQ.AIR DEFENCE GUN"].append(
            {"type": "path", "d": "M 85,75 100,60 115,75", "fill": False}
        )
    icn["GR.EQ.ANTITANK GUN"] = {
        "type": "path",
        "d": "m 85,140 15,-15 15,15 m -15,-80 0,65 m -15,-45 0,40 m 30,-40 0,40",
        "fill": False,
    }
    icn["GR.EQ.DIRECT FIRE GUN"] = {
        "type": "path",
        "d": "m 100,60 0,80 m 15,-60 0,40 m -30,-40 0,40",
        "fill": False,
    }
    icn["GR.EQ.RECOILLESS GUN"] = {
        "type": "path",
        "d": "m 85,75 15,-15 15,15 m 0,5 0,40 m -30,-40 0,40 m 15,-60 0,80",
        "fill": False,
    }
    icn["GR.EQ.HOWITZER"] = [
        {"type": "circle", "cx": 100, "cy": 130, "r": 10, "fill": False},
        {
            "type": "path",
            "d": "m 115,80 0,40 m -30,-40 0,40 m 15,-60 0,60",
            "fill": False,
        },
    ]
    icn["GR.EQ.HOWITZER TRACKED"] = {
        "type": "path",
        "d": "M 70,120 l 60,0 c10,0 10,10 0,10 l -60,0 c-10,0 -10,-10 0,-10",
        "fill": False,
    }
    icn["GR.EQ.MISSILE LAUNCHER"] = {
        "type": "path",
        "d": "m 100,140 0,-80 m -15,80 0,-65 c 0,-20 30,-20 30,0 l 0,65",
        "fill": False,
    }
    icn["GR.EQ.AIR DEFENCE MISSILE LAUNCHER SURFACE-TO-AIR"] = {
        "type": "path",
        "d": "m 85,140 30,0 c 0,-20 -30,-20 -30,0 z m 15,-15 0,-65 m -15,80 0,-65 c 0,-20 30,-20 30,0 l 0,65",
        "fill": False,
    }
    icn["GR.EQ.AIR DEFENCE MISSILE LAUNCHER SURFACE-TO-AIR TLAR"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 132,
        "y": 100,
        "fontsize": 25,
        "text": "R",
    }
    icn["GR.EQ.AIR DEFENCE MISSILE LAUNCHER SURFACE-TO-AIR TELAR"] = [
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 68,
            "y": 100,
            "fontsize": 25,
            "text": "E",
        },
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 132,
            "y": 100,
            "fontsize": 25,
            "text": "R",
        },
    ]

    icn["GR.EQ.AIR DEFENCE MISSILE LAUNCHER SURFACE-TO-AIR THEATRE"] = {
        "type": "text",
        "stroke": False,
        "x": 100,
        "y": 145,
        "fontsize": 30,
        "text": "T",
    }
    icn["GR.EQ.ANTITANK MISSILE LAUNCHER"] = {
        "type": "path",
        "d": "m 85,140 15,-15 15,15 M 85,120 85,75 c 0,-20 30,-20 30,0 l 0,45 m -15,5 0,-65",
        "fill": False,
    }
    icn["GR.EQ.SURFACE-TO-SURFACE MISSILE LAUNCHER"] = [icn["GR.EQ.MISSILE LAUNCHER"]]
    icn["GR.EQ.SURFACE-TO-SURFACE MISSILE LAUNCHER"].append(
        {"type": "path", "d": "m 85,140 30,0", "fill": False}
    )
    icn["GR.EQ.MORTAR"] = [
        {"type": "path", "d": "m 100,60 0,60 M 85,75 100,60 115,75", "fill": False},
        {"type": "circle", "cx": 100, "cy": 130, "r": 10, "fill": False},
    ]
    icn["GR.EQ.SINGLE ROCKET LAUNCHER"] = {
        "type": "path",
        "d": "m 85,75 15,-15 15,15 m -15,-5 0,70 M 85,85 100,70 115,85",
        "fill": False,
    }
    icn["GR.EQ.MULTIPLE ROCKET LAUNCHER"] = {
        "type": "path",
        "d": "m 115,90 0,40 m -30,-40 0,40 m 0,-55 15,-15 15,15 m -15,-5 0,70 M 85,85 100,70 115,85",
        "fill": False,
    }
    icn["GR.EQ.ANTITANK ROCKET LAUNCHER"] = {
        "type": "path",
        "d": "m 85,140 15,-15 15,15 M 85,85 100,70 115,85 m -15,-15 0,55 M 85,75 100,60 115,75",
        "fill": False,
    }
    icn["GR.EQ.NON-LETHAL WEAPON"] = {
        "type": "path",
        "d": "m 100,60 0,80 M 80,60 l40,0",
        "fill": False,
    }
    icn["GR.EQ.NON-LETHAL GRENADE LAUNCHER"] = [
        icn["GR.EQ.NON-LETHAL WEAPON"],
        {"type": "circle", "cx": 100, "cy": 90, "r": 15, "fill": False},
    ]
    icn["GR.EQ.TASER"] = [icn["GR.EQ.NON-LETHAL WEAPON"], text("Z")]
    icn["GR.EQ.WATER CANNON"] = [icn["GR.EQ.NON-LETHAL WEAPON"], text("W")]
    icn["GR.EQ.LIMITED CROSS-COUNTRY"] = [
        {"type": "path", "d": "m 70,130 60,0", "fill": False},
        {"type": "circle", "cx": 75, "cy": 135, "r": 5, "fill": False},
        {"type": "circle", "cx": 125, "cy": 135, "r": 5, "fill": False},
    ]
    icn["GR.EQ.CROSS-COUNTRY"] = [
        {"type": "path", "d": "m 70,130 60,0", "fill": False},
        {"type": "circle", "cx": 75, "cy": 135, "r": 5, "fill": False},
        {"type": "circle", "cx": 100, "cy": 135, "r": 5, "fill": False},
        {"type": "circle", "cx": 125, "cy": 135, "r": 5, "fill": False},
    ]
    icn["GR.EQ.ARMOURED FIGHTING VEHICLE"] = {
        "type": "path",
        "d": "m 70,100 30,-30 30,30 -30,30 z m 60,-30 0,60 m -60,-60 0,60 0,0",
        "fill": False,
    }
    icn["GR.EQ.ARMOURED FIGHTING VEHICLE (AFV) COMMAND AND CONTROL"] = [
        icn["GR.EQ.ARMOURED FIGHTING VEHICLE"]
    ]
    if numberSIDC:
        icn["GR.EQ.ARMOURED FIGHTING VEHICLE (AFV) COMMAND AND CONTROL"].append(
            {
                "type": "text",
                "alignmentBaseline": "middle",
                "stroke": False,
                "x": 100,
                "y": 103,
                "fontsize": 30,
                "text": "C2",
            }
        )
    else:
        icn["GR.EQ.ARMOURED FIGHTING VEHICLE (AFV) COMMAND AND CONTROL"].append(
            {"type": "path", "d": "m 80,90 20,15 0,-10 20,15", "fill": False}
        )
    icn["GR.EQ.ARMOURED PERSONNEL CARRIER"] = {
        "type": "path",
        "fill": False,
        "d": "m 70,80 30,-10 30,10 m -60,-10 0,60 60,0 0,-60",
    }
    icn["GR.EQ.ARMOURED PERSONNEL CARRIER COMBAT SERVICE SUPPORT VEHICLE"] = [
        icn["GR.EQ.ARMOURED PERSONNEL CARRIER"],
        {"type": "path", "d": "m 70,120 60,0", "fill": False},
    ]
    icn["GR.EQ.ARMOURED PERSONNEL CARRIER ENGINEER RECON VEHICLE"] = {
        "type": "path",
        "fill": False,
        "d": "M 130,80 70,130",
    }
    icn["GR.EQ.COMBAT SERVICE SUPPORT VEHICLE"] = {
        "type": "path",
        "fill": False,
        "d": "M 70,120 130,120",
    }
    icn["GR.EQ.DESIGNATED MARKSMAN"] = text("DM")
    icn["GR.EQ.ARMOURED MEDICAL PERSONNEL CARRIER"] = {
        "type": "path",
        "fill": False,
        "d": "m 70,100 60,0 m -30,-30 0,60",
    }
    icn["GR.EQ.ARMOURED PROTECTED VEHICLE WITH LIMITED CROSS COUNTRY MOBILITY"] = [
        {
            "type": "path",
            "d": "m 60,120 80,0 M 120,80 c 25,0.2 25,40 0,40 l -40,0 C 55,120 55,80 80,80 Z",
            "fill": False,
        },
        icn["GR.M2.WHEELED LIMITED"],
    ]
    icn["GR.EQ.ARMOURED VEHICLE"] = text("A")
    icn["GR.EQ.CLOSE PROTECTION"] = text("CLP")
    icn["GR.EQ.CROWD AND RIOT CONTROL"] = text("CRC")
    icn["GR.EQ.SPECIAL WEAPONS AND TACTICS (SWAT)"] = text("SWAT")
    icn["GR.EQ.DEMOLITION"] = text("DEM")
    icn["GR.EQ.COMMANDER (CDR)"] = text("CDR")
    icn["GR.EQ.SECOND IN COMMAND (SIC)"] = text("SIC")
    icn["GR.EQ.ARMORED CARRIER WITH VOLCANO"] = text("V")
    icn["GR.EQ.TANK"] = {
        "type": "path",
        "fill": False,
        "d": "m 70,80 60,0 m -60,40 60,0 m -60,-50 0,60 0,0 m 60,-60 0,60",
    }
    icn["GR.EQ.ASSAULT BREACHER VEHICLE (ABV) WITH COMBAT DOZER BLADE"] = {
        "type": "path",
        "fill": False,
        "d": "m 100,95 30,25 m -30,-60 0,35 -30,25 m 10,-60 40,0 m -50,20 60,0 m -60,40 60,0 m -60,-50 0,60 0,0 m 60,-60 0,60",
    }
    icn["GR.EQ.LIGHT TANK"] = {"type": "path", "fill": False, "d": "m 100,80 0,40"}
    icn["GR.EQ.MEDIC"] = {
        "type": "path",
        "d": "M93,83 l14,0 0,10 10,0 0,14 -10,0 0,10 -14,0 0,-10 -10,0 0,-14 10,0 Z",
    }
    icn["GR.EQ.MEDIUM TANK"] = {
        "type": "path",
        "fill": False,
        "d": "m 105,80 0,40 m -10,-40 0,40",
    }
    icn["GR.EQ.HEAVY TANK"] = {
        "type": "path",
        "fill": False,
        "d": "m 110,80 0,40 m -20,-40 0,40 m 10,-40 0,40",
    }
    icn["GR.EQ.TANK RECOVERY VEHICLE"] = {
        "type": "path",
        "fill": False,
        "d": "m 85,100 30,0 m 10,-10 c -13.1,0 -12.4,20 0,20 M 75,90 c 12.7,0.3 12.7,20.3 0,20",
    }
    icn["GR.EQ.BRIDGE"] = {
        "type": "path",
        "d": "m 115,75 -10,10 0,30 10,10 m -30,-50 10,10 0,30 -10,10 m -15,-55 60,0 0,60 -60,0 0,-60",
        "fill": False,
    }
    icn["GR.EQ.FIXED BRIDGE"] = {"type": "path", "d": "M 100,70 100,130", "fill": False}
    icn["GR.EQ.FOLDING GIRDER BRIDGE"] = {
        "type": "path",
        "d": "M 110, 80 90,80 90,120 110,120",
        "fill": False,
    }
    icn["GR.EQ.HOLLOW DECK BRIDGE"] = {
        "type": "path",
        "d": "M 110, 80 90,80 90,120 110,120 z",
        "fill": False,
    }
    icn["GR.EQ.DRILL"] = icn["GR.IC.DRILLING"]
    icn["GR.EQ.DOZER"] = {
        "type": "path",
        "d": "m 90,60 20,0 m -10,0 0,20 m -30,0 60,0 m -60,-10 0,60 0,0 m 60,-60 0,60 m -60,-10 60,0",
        "fill": False,
    }
    icn["GR.EQ.DOZER ARMORED"] = {
        "type": "path",
        "d": "m 70,130 60,0 m -30,-70 0,10 m -30,10 30,-10 30,10 m 0,-10 0,60 m -60,-60 0,60 0,0 m 20,-70 20,0",
        "fill": False,
    }
    icn["GR.EQ.EARTHMOVER"] = {
        "type": "path",
        "d": "m 100,60 0,20 m -25,-15 5,-5 40,0 5,5 m -55,15 60,0 m -60,40 60,0 m 0,-50 0,60 m -60,-60 0,60 0,0",
        "fill": False,
    }
    icn["GR.EQ.MULTIFUNCTIONAL EARTHMOVER/DIGGER"] = [
        icn["GR.EQ.EARTHMOVER"],
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 100,
            "fontsize": 30,
            "text": "MF",
        },
    ]
    icn["GR.EQ.MINE CLEARING EQUIPMENT"] = {
        "type": "path",
        "d": "m 100,80 0,15 -30,25 60,0 -30,-25",
        "fill": False,
    }
    icn["GR.EQ.MINE LAYING VEHICLE"] = [
        {
            "type": "path",
            "d": "m 90,85 20,30 m 0,-30 -20,30 m 10,-30 0,30",
            "fill": False,
        },
        {"type": "circle", "cx": 100, "cy": 100, "r": 10},
    ]
    icn["GR.EQ.MINE SCATTERABLE"] = [
        text("S"),
        {"type": "circle", "cx": 85, "cy": 115, "r": 5, "fill": False},
        {"type": "circle", "cx": 100, "cy": 115, "r": 5, "fill": False},
        {"type": "circle", "cx": 115, "cy": 115, "r": 5, "fill": False},
    ]
    icn["GR.EQ.UTILITY VEHICLE"] = {
        "type": "path",
        "fill": False,
        "d": "m 70,65 c 0,15 60,15 60,0 l 0,65 -60,0 z",
    }
    icn["GR.EQ.UTILITY VEHICLE BACKHOE"] = [
        {"type": "path", "fill": False, "d": "M 130,130 100,80 75,95 75,95"},
        {"type": "path", "d": "M 75,105 85,95 75,95 z"},
    ]
    icn["GR.EQ.UTILITY VEHICLE FERRY TRANSPORTER"] = {
        "type": "path",
        "fill": False,
        "d": "m 75,100 c 15,15 35,15 50,0 z",
    }
    icn["GR.EQ.UTILITY VEHICLE LIGHT"] = {
        "type": "path",
        "fill": False,
        "d": "M 100,78.3 100,130",
    }
    icn["GR.EQ.UTILITY VEHICLE MEDIUM"] = {
        "type": "path",
        "fill": False,
        "d": "m 105,130 0,-52 M 95,130 l0,-52",
    }
    icn["GR.EQ.UTILITY VEHICLE HEAVY"] = {
        "type": "path",
        "fill": False,
        "d": "m 110,130 0,-53 m -20,50 0,-53 m 10,1.3 0,52",
    }
    icn["GR.EQ.UTILITY VEHICLE.TOW TRUCK"] = {
        "type": "path",
        "fill": False,
        "d": "m 130,130 -40,-40 0,25 c 0,5 -10,5 -10,0",
    }
    icn["GR.EQ.UTILITY VEHICLE.TOW TRUCK.LIGHT"] = {
        "type": "path",
        "fill": False,
        "d": "m 105,115 10,-10",
    }
    icn["GR.EQ.UTILITY VEHICLE.TOW TRUCK.HEAVY"] = {
        "type": "path",
        "fill": False,
        "d": "m 120,110 -10,10 m -10,-10 10,-10 m -5,15 10,-10",
    }
    icn["GR.EQ.MEDICAL VEHICLE"] = {
        "type": "path",
        "fill": False,
        "d": "m 70,100 l 60,0 M 100,78.3 100,130",
    }
    icn["GR.EQ.MEDICAL EVACUATION"] = {
        "type": "path",
        "d": "m 95,85 10,0 0,10 10,0 0,10 -10,0 0,10 -10,0 0,-10 -10,0 0,-10 10,0 z",
    }
    icn["GR.EQ.MOBILE EMERGENCY PHYSICIAN"] = {
        "type": "path",
        "fill": False,
        "d": "m 70,100 l 60,0 M 100,78.3 100,130 M 85,85 115,85",
    }
    icn["GR.EQ.BUS"] = [icn["GR.EQ.UTILITY VEHICLE"], text("B")]
    icn["GR.EQ.SEMI-TRAILER TRUCK"] = [
        icn["GR.EQ.UTILITY VEHICLE"],
        {"type": "path", "fill": False, "d": "m 140,90 0,20 m -10,-10 10,0"},
        {"type": "circle", "cx": 75, "cy": 135, "r": 5, "fill": False},
        {"type": "circle", "cx": 85, "cy": 135, "r": 5, "fill": False},
        {"type": "circle", "cx": 125, "cy": 135, "r": 5, "fill": False},
    ]
    icn["GR.EQ.WATER VEHICLE"] = [
        icn["GR.EQ.UTILITY VEHICLE"],
        {
            "type": "path",
            "fill": False,
            "d": "m 70,95 c 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10 10,0 0,10 10,10 10,0 0,-10 10,-10",
        },
        {"type": "circle", "cx": 75, "cy": 135, "r": 5, "fill": False},
        {"type": "circle", "cx": 125, "cy": 135, "r": 5, "fill": False},
    ]
    icn["GR.EQ.TRAIN LOCOMOTIVE"] = {
        "type": "path",
        "fill": False,
        "d": "m 70,70 0,60 60,0 0,-30 -30,0 0,-30 z",
    }
    icn["GR.EQ.RAILCAR"] = [
        icn["GR.EQ.UTILITY VEHICLE"],
        {"type": "circle", "fill": False, "cx": 75, "cy": 135, "r": 5},
        {"type": "circle", "fill": False, "cx": 85, "cy": 135, "r": 5},
        {"type": "circle", "fill": False, "cx": 115, "cy": 135, "r": 5},
        {"type": "circle", "fill": False, "cx": 125, "cy": 135, "r": 5},
    ]
    icn["GR.EQ.CBRN EQUIPMENT"] = [
        {
            "type": "path",
            "d": "M80,140 c0,-20 10,-60 50,-63 m-10,63 c0,-20 -10,-60 -50,-63 ",
            "fill": False,
        },
        {"type": "circle", "cx": 70, "cy": 85, "r": 8},
        {"type": "circle", "cx": 130, "cy": 85, "r": 8},
    ]
    icn["GR.EQ.COMPUTER SYSTEM"] = {
        "type": "path",
        "d": "m 100,132 0,-10 -35,0 0,-50 70,0 0,50 -35,0 m -25,10 50,0",
        "fill": False,
    }
    icn["GR.EQ.COMMAND LAUNCH EQUIPMENT (CLE)"] = text("CLE")
    icn["GR.EQ.GENERATOR SET"] = text("G")
    icn["GR.EQ.GROUND-BASED MIDCOURSE DEFENSE (GMD) FIRE CONTROL (GFC) CENTER"] = text(
        "GFC"
    )
    icn[
        "GR.EQ.IN-FLIGHT INTERCEPTOR COMMUNICATIONS SYSTEM (IFICS) DATA TERMINAL (IDT)"
    ] = {
        "type": "path",
        "fill": False,
        "d": "m 80,82.4 45,-2 -4,37 m -6,-1 0,-35 -34,9 m 12,21 0,8 M 80,82.4 c 0,25 16,35 41,35",
    }
    icn["GR.EQ.LASER"] = {
        "type": "path",
        "fill": False,
        "d": "m 100,55 0,25 10,5 -20,5 20,5 -20,5 10,5 0,15 10,5 -20,5 20,5 -20,5 20,5 M 90,65 100,55 110,65",
    }
    icn["GR.EQ.TENT"] = {
        "type": "path",
        "fill": False,
        "d": "m 65,124.4 10,-37 25,-10 25,10 10,37 z",
    }
    icn["GR.EQ.TENT CIVILIAN"] = {
        "type": "path",
        "fill": False,
        "d": "m 75,120 10,-30 15,-10 15,10 10,30 z",
    }
    icn["GR.EQ.TENT MILITARY"] = {
        "type": "path",
        "d": "m 75,120 10,-30 15,-10 15,10 10,30 z",
    }
    icn["GR.EQ.UNIT DEPLOYMENT SHIPMENTS"] = text("DPLY")
    icn["GR.EQ.CIVILIAN VEHICLE.LIGHT"] = {
        "type": "path",
        "fill": False,
        "d": "m 100,125 0,-20",
    }
    icn["GR.EQ.CIVILIAN VEHICLE.MEDIUM"] = {
        "type": "path",
        "fill": False,
        "d": "m 103,105 0,20 m -6,-20 0,20",
    }
    icn["GR.EQ.CIVILIAN VEHICLE.HEAVY"] = {
        "type": "path",
        "fill": False,
        "d": "m 106,105 0,20 m -12,-20 0,20 m 6,-20 0,20",
    }
    icn["GR.EQ.CIVILIAN VEHICLE.TRAILER"] = {
        "type": "path",
        "fill": False,
        "d": "m 140,105 0,20 m -10,-10 10,0",
    }
    icn["GR.EQ.CIVILIAN VEHICLE.AUTOMOBILE"] = [
        {
            "type": "path",
            "fill": iconFillColor if STD2525 else False,
            "d": "m 90,125 20,0 m -20,0 c 0,-4.1 -3.4,-7.5 -7.5,-7.5 -4.1,0 -7.5,3.4 -7.5,7.5 0,4.1 3.4,7.5 7.5,7.5 4.1,0 7.5,-3.4 7.5,-7.5 z m 35,0 5,0 0,-20 -20,0 0,-20 -20,0 0,20 -20,0 0,20 5,0 m 50,0 c 0,-4.1 -3.4,-7.5 -7.5,-7.5 -4.1,0 -7.5,3.4 -7.5,7.5 0,4.1 3.4,7.5 7.5,7.5 4.1,0 7.5,-3.4 7.5,-7.5 z",
        },
        {
            "type": "path",
            "fill": False,
            "strokewidth": 2,
            "d": "m 95,90 0,15 10,0 0,-15 z",
        },
    ]
    icn["GR.EQ.CIVILIAN VEHICLE.OPEN-BED TRUCK"] = [
        {
            "type": "path",
            "fill": iconFillColor if STD2525 else False,
            "d": "m 90,125 20,0 m -20,0 c 0,-4.1 -3.4,-7.5 -7.5,-7.5 -4.1,0 -7.5,3.4 -7.5,7.5 0,4.1 3.4,7.5 7.5,7.5 4.1,0 7.5,-3.4 7.5,-7.5 z m 35,0 c 0,-4.1 -3.4,-7.5 -7.5,-7.5 -4.1,0 -7.5,3.4 -7.5,7.5 0,4.1 3.4,7.5 7.5,7.5 4.1,0 7.5,-3.4 7.5,-7.5 z m 0,0 5,0 0,-20 -20,0 -20,0 0,-20 -20,0 0,20 0,20 5,0",
        },
        {
            "type": "path",
            "fill": False,
            "strokewidth": 2,
            "d": "m 75,90 0,15 10,0 0,-15 z",
        },
    ]
    icn["GR.EQ.CIVILIAN VEHICLE.MULTIPLE PASSENGER VEHICLE"] = [
        {
            "type": "path",
            "fill": iconFillColor if STD2525 else False,
            "d": "m 90,125 20,0 m -20,0 c 0,-4.1 -3.4,-7.5 -7.5,-7.5 -4.1,0 -7.5,3.4 -7.5,7.5 0,4.1 3.4,7.5 7.5,7.5 4.1,0 7.5,-3.4 7.5,-7.5 z m 35,0 c 0,-4.1 -3.4,-7.5 -7.5,-7.5 -4.1,0 -7.5,3.4 -7.5,7.5 0,4.1 3.4,7.5 7.5,7.5 4.1,0 7.5,-3.4 7.5,-7.5 z m 0,0 5,0 0,-20 0,-20 -20,0 -20,0 -20,0 0,20 0,20 5,0",
        },
        {
            "type": "path",
            "fill": False,
            "strokewidth": 2,
            "d": "m 115,90 0,15 10,0 0,-15 z m -20,0 0,15 10,0 0,-15 z m -20,0 0,15 10,0 0,-15 z",
        },
    ]
    icn["GR.EQ.CIVILIAN VEHICLE.UTILITY VEHICLE"] = [
        {
            "type": "path",
            "fill": iconFillColor if STD2525 else False,
            "d": "m 90,125 c 0,-4.1 -3.4,-7.5 -7.5,-7.5 -4.1,0 -7.5,3.4 -7.5,7.5 0,4.1 3.4,7.5 7.5,7.5 4.1,0 7.5,-3.4 7.5,-7.5 z m 35,0 c 0,-4.1 -3.4,-7.5 -7.5,-7.5 -4.1,0 -7.5,3.4 -7.5,7.5 0,4.1 3.4,7.5 7.5,7.5 4.1,0 7.5,-3.4 7.5,-7.5 z m -35,0 20,0 m 15,0 5,0 0,-20 0,-20 -20,0 -20,0 0,20 -20,0 0,20 5,0",
        },
        {
            "type": "path",
            "fill": False,
            "strokewidth": 2,
            "d": "m 95,90 0,15 10,0 0,-15 z",
        },
    ]
    icn["GR.EQ.CIVILIAN VEHICLE.JEEP TYPE VEHICLE"] = {
        "type": "path",
        "fill": iconFillColor if STD2525 else False,
        "d": "m 90,125 20,0 m -20,0 c 0,-4.1 -3.4,-7.5 -7.5,-7.5 -4.1,0 -7.5,3.4 -7.5,7.5 0,4.1 3.4,7.5 7.5,7.5 4.1,0 7.5,-3.4 7.5,-7.5 z m 35,0 c 0,-4.1 -3.4,-7.5 -7.5,-7.5 -4.1,0 -7.5,3.4 -7.5,7.5 0,4.1 3.4,7.5 7.5,7.5 4.1,0 7.5,-3.4 7.5,-7.5 z m 0,0 5,0 0,-20 -60,0 0,20 5,0 m 15,-20 5,-15",
    }
    icn["GR.EQ.PACK ANIMAL"] = {
        "type": "path",
        "fill": False,
        "d": "m 70,125 15,-50 15,50 15,-50 15,50 ",
    }
    icn["GR.EQ.MISSILE SUPPORT"] = [
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 93,
            "fontsize": 20,
            "text": "MSL",
        },
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 110,
            "fontsize": 20,
            "text": "SPT",
        },
    ]
    icn["GR.EQ.MISSILE TRANSLOADER"] = [
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 100,
            "fontsize": 30,
            "text": "MSL",
        },
        {
            "type": "path",
            "fill": False,
            "d": "m 75,70 50,0 m -25,10 c 0,-5 0,-10 0,-10",
        },
    ]
    icn["GR.EQ.MISSILE TRANSPORTER"] = [
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 100,
            "fontsize": 30,
            "text": "MSL",
        }
        # { 'type': a"path", 'fill': False, d: "m 55,85 90,0" }
    ]
    icn["GR.EQ.MISSILE CRANE/LOADING DEVICE"] = [
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 100,
            "fontsize": 30,
            "text": "MSL",
        },
        {
            "type": "path",
            "fill": False,
            "d": "m 75,80 25,-20 c 0,0 0,15 0,15 l 5,0 0,-5",
        },
    ]
    icn["GR.EQ.MISSILE PROPELLANT TRANSPORTER"] = [
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 90,
            "y": 100,
            "fontsize": 20,
            "text": "MSL",
        },
        {"type": "path", "fill": False, "d": "m 120,115 0,-15 -10,-10 20,0 -10,10"},
    ]
    icn["GR.EQ.MISSILE WARHEAD TRANSPORTER"] = [
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 93,
            "fontsize": 20,
            "text": "MSL",
        },
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 110,
            "fontsize": 20,
            "text": "WHD",
        },
    ]
    icn["GR.EQ.LAND MINE"] = (
        {"type": "circle", "cx": 100, "cy": 100, "r": 22, "fill": False}
        if numberSIDC
        else [
            {"type": "path", "fill": False, "d": "m 70,65 60,0 -30,65 z"},
            {
                "type": "text",
                "stroke": False,
                "x": 100,
                "y": 90,
                "fontfamily": "Arial",
                "fontsize": 30,
                "text": "M",
            },
        ]
    )
    icn["GR.EQ.ANTIPERSONNEL LAND MINE"] = [
        {"type": "circle", "cx": 100, "cy": 100, "r": 22},
        {
            "type": "path",
            "d": "M117,82 l20,-18 -18,25z M83,82 l-20,-18 18,25z",
            "stroke": False,
        },
    ]
    icn["GR.EQ.ANTIPERSONNEL LAND MINE LESS THAN LETHAL"] = [
        {"type": "circle", "cx": 100, "cy": 100, "r": 22, "fill": False},
        {
            "type": "path",
            "d": "M117,82 l20,-18 -18,25z M83,82 l-20,-18 18,25z",
            "stroke": False,
        },
    ]
    icn["GR.EQ.ANTITANK MINE"] = {"type": "circle", "cx": 100, "cy": 100, "r": 22}
    icn["GR.EQ.IMPROVISED EXPLOSIVE DEVICE"] = text("IED")
    icn["GR.EQ.LAND MINES"] = [
        {
            "type": "text",
            "stroke": False,
            "x": 100,
            "y": 110,
            "fontsize": 30,
            "text": "M",
        },
        {
            "type": "path",
            "fill": False,
            "d": "m 135,70 -70,0 35,70 z" if STD2525 else "m 65,130 70,0 -35,-70 z",
        },
    ]
    icn["GR.EQ.SENSOR"] = {
        "type": "path",
        "d": "m 100,60 c 0,15 25,40 40,40 -15,0 -40,25 -40,40 0,-15 -25,-40 -40,-40 15,0 40,-25 40,-40 z",
    }
    icn["GR.EQ.SENSOR EMPLACED"] = [
        ms._scale(0.75, icn["GR.EQ.SENSOR"], True),
        {
            "type": "path",
            "fill": False,
            "d": "m 70,75 10,-15 10,15 10,-15 10,15 10,-15 10,15",
        },
    ]
    icn["GR.EQ.RADAR"] = {
        "type": "path",
        "d": "M72,95 l30,-25 0,25 30,-25 M70,70 c0,35 15,50 50,50",
        "fill": False,
    }
    icn["GR.EQ.ANTENNAE"] = []
    icn["GR.EQ.PSYCHOLOGICAL OPERATIONS EQUIPMENT"] = {
        "type": "path",
        "fill": iconFillColor if STD2525 else False,
        "stroke": "black",  # TODO: Verify if variable exists or use string
        "d": "m 110,95 10,0 m -10,10 10,0 m -10,10 10,0 m -10,-30 10,0 m -10,-5 -10,10 -30,0 0,20 30,0 10,10 z",
    }
    # Installation
    icn["GR.IN.IC.ELDER CARE"] = {
        "type": "path",
        "d": "m 120.1,119.1 c 0,-6.3 2.3,-8.2 3.9,-12.6 1,-2.6 1.6,-3.3 1.8,-6.5 0.2,-2.4 0.9,-4.7 0.9,-7.2 v -2.6 c 0,-2.6 -2.2,-8.9 -3.3,-10.5 -1.3,-2 -4.8,-5.4 -6.7,-6.9 -2.2,-1.8 -5.4,-4.6 -8.2,-5.6 -1.6,-0.5 -9.8,-2.4 -11.4,-2.3 l -5.7,0.6 v 0.8 c 0,0.8 2,2.7 2.4,3.3 0,3.3 0.8,6.8 -1.3,8.4 -2.2,1.6 -2.8,3.4 -3.8,6.3 -0.4,1 -0.9,3.1 -1,4 -0.2,1 -0.2,4 -0.4,4.6 -1.1,2.4 -2.6,4.2 -3.8,6.4 l -5.1,0.5 c -2.1,3.2 -4.6,4.1 -4.6,9.6 v 26.4 c 0.6,0.2 0.4,0.2 0.9,0.2 0.5,0 0.3,-0.1 0.9,-0.2 v -27.5 c 0,-0.7 0.8,-3 1.1,-3.5 0.4,0.2 0.8,0.6 1.3,0.6 0.3,0 1.1,-0.3 1.3,-0.4 l 2.6,0.9 0.8,-0.6 0.6,2.5 c 0.4,0.3 0.4,0.5 0.8,0.5 h 0.4 c 0.5,0 0.6,-0.2 0.6,-0.6 v -0.4 c 0,-1 -1.2,-3 -1.5,-3.7 1.2,-2.5 6.3,-2.6 8.2,-5.8 0.9,-1.6 1.8,-3 2.6,-4.5 0.4,-0.9 2.3,-4.1 2.4,-4.4 h 4.4 c 2.3,0 2.1,2.5 2.6,4.2 0.6,2 2,2 2,4.6 0,2.8 -2.9,7 -4,9 -0.3,0.7 -3.9,8.8 -3.9,8.9 v 2 c 0,3 2.6,9.1 2.6,11.2 v 2.2 c -1.2,0.3 -6.8,2.4 -6.8,3.5 0,0.3 0.4,0.6 0.9,0.6 h 6.8 c 2.3,0 4.5,-1 6.6,-1.1 v -3 c 0,-0.6 -1.1,-2.2 -1.1,-3.7 -0.9,-1.3 -1.8,-6 -1.8,-8.2 0,-3.2 1.2,-5.4 2.5,-7.4 2.5,-4 0.4,-2.3 4.6,-5.1 l 1.8,1.7 c -1,1.8 -2.3,3.7 -2.3,6.4 v 5.9 h 0.4 v 0.6 c 0,0.9 5,9 5.7,10.3 -1.5,2.3 -6.7,1.6 -6.8,5 h 7.5 c 1.2,0 3.3,-1 4.5,-1.4 1.6,-0.5 2.9,-1.1 2.9,-3 0,-0.7 -2.9,-4.6 -3.6,-5.7 -0.3,-0.4 -2.4,-6 -2.4,-6.6 v -0.4 z m -45.3,-47.9 v 0.6 c 0,4.3 3.7,7.9 8.1,7.9 h 0.2 c 3.7,0 7.7,-3.6 7.7,-7 v -2.2 c 0,-3.2 -3.9,-6.8 -7.5,-6.8 h -1.2 c -3.4,0 -7.3,4 -7.3,7.5 z",
        "stroke": False,
    }
    icn["GR.IN.IC.RAW MATERIAL PRODUCTION/STORAGE"] = [
        {
            "type": "text",
            "stroke": False,
            "x": 100,
            "y": 90,
            "fontsize": 30,
            "text": "PS",
        },
        {
            "type": "text",
            "stroke": False,
            "x": 100,
            "y": 120,
            "fontsize": 30,
            "text": "RM",
        },
    ]
    icn["GR.IN.IC.MINE"] = {
        "type": "path",
        "d": "m 105,85 10,10 5,-5 c -5,-5 -10,-5 -15,-5 z M 95,85 85,95 80,90 c 5,-5 10,-5 15,-5 z m -5,5 30,30 m -40,0 30,-30",
    }
    icn["GR.IN.IC.PROCESSING FACILITY"] = [
        {
            "type": "text",
            "stroke": False,
            "x": 100,
            "y": 90,
            "fontsize": 30,
            "text": "PROC",
        },
        {
            "type": "text",
            "stroke": False,
            "x": 100,
            "y": 120,
            "fontsize": 30,
            "text": "FAC",
        },
    ]
    icn["GR.IN.IC.UTILITY FACILITY"] = {
        "type": "text",
        "stroke": False,
        "x": 100,
        "y": 110,
        "fontsize": 30,
        "text": "UTIL",
    }
    icn["GR.IN.IC.RESEARCH"] = {
        "type": "text",
        "stroke": False,
        "x": 100,
        "y": 110,
        "fontsize": 30,
        "text": "R&D",
    }
    icn["GR.IN.IC.TELECOMMUNICATIONS"] = {
        "type": "path",
        "d": "m 95,80 10,20 -10,0 10,20",
        "fill": False,
    }
    icn["GR.IN.IC.ELECTRIC POWER"] = {
        "type": "path",
        "d": "m 100,60.5 c -16.4,0 -29.6,13.2 -29.6,29.6 0,12.8 8.3,23.9 19.7,27.8 l 0,19.7 c 3.2,1.2 6.3,1.8 9.9,1.8 3.6,0 6.7,-0.6 9.9,-1.8 l 0,-19.8 c 11.5,-3.9 19.8,-15 19.7,-27.8 0,-16.4 -13.2,-29.6 -29.6,-29.6 z",
        "fill": False,
    }
    icn["GR.IN.IC.ELECTRIC POWER NUCLEAR"] = {
        "type": "text",
        "alignmentBaseline": "middle",
        "stroke": False,
        "x": 100,
        "y": 100,
        "fontsize": 40,
        "text": "N",
    }
    icn["GR.IN.IC.ELECTRIC POWER DAM"] = {
        "type": "text",
        "stroke": False,
        "x": 100,
        "y": 105,
        "fontsize": 40,
        "text": "H",
    }
    icn["GR.IN.IC.ELECTRIC POWER FOSSIL"] = {
        "type": "text",
        "stroke": False,
        "x": 100,
        "y": 105,
        "fontsize": 40,
        "text": "F",
    }
    icn["GR.IN.MC.HOME"] = {
        "type": "path",
        "d": "m 100,82 18,15 h -4 v 22 h -10 v -15 h -8 v 15 H 86 V 97 h -4 z",
        "stroke": False,
    }
    icn["GR.IN.IC.ATOMIC ENERGY"] = {
        "type": "path",
        "d": "M 90.4,119 C 84.2,115 80,109 80,101 l 20,0 -9.6,18 z m 19.6,0 -10,-18 20,0 c 0,8 -4,14 -10,18 z M 100,101 89.7,83.8 c 3,-2 6.5,-3 10.3,-3 4,0 7,1 10,3 L 100,101 Z"
        if STD2525
        else "M 89.9,82.5 110,82.7 89.7,117.1 80,99.9 120.1,100 110,117.3 z",
        "fill": False,
    }
    icn["GR.IN.IC.ATOMIC ENERGY WEAPONS GRADE"] = {
        "type": "path",
        "d": "M 90.4,119 C 84.2,115 80,109 80,101 l 20,0 -9.6,18 z m 19.6,0 -10,-18 20,0 c 0,8 -4,14 -10,18 z M 100,101 89.7,83.8 c 3,-2 6.5,-3 10.3,-3 4,0 7,1 10,3 L 100,101 Z"
        if STD2525
        else "M 89.9,82.5 110,82.7 89.7,117.1 80,99.9 120.1,100 110,117.3 z",
    }
    icn["GR.IN.IC.AIRCRAFT PRODUCTION & ASSEMBLY"] = {
        "type": "path",
        "stroke": False,
        "d": "m 95.1,109.3 c 0,0 -20.8,4.9 -30.1,6.7 -2.2,0.4 -5.7,0.2 -6.5,-2 -0.4,-1.1 3.3,-6.6 6.5,-7.3 8.7,-1.9 25.7,-5.5 25.7,-5.5 l 3.1,-16.1 4,-0.8 0.3,15.9 25.6,-5.8 6.5,-13.2 5.3,-1.4 -3.3,16.1 14,4.8 -4.3,1.2 -13.7,-2.8 -23.6,6.7 31.6,11.8 -5.5,2.5 z",
    }
    icn["GR.IN.IC.AIRPORT"] = {
        "type": "path",
        "fill": False,
        "d": "m 74,118 52,-36  m -53,22 h 54",
    }
    icn["GR.IN.IC.BRIDGE"] = {
        "type": "path",
        "d": "m 70,115 10,-10 40,0 10,10 m -60,-30 10,10 40,0 10,-10",
        "fill": False,
    }
    icn["GR.IN.IC.BASE"] = {
        "type": "path",
        "d": "m 75,85 50,30 m -50,0 50,-30",
        "fill": False,
    }
    icn["GR.IN.IC.SEA SURFACE INSTALLATION, OIL RIG/PLATFORM"] = [
        {
            "type": "path",
            "d": "m 85,105 0,-40 m 25,40 0,15 m -35,0 0,-15 50,0 0,15",
            "fill": False,
        },
        {"type": "path", "d": "m 85,90 15,0 0,15 -15,0 0,-15"},
    ]
    icn["GR.IN.IC.MILITARY/CIVILIAN.MATERIEL"] = text("MAT")
    icn["GR.IN.IC.MILITARY/CIVILIAN.PRINTED MEDIA"] = [
        {"type": "circle", "cx": 100, "cy": 90, "r": 10, "fill": False},
        {"type": "circle", "cx": 100, "cy": 110, "r": 10, "fill": False},
        {"type": "path", "d": "m 65,100 75,0", "fill": False},
    ]
    icn[
        "GR.IN.IC.INFRASTRUCTURE.BANKING FINANCE AND INSURANCE  INFRASTRUCTURE.ECONOMIC INFRASTRUCTURE ASSET"
    ] = text("ECON")
    icn[
        "GR.IN.IC.INFRASTRUCTURE.TELECOMMUNICATIONS INFRASTRUCTURE.TELECOMMUNICATIONS"
    ] = {
        "type": "path",
        "d": "m 90,105 20,0 0,0 m -25,15 15,-30 15,30 m -55,-40 25,10 0,-10 15,10 15,-10 0,10 25,-10",
        "fill": False,
    }
    icn["GR.IN.M1.RADIOLOGICAL"] = textm1("R")
    icn["GR.IN.M1.COAL"] = textm1("CO")
    icn["GR.IN.M1.GEOTHERMAL"] = textm1("GT")
    icn["GR.IN.M1.HYDROELECTRIC"] = textm1("HY")
    icn["GR.IN.M1.NATURAL GAS"] = textm1("NG")
    icn["GR.IN.M1.PETROLEUM"] = {
        "type": "path",
        "d": "M 100,79 V 69 L 91,57 h 18 l -9,12",
        "fill": False,
    }
    icn["GR.IN.M1.CIVILIAN"] = textm1("CIV")
    icn["GR.IN.M1.CIVILIAN TELEPHONE"] = textm1("T")
    icn["GR.IN.M1.CIVILIAN TELEVISION"] = textm1("TV")
    icn["GR.IN.M2.CHEMICAL WARFARE PRODUCTION"] = textm2("C")
    icn["GR.IN.M2.NUCLEAR WARFARE PRODUCTION"] = textm2("N")
    icn["GR.IN.M2.RADIOLOGICAL WARFARE PRODUCTION"] = textm2("R")
    icn["GR.IN.M2.TRANSPORTATION"] = {
        "type": "path",
        "d": "M 112,134 A 12.3,12.2 0 0 1 99.7,146 12.3,12.2 0 0 1 87.6,134 12.3,12.2 0 0 1 99.7,122 12.3,12.2 0 0 1 112,134 Z  m -12,-12 v 24  M 88.7,128 111,139  m -22.3,0 22.3,-11",
        "fill": False,
    }
    icn["GR.IN.M2.ATOMIC ENERGY REACTOR"] = textm2("A")
    icn["GR.IN.M2.NUCLEAR MATERIAL PRODUCTION"] = textm2("P")
    icn["GR.IN.M2.NUCLEAR MATERIAL STORAGE"] = textm2("S")
    icn["GR.IN.M2.CHEMICAL & BIOLOGICAL WARFARE"] = textm2("B")
    icn["GR.IN.M2.SHIP CONSTRUCTION"] = textm2("YRD")
    icn["GR.IN.M2.WEAPONS GRADE PRODUCTION"] = textm2("WPN")
    # SUBSURFACE
    icn["SOF.IC.UNDERWATER DEMOLITION TEAM"] = text("UD")
    icn["SOF.M2.ATTACK"] = textm2("A")
    icn["SOF.M2.REFUEL"] = textm2("K")
    icn["SOF.M2.UTILITY"] = textm2("U")
    icn["SOF.M2.VSTOL"] = {
        "type": "text",
        "stroke": False,
        "x": 100,
        "y": 135,
        "fontsize": 20,
        "text": "VSTOL",
    }
    icn["SOF.M2.COMBAT SEARCH AND RESCUE"] = textm2("CSAR") if STD2525 else textm2("H")
    # STABILITY OPERATIONS ==========================================================
    icn["ST.IC.ARREST"] = {
        "type": "path",
        "d": "m 92.5,100 15,0 m -2.5,-10 c 0,2.8 -2.2,5 -5,5 -2.8,0 -5,-2.2 -5,-5 0,-2.8 2.2,-5 5,-5 2.8,0 5,2.2 5,5 z m -5,5 0,20 m 20,-15 c 0,11 -9,20 -20,20 -11,0 -20,-9 -20,-20 0,-11 9,-20 20,-20 11,0 20,9 20,20 z",
        "fill": False,
    }
    icn["ST.IC.ARSON/FIRE"] = [
        {
            "type": "path",
            "d": "m 84.6,101.6 c 1.3,23.1 31,23.2 30.7,-1.9 -1.5,2.1 -4.6,6.5 -8.1,7.3 1.9,-2.4 2.6,-8.5 2.4,-12.9 -1.7,3.4 -4,7.9 -7,7.8 1.7,-4.3 2.7,-9.4 -0.5,-13.7 -0.2,3 0.8,7.1 -1.9,7 -2.7,-0.1 -2.9,-4.4 -1.1,-10.8 -4,4.1 -6.2,9.8 -3.8,17.5 -1.9,-0.2 -4.4,-1.9 -7,-7.8 -1.5,4.9 1.2,9.6 3.2,13.7 -2.4,-1.1 -6,-3 -7,-6.2 z",
            "stroke": False,
        },
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 70,
        },
    ]

    icn["ST.IC.ATTEMPTED CRIMINAL ACTIVITY"] = {
        "type": "path",
        "d": "m 127,114.4 5,2.7  m -15,-8.1 5,2.7  m -15,-8.1 5,2.7  m -15,-8.16 5,2.76  m -15,-8.19 5,2.72  M 77,87.29 82,90  m -15,-8.14 5,2.71",
        "fill": False,
    }
    icn["ST.IC.BLACK LIST LOCATION"] = text("BLK")
    icn["ST.IC.BLACK MARKETING"] = [
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 93,
            "fontsize": 22,
            "text": "BLK",
        },
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 110,
            "fontsize": 22,
            "text": "MKT",
        },
    ]
    icn["ST.IC.BOMB"] = text("BOMB")
    icn["ST.IC.BOOBY TRAP"] = {
        "type": "path",
        "d": "m 85,105 15,-25 15,25 m -35,5 c 0,-10 40,-10 40,0 0,10 -40,10 -40,0 z",
        "fill": False,
    }
    icn["ST.IC.COMPOSITE LOSS"] = {
        "type": "path",
        "d": "m 100,85 0,30 m -35,-15 45,0 m 20,0 c 0,5.5 -4.5,10 -10,10 -5.5,0 -10,-4.5 -10,-10 0,-5.5 4.5,-10 10,-10 5.5,0 10,4.5 10,10 z",
        "fill": False,
    }
    icn["ST.IC.DEMONSTRATION"] = text("MASS")
    icn["ST.IC.DRIVE-BY SHOOTING"] = {
        "type": "path",
        "d": "m 95,85 5,-5 5,5 m -5,-5 0,30 m -15,0 30,0 m 5,5 c 0,2.8 -2.2,5 -5,5 -2.8,0 -5,-2.2 -5,-5 0,-2.8 2.2,-5 5,-5 2.8,0 5,2.2 5,5 z m -30,0 c 0,2.8 -2.2,5 -5,5 -2.8,0 -5,-2.2 -5,-5 0,-2.8 2.2,-5 5,-5 2.8,0 5,2.2 5,5 z",
        "fill": False,
    }
    icn["ST.IC.DRUG RELATED ACTIVITIES"] = text("DRUG")
    icn["ST.IC.EXPLOSION"] = {
        "type": "path",
        "d": "m 110,55 5,20 15,-10 0,15 15,5 -15,10 15,10 -15,5 5,15 -20,-5 -5,20 -10,-15 -10,20 -5,-25 -20,10 5,-15 L 55,105 70,95 60,85 70,80 70,65 85,75 90,55 100,70 z",
        "fill": False,
    }
    icn["ST.IC.EXTORTION"] = {
        "type": "text",
        "stroke": False,
        "textanchor": "middle",
        "alignmentBaseline": "middle",
        "x": 100,
        "y": 103,
        "fontsize": 80,
        "text": "$",
    }
    icn["ST.IC.FOOD DISTRIBUTION"] = [
        {
            "type": "path",
            "d": "M 111,115 C 96.3,110 96.3,89.5 111,84 100,79.7 87.5,86.3 87.5,99.5 87.5,113 100,119 111,115 Z",
            "fill": False,
        },
        {
            "Unknown": {"type": "path", "d": "M35,120 l130,0 ", "fill": False},
            "Friend": {"type": "path", "d": "M25,120 l150,0 ", "fill": False},
            "Neutral": {"type": "path", "d": "M45,120 l110,0 ", "fill": False},
            "Hostile": {"type": "path", "d": "M50,120 l100,0 ", "fill": False},
        }.get(affiliation),
    ]
    icn["ST.IC.GRAFFITI"] = {
        "type": "path",
        "d": "m 110,80 c -10,0 -10,10 0,10 10,0 10,10 0,10 -10,0 -10,10 0,10 10,0 10,10 0,10 M 90,80 c -10,0 -10,10 0,10 10,0 10,10 0,10 -10,0 -10,10 0,10 10,0 10,10 0,10",
        "fill": False,
    }
    icn["ST.IC.GROUP"] = {
        "type": "path",
        "d": "m 133,90 c 0,10 -15,10 -15,0 0,-10 15,-10 15,0 z m -8,7.3 0,25 m -10,-20 20,0 m -52,-12.3 c 0,10 -15,10 -15,0 0,-10 15,-10 15,0 z m -8,7.3 0,25 m -10,-20 20,0 m 23,-7.3 c 0,10 -15,10 -15,0 0,-10 15,-10 15,0 z m -8,7.3 0,25 m -10,-20 20,0",
        "fill": False,
    }
    icn["ST.IC.HIJACKING (AIRPLANE)"] = {
        "type": "path",
        "fill": iconFillColor if STD2525 else False,
        "d": "m 70,95 0,10 65,0 0,-10 z m 55,10 0,10 5,0 0,-10 z m 0,-10 0,-10 5,0 0,10 z m -45,10 0,15 10,0 0,-15 z m 0,-10 0,-15 10,0 0,15 z",
    }
    frame = metadata.get("frame", False)  # Ensure frame is available
    icn["ST.IC.HIJACKING (BOAT)"] = {
        "type": "path",
        "fill": iconFillColor if STD2525 else (iconFillColor if not frame else False),
        "d": "m 105,80 0,20 20,0 z m -5,25 0,-25 m -30,25 10,15 40,0 10,-15 z",
    }
    icn["ST.IC.GRAY LIST LOCATION"] = text("GRAY")
    icn["ST.IC.IED"] = text("IED")
    icn["ST.IC.INDIVIDUAL"] = {
        "type": "path",
        "d": "m 108,90 c 0,10 -15,10 -15,0 0,-10 15,-10 15,0 z m -8,7.3 0,25 m -10,-20 20,0",
        "fill": False,
    }
    icn["ST.IC.INTERNAL SECURITY FORCE"] = text("ISF")
    icn["ST.IC.KILLING VICTIM"] = [
        {
            "type": "path",
            "d": "m 108,90 c 0,10 -15,10 -15,0 0,-10 15,-10 15,0 z m -8,7.3 0,25 m -10,-20 20,0",
            "fill": False,
        },
        {
            "Unknown": {"type": "path", "fill": False, "d": "M50,65 150,135"},
            "Friend": {"type": "path", "fill": False, "d": "M25,50 175,150"},
            "Neutral": {"type": "path", "fill": False, "d": "M45,45 155,155"},
            "Hostile": {"type": "path", "fill": False, "d": "M57,70 143,130"},
        }.get(affiliation),
    ]
    icn["ST.IC.KILLING VICTIMS"] = [
        {
            "type": "path",
            "d": "m 133,90 c 0,10 -15,10 -15,0 0,-10 15,-10 15,0 z m -8,7.3 0,25 m -10,-20 20,0 m -52,-12.3 c 0,10 -15,10 -15,0 0,-10 15,-10 15,0 z m -8,7.3 0,25 m -10,-20 20,0 m 23,-7.3 c 0,10 -15,10 -15,0 0,-10 15,-10 15,0 z m -8,7.3 0,25 m -10,-20 20,0",
            "fill": False,
        },
        {
            "Unknown": {"type": "path", "fill": False, "d": "M50,65 150,135"},
            "Friend": {"type": "path", "fill": False, "d": "M25,50 175,150"},
            "Neutral": {"type": "path", "fill": False, "d": "M45,45 155,155"},
            "Hostile": {"type": "path", "fill": False, "d": "M57,70 143,130"},
        }.get(affiliation),
    ]
    icn["ST.IC.KNOWN INSURGENT VEHICLE"] = {
        "type": "path",
        "d": "m 65,95 70,0 m 0,10 c 0,5.5 -4.5,10 -10,10 -5.5,0 -10,-4.5 -10,-10 0,-5.5 4.5,-10 10,-10 5.5,0 10,4.5 10,10 z m -50,0 c 0,5.5 -4.5,10 -10,10 -5.5,0 -10,-4.5 -10,-10 0,-5.5 4.5,-10 10,-10 5.5,0 10,4.5 10,10 z",
        "fill": False,
    }
    icn["ST.IC.MASS GRAVE LOCATION"] = {
        "type": "path",
        "d": "m 77.5,90 10,0 m -5,-5 0,15 m 7.5,-20 0,30 -15,0 0,-30 z m 22.5,10 10,0 m -5,-5 0,15 m -7.5,-20 0,30 15,0 0,-30 z m -15,20 10,0 m -5,-5 0,20 m -7.5,-25 15,0 0,30 -15,0 z",
        "fill": False,
    }
    icn["ST.IC.MINE LAYING"] = [
        {"type": "path", "d": "m 60,85 80,0 0,30 -80,0 z", "fill": False},
        {
            "type": "path",
            "d": "m 135,100 c 0,5.5 -4.5,10 -10,10 -5.5,0 -10,-4.5 -10,-10 0,-5.5 4.5,-10 10,-10 5.5,0 10,4.5 10,10 z m -25,0 c 0,5.5 -4.5,10 -10,10 -5.5,0 -10,-4.5 -10,-10 0,-5.5 4.5,-10 10,-10 5.5,0 10,4.5 10,10 z m -25,0 c 0,5.5 -4.5,10 -10,10 -5.5,0 -10,-4.5 -10,-10 0,-5.5 4.5,-10 10,-10 5.5,0 10,4.5 10,10 z",
            "stroke": False,
        },
    ]
    icn["ST.IC.PATROLLING"] = {
        "type": "path",
        "d": "m 131,97 0,-14 5,0 c 4,0 4,7 0,7 l -5,0 m -71,15 15,10 M 60,105 75,95 m -15,10 40,0 -15,-15 40,0",
        "fill": False,
    }
    icn["ST.IC.POISONING"] = {
        "type": "path",
        "d": "m 85,95 c 0,-20 30,-20 30,0 0,20 -30,20 -30,0 z m -15,10 60,15 m -60,0 60,-15",
        "fill": False,
    }
    icn["ST.IC.PSYCHOLOGICAL OPERATIONS"] = {
        "type": "path",
        "fill": iconFillColor if STD2525 else False,
        "stroke": "black",
        "d": "m 110,95 10,0 m -10,10 10,0 m -10,10 10,0 m -10,-30 10,0 m -10,-5 -10,10 -30,0 0,20 30,0 10,10 z",
    }
    icn["ST.IC.RADIO AND TELEVISION PSYCHOLOGICAL OPERATIONS"] = [
        icn["ST.IC.PSYCHOLOGICAL OPERATIONS"],
        {
            "Unknown": {
                "type": "path",
                "fill": False,
                "d": "M50,65 100,110 100,90 150,135",
            },
            "Friend": {
                "type": "path",
                "fill": False,
                "d": "M25,50 100,110 100,90 175,150",
            },
            "Neutral": {
                "type": "path",
                "fill": False,
                "d": "M45,45 100,110 100,90 155,155",
            },
            "Hostile": {
                "type": "path",
                "fill": False,
                "d": "M57,70 100,110 100,90 143,130",
            },
        }.get(affiliation),
    ]
    icn["ST.IC.RIOT"] = text("RIOT")
    icn["ST.IC.SAFE HOUSE"] = text("SAFE")
    icn["ST.IC.SEARCHING"] = {
        "type": "path",
        "d": "m 140,105 c -10,0 -5,0 -10,0 -15,0 -5,-15 -20,-15 -15,0 -5,20 -20,20 -15,0 -5,-20 -20,-20 -10,0 -10,10 -10,10 m 70,0 10,5 -10,5",
        "fill": False,
    }
    icn["ST.IC.SPY"] = text("SPY")
    icn["ST.IC.SNIPING"] = [
        {"type": "path", "d": "m 95,85 5,-5 5,5 m -5,-5 0,40", "fill": False},
        {
            "type": "text",
            "alignmentBaseline": "middle",
            "stroke": False,
            "x": 100,
            "y": 65,
            "fontsize": 25,
            "text": "S",
        },
    ]
    icn["ST.IC.VANDALISM/LOOT/RANSACK/PLUNDER/SACK"] = {
        "type": "path",
        "d": "m 115,100 c 0,-5 5,-10 10,-10 M 85,100 C 85,95 80,90 75,90 m 5,25 c -0.5,-29.5 40,-30 40,0 z",
        "fill": False,
    }
    icn["ST.IC.WHITE LIST LOCATION"] = text("WHT")
    icn["ST.IC.ROBBERY"] = text("ROB")
    icn["ST.IC.THEFT"] = text("THF")
    icn["ST.IC.BURGLARY"] = text("BUR")
    icn["ST.IC.SMUGGLING"] = text("SMGL")
    icn["ST.IC.SABOTAGE"] = text("SAB")
    icn["ST.IC.ILLEGAL DRUG OPERATION"] = text("DRUG")
    icn["ST.IC.SPY"] = text("SPY")
    icn["ST.IC.WARRANT SERVED"] = text("WNT")
    icn["ST.IC.POLLING PLACE/ELECTION"] = text("VOTE")
    icn["ST.IC.NATURAL EVENT"] = text("NAT")
    icn["ST.IC.GEOLOGIC"] = text("GEOL")
    icn["ST.IC.HYDRO-METEOROLOGICAL"] = text("HYDR")
    icn["ST.IC.INFESTATION"] = text("INFS")
    icn["ST.IC.GRENADE"] = text("G")
    icn["ST.IC.INCENDIARY"] = text("I")
    icn["ST.IC.MINE"] = text("M")
    icn["ST.IC.HOUSE"] = {
        "type": "path",
        "fill": iconFillColor if STD2525 else False,
        "d": "m 70,100 60,0 m -30,-20 -30,20 0,35 60,0 0,-35 -30,-20 z",
    }
    icn["ST.IC.ROCK THROWING"] = {
        "type": "path",
        "d": "m 90,60 25,25 M 70,65 95,90 M 60,80 80,100 m 45,-5 5,15 -5,15 -20,10 -20,-5 -5,-20 5,-5 10,0 5,-10 10,-5 15,5 z",
    }
    icn["ST.M1.ACCIDENT"] = textm1("ACC")
    icn["ST.M1.ASSASSINATION"] = textm1("AS")
    icn["ST.M1.CIVILIAN"] = textm1("CIV")
    icn["ST.M1.COERCED/IMPRESSED"] = textm1("UR")
    icn["ST.M1.COMBAT"] = textm1("CBT")
    icn["ST.M1.DEAD BODY"] = textm1("DB")
    icn["ST.M1.DISPLACED PERSONS, REFUGEES, AND EVACUEES"] = textm1("DPRE")
    icn["ST.M1.DRUG"] = textm1("DRUG")
    icn["ST.M1.EVICTION"] = textm1("EV")
    icn["ST.M1.EXECUTION (WRONGFUL KILLING)"] = textm1("EX")
    icn["ST.M1.EXFILTRATION"] = textm1("EXFL")
    icn["ST.M1.FOREIGN FIGHTERS"] = textm1("FF")
    icn["ST.M1.GANG"] = textm1("GANG")
    icn["ST.M1.GOVERNMENT ORGANIZATION"] = textm1("GO")
    icn["ST.M1.HIJACKING/HIJACKED"] = textm1("H")
    icn["ST.M1.HOUSE-TO-HOUSE"] = {
        "type": "path",
        "fill": iconFillColor if STD2525 else False,
        "d": "m 110,65 -20,0 0,15 20,0 z m -10,-10 -10,10 20,0 z",
    }
    icn["ST.M1.IED"] = textm1("IED")
    icn["ST.M1.INCIDENT"] = textm1("INC")
    icn["ST.M1.INFILTRATION"] = textm1("INFL")
    icn["ST.M1.KIDNAPPING"] = textm1("K")
    icn["ST.M1.LABRATORY"] = textm1("LAB")
    icn["ST.M1.LEADER"] = textm1("LDR")
    icn["ST.M1.LOOT"] = textm1("LOOT")
    icn["ST.M1.MEETING"] = textm1("MTG")
    icn["ST.M1.MURDER"] = textm1("MU")
    icn["ST.M1.NONGOVERNMENTAL ORGANIZATION (NGO)"] = textm1("NGO")
    icn["ST.M1.OTHER"] = textm1("OTH")
    icn["ST.M1.PIRACY"] = textm1("PI")
    icn["ST.M1.PREMATURE"] = textm1("P")
    icn["ST.M1.RAID"] = textm1("RAID")
    icn["ST.M1.RAPE"] = textm1("RA")
    icn["ST.M1.RELIGIOUS"] = textm1("REL")
    icn["ST.M1.SPEAKER"] = textm1("SPK")
    icn["ST.M1.TARGETED"] = textm1("TGT")
    icn["ST.M1.TERRORIST"] = textm1("TER")
    icn["ST.M1.TRAFFICKING"] = textm1("TFK")
    icn["ST.M1.WILLING RECRUIT"] = textm1("WR")
    icn["ST.M1.WRITTEN PSYCHOLOGICAL OPERATIONS"] = textm1("W")
    icn["ST.M1.WILLING"] = textm1("W")
    icn["ST.M1.FALSE"] = textm1("FAL")
    icn["ST.M1.FIND"] = textm1("FND")
    icn["ST.M1.FOUND AND CLEARED"] = textm1("CLR")
    icn["ST.M1.HOAX (DECOY)"] = {
        "type": "path",
        "d": "M 90,75 80,67.5 90,60 90,75 Z m 15,0 -10,-7.5 10,-7.5 0,15 z m 15,0 -10,-7.5 10,-7.5 0,15 z",
    }
    icn["ST.M1.ATTEMPTED"] = textm1("ATT")
    icn["ST.M1.ACCIDENT"] = textm1("ACC")
    icn["ST.M1.INCIDENT"] = textm1("INC")
    icn["ST.M1.THEFT"] = textm1("THF")
    icn["ST.M1.PIRATE"] = [
        {"type": "circle", "cx": 100, "cy": 60, "r": 7, "fill": False},
        {
            "type": "path",
            "fill": False,
            "d": "m 82.5,75 35,-15 m 0,15 -35,-15 m 3,7 5,10 m 27,-10 -10,10",
        },
    ]

    icn["ST.M1.ACCIDENT"] = textm1("ACC")
    icn["ST.M1.INCIDENT"] = textm1("INC")
    icn["ST.M1.THEFT"] = textm1("THF")
    icn["ST.M1.PIRATE"] = [
        {"type": "circle", "cx": 100, "cy": 60, "r": 7, "fill": False},
        {
            "type": "path",
            "fill": False,
            "d": "m 82.5,75 35,-15 m 0,15 -35,-15 m 3,7 5,10 m 27,-10 -10,10",
        },
    ]
    icn["ST.M2.LEADER OR LEADERSHIP"] = textm2("LDR")
    icn["ST.M2.RELIGIOUS"] = textm2("REL")
    icn["AC.IC.CRIMINAL.ACTIVITY.INCIDENT"] = [
        {
            "type": "path",
            "stroke": False,
            "d": "m 98.7,66.7 c -3.2,0.7 -6.3,3.7 -6.4,7 0.3,3.6 5.3,2.8 7,0.6 2,-1.2 1.7,-4.5 4.5,-3.7 2.6,-0.6 3.2,3.2 5.9,3.2 1.6,1.5 4.4,-0.6 5.4,1.2 0.7,1.1 1.5,2.2 2.2,3.3 -2,3.1 -1.3,7.9 1.9,10 3.5,1.1 4.8,-3.5 4.1,-6.2 -0.2,-3 -2.5,-5 -5.1,-5.4 -1.5,-1.9 -2.7,-3.4 -1.6,-5.6 -1,-3.3 -5.1,-4.5 -8.2,-4.3 -2.2,0.3 -2.9,2.6 -5.3,1.9 -1.9,0.4 -1.9,-2.8 -4.3,-2 z m 0.2,1.3 c 2.7,0.5 0.9,0.6 -0.6,1.3 -0.5,2.2 3.8,0.4 1.4,2.9 -0.9,1.9 -5.8,4.7 -5.9,1.1 0.1,-2.5 2.7,-4.8 5.1,-5.2 z m 10.3,0.1 c 2.4,-0.5 7.1,2.3 5.6,3.7 -0.8,-2.1 -3,0 -1.2,1.2 -1.7,0.9 -7.4,-1.6 -5.7,-2.4 2.5,0.8 2.8,-2.7 -0,-1.9 -1.4,0.2 1.1,-0.8 1.3,-0.6 z M 81.9,71.6 c -1.8,1.9 -3.6,3.9 -5.5,5.8 -7.5,-0.1 -14,6.2 -15.7,13.2 -0.6,4.2 0.5,8.5 2.8,12 0.7,3.9 -3.2,6.7 -3,10.7 -0.8,7.4 4.8,14.5 11.7,16.8 2.3,-0.4 1.3,1.3 1.4,2 1.5,-0.4 3,-0.8 4.6,-1.2 -0.2,1.5 -0.1,2.7 1.4,1.2 0.9,-0.3 2.3,-2.2 2.9,-1.5 0.2,2.2 1.2,0.1 2,-0.7 0.8,-1.2 1.6,-2.3 2.4,-0.5 1.2,-2.4 4.1,-7.2 -0.8,-7.3 -3.4,2.3 -7.5,4.6 -11.8,3.5 -6.3,-1.5 -10.9,-8.8 -8.2,-14.9 0.4,-3.9 6.8,-3.4 5,-8.2 -1.8,-2.6 -5.7,-2.9 -5.7,-7 -1.5,-7.3 5.6,-14.7 13,-13.7 4.7,0.5 7.4,4.9 10.8,7.6 1.9,1.9 4.1,5.1 5.9,1.4 2.8,-2 4.3,-4.7 1.8,-7.6 C 94.8,79.7 90.9,77.3 88,74.4 86.3,72.9 83.9,72.6 81.9,71.6 z m 3.3,3.8 c 1.6,1.1 2.9,2.1 0.3,3.3 -0.9,3.7 -5.1,-0.5 -1.5,-1.5 0.4,-0.6 0.9,-1.1 1.2,-1.8 z m 34.2,3.1 c 3,1.4 3.9,6.4 1.4,8.8 -2.9,0.1 -3.6,-4.3 -3.1,-6.6 0.1,-2.9 2.5,2.7 2.5,-0.7 -0.2,-0.5 -0.5,-1 -0.8,-1.4 z M 127.3,90.2 c -4.3,0.4 -8.8,-0 -13.1,1 -2.1,1.1 -5.7,1.5 -4.6,4.5 0.1,1.8 0.2,3.6 0.4,5.4 -4.9,4.9 -5.5,13.3 -2.2,19.2 2.4,4.3 7,7 11.8,7.8 3.3,4.9 7.3,-1.3 11.2,-1.7 5.5,-2.5 8.9,-8.5 8.5,-14.5 0.2,-5 -2.4,-10.1 -6.7,-12.8 -0.1,-2.3 -0.2,-4.6 -0.3,-6.9 -1.6,-0.8 -3.4,-1.4 -5.1,-2.1 z M 127.8,92.5 c -0.9,1.7 0.6,3.8 -0.9,4.9 -2.3,0.7 -1.7,-2.4 -1.9,-3.8 -0.6,-1.7 1.9,-0.7 2.8,-1 z m -2.9,8.3 c 4.1,0.9 8,3.7 9.3,7.9 0.9,3.7 0.5,8 -2.3,10.9 -1.7,2 -5.3,4.3 -7.7,3.1 -3.1,-0.8 -5.8,2.1 -8.6,-0.5 -6.9,-4.2 -7.2,-16 0.2,-19.8 2.7,-1.6 6,-1.6 9.1,-1.6 z",
        },
        {
            "type": "path",
            "stroke": False,
            "fill": iconFillColor if STD2525 else False,
            "d": "M 85.1 75.3 C 85 75.8 84.2 76.7 83.9 77.1 C 83.6 77.6 82.4 77.9 82.4 78.6 L 82.4 79 C 82.4 79.4 83.3 80.1 83.6 80.1 L 83.8 80.1 C 84.8 80.1 85 79.1 85.4 78.6 C 85.7 78.2 86.7 77.4 87.2 77 L 85.1 75.3 z M 127.8 92.5 L 125 92.7 L 125.2 96.5 C 125.3 97.5 125.9 97.3 126.5 97.6 C 127.1 97.3 127.8 97.1 127.8 96.3 C 127.8 95.8 127.7 95.6 127.5 95.3 L 127.8 92.5 z",
        },
    ]
    icn["AC.IC.CRIMINAL.CIVIL DISTURBANCE"] = {
        "type": "path",
        "stroke": False,
        "d": "m 110.6,142.4 0,-28.6 -7.1,0 0,28.6 z m -21.2,0 7.1,0 0,-28.6 -7.1,0 z m 7.1,-28.6 h 7.1 v -11.8 h 24.4 V 77.2 h -6.3 v 18.6 h -18 v -10.7 c 0,-0.9 2.1,-1.2 3,-1.7 0.8,-0.4 2.1,-1.4 2.7,-2 1.5,-1.4 3.2,-3.6 3.8,-5.9 1.6,-6.3 -0.2,-10.6 -3.8,-14.1 -3,-3.1 -9.2,-4.9 -14.3,-2.7 -3.6,1.6 -8.4,6.2 -8.4,11 v 3.2 c 0,2.8 1.9,6.2 3.3,7.7 1,1 1.8,1.7 3,2.5 1,0.6 3.6,1.3 3.6,2.2 v 10.7 H 78.4 v -18.6 h -6.3 v 24.9 h 24.4 v 11.8 h -0 z",
    }
    icn["AC.IC.SHOOTING"] = {
        "type": "path",
        "stroke": False,
        "d": "m 93.2,89.7 h 16.8 v 9.3 c -2.6,0 -7.3,1.6 -9,1 -2.3,-0.8 -5.4,-2 -7.8,-2.6 v -7.8 l 0,0 z m -30,0 h 26.1 v 9.6 c 0,0.9 4.1,2 5,2.3 1.9,0.6 3.6,1.4 5.5,2 2,0.7 3.4,0.4 6,-0.1 1.6,-0.3 5.7,-0.4 6.6,-0.9 0.6,2.7 4.6,14 4.6,15.2 0,1.6 -1.2,4 -1.3,5.7 l 21.5,0 -8.2,-25.9 7.8,-7.7 c -0.8,-1.6 -4.1,-13.4 -5.2,-13.4 h -68.4 v 13.2 l 0,0 z",
    }
    icn["AC.IC.FIRE EVENT"] = {
        "type": "path",
        "stroke": False,
        "d": "m 96.5,78.5 c 0,-5.1 4.1,-9.7 4.1,-13 v -0.4 c 0,-1.3 -0,-3.8 -1.1,-4.1 -1,4.5 -3.5,8 -5.9,11.2 -1.2,1.6 -2.4,3.3 -3.6,5 -1,1.4 -3.1,3.5 -3.1,5.5 0,1.4 6.1,17.7 3,17.7 -0.1,0 -3.8,-2.5 -4.2,-2.9 -1.4,-1 -2.4,-2.3 -3.3,-3.7 -3.1,-4.6 -2.4,-4.4 -3.8,-10.3 -1.5,0.4 -2.6,5 -2.9,6.9 -0.4,2.4 -0.3,6.6 0.2,9 0.6,2.8 1.4,5 2.5,7.3 0.6,1.2 3,5.5 3.1,6.5 -2.2,-0.5 -7,-4.6 -8.6,-6.2 -1.5,-1.5 -5.5,-8.3 -5.9,-8.6 0,9.9 5,22.8 9.8,27.6 3.1,3.1 6.3,6.4 10.2,8.6 2.4,1.5 10.5,4.3 14.3,4.3 h 2.4 c 2.8,0 10.8,-3 12.9,-4.2 3.4,-1.9 6.9,-4.7 9,-7.9 4.4,-6.5 8,-15 8,-25.8 v -1.3 l -0.4,-5.8 c -0.7,0.4 -2.2,4.4 -2.5,5.2 -0.5,1.3 -2,3.4 -2.9,4.6 -1.4,2.1 -5.2,6.3 -7.8,6.9 v -1.1 c 0,-4.4 2.8,-8.8 2.8,-12.4 v -1.9 l -1.3,-12.2 h -0.6 c -0.3,3.9 -1.6,7.9 -3.4,10.5 -1.3,2 -5.3,5.6 -7.7,6.2 -0.2,-0.4 -0.4,-0.6 -0.4,-1.3 v -2.3 c 0,-5.1 3,-8.9 3,-12.8 v -0.8 c 0,-1.5 -2.1,-3.9 -2.9,-5.2 -0.7,-1.1 -2.4,-4.3 -3.5,-4.6 v 1.3 c 0,6.2 -1.4,10.6 -5.6,12.6 -1.1,-1.7 -3.6,-3.2 -3.6,-6.2 v -1.9 l 0,0 z",
    }
    icn["AC.IC.NON-REsIdENTIAL FIRE"] = {
        "type": "path",
        "stroke": False,
        "d": "m 121.2,122.3 -6.2,0 0,5.9 6.2,0 z m -12.1,0 -6.1,0 0,5.9 6.1,0 z m -12.2,0 -5.9,0 0,5.9 5.9,0 z m -12.3,0 -5.7,0 0,5.9 5.7,0 z m 30.4,-4.8 h 6.1 v -6.2 h -2.5 c -1.2,0 -2.5,1.5 -3.6,1.8 v 4.4 z m -5.9,-6.2 -6.1,0 0,6.2 6.1,0 z m -12.2,0 -5.9,0 0,6.2 5.9,0 z m -12.3,0 -5.7,0 0,6.2 5.7,0 z m 25,-33.4 c 0,-3.4 3.4,-7.4 3.4,-9.1 0,-1.4 -0.8,-4.2 -1.8,-4.6 0,7.1 -8.6,12.8 -8.6,15.7 v 0.4 c 0,0.7 1.9,5.2 2.3,6.6 0.4,1.7 1.4,5.6 1.6,7.3 -6.2,-0.1 -7.3,-9.8 -10.3,-11.8 l -0.3,3 0,4.6 c 0,4.7 3.4,11.4 5.6,13.9 1,1.1 4.2,3.7 5.5,4.3 0.8,0.4 6.3,3 6.6,3 1.4,0 9.2,-7.2 10.5,-8.6 2.5,-2.5 4,-9.6 4,-14.8 v -0.7 l -0.7,-5.7 c -1,0.6 -2.1,5.6 -2.8,7 -1.5,3.2 -1.8,3.1 -5.4,4 -0.3,-12.2 6.7,-8.3 -2.7,-19.1 0,4.9 -0.9,7.9 -4.1,9.6 -1.4,-0.7 -3,-2.7 -3,-4.8 z m -14.8,26.4 h 3.6 c -0.1,-0.6 -0.3,-1.4 -1.1,-1.4 h -1.2 v -2.7 c 0,-0.9 -0.9,-2.4 -1.4,-3 v 7 z m -16.4,-28.6 h 3.9 v 28.6 h 8.9 v -28.6 h 3.6 v 5.4 c 0.3,-0.2 1.4,-1.4 1.4,-1.8 v -5 h -6.4 v 28.6 h -6.4 v -28.6 h -6.1 v 28.6 h -5.2 v 32.7 h 54.8 v -30.7 c -0.4,0.2 -1.1,1 -1.1,1.6 v 27.5 h -52.5 v -29.8 h 5.2 v -28.6 h -0 z",
    }
    icn["AC.IC.REsIdENTIAL FIRE"] = {
        "type": "path",
        "stroke": False,
        "d": "m 91.5,88.3 -0.7,-3 -30.1,25.2 15.6,0.1 v 25.6 h 50.5 v -25.6 h 12.4 c -0.4,-0.5 -7.6,-5.9 -8,-5.9 -0.3,0 -1.2,1.6 -1.4,1.9 l 1.4,1.4 h -2.4 c -0.7,0.5 -4.9,3.1 -4.9,3.8 v 22.3 h -18.3 v -12.9 h -8.7 v 12.9 h -18.1 v -23.5 h 22.6 l -2.2,-2.7 -30.7,-0.1 L 91.5,88.3 z m 27.6,28 -8.2,0 0,8.5 8.2,0 z m -27,0.2 -8.7,0 0,8.2 8.7,0 z m 11,-36.4 c 0,0.9 2.1,5.3 2.5,6.9 0.4,1.8 1.5,6.1 1.5,7.8 -7.1,-1.6 -6.9,-9.9 -10.3,-12.2 -1.7,7.5 0.8,15.1 3.7,19.5 2.4,3.6 2.6,3.4 6,6 0.4,0.4 7.9,4.3 7.9,4.3 2,0 9.6,-7.1 11.1,-8.6 1.8,-1.8 5.6,-10.8 5.6,-14.4 V 83.5 c 0,-1.9 -0.3,-3.2 -1.4,-4 0,2 -1.8,7 -2.6,8.4 -0.8,1.8 -4.3,4.2 -6.3,4.7 v -1.7 c 0,-4.4 2.4,-6.8 2.4,-10.1 0,-2 -4,-7.2 -5.2,-8 0,5.4 -0.7,8 -4.2,9.8 -1.2,-0.7 -3.1,-2.6 -3.1,-4.4 v -1 c 0,-1.5 1.8,-5.4 2.5,-6.6 2,-3.9 0.5,-3.8 -0.4,-7 h -0.4 c -1.3,5.5 -0.8,4.8 -3.8,8.9 -1,1.4 -5.4,5.9 -5.4,7.5 z",
    }
    icn["AC.IC.SCHOOL FIRE"] = {
        "type": "path",
        "stroke": False,
        "d": "m 131.3,73 c -4,-1 -17,-7.2 -19.8,-7.2 h -2.4 V 96 h -0.7 c 0,5.6 -3.8,15.3 -6.2,18.6 -2,2.7 -3.7,4.1 -6.2,6.2 -0.8,0.6 -7,4.9 -7,5.4 v 8 h 44.1 V 96 h -20.4 l 0,-14.8 18.8,-8.2 z m -49.2,11.8 c 0,-3 3.6,-8 3.6,-10 0,-1.8 -0.8,-3.9 -2,-4.6 -0.4,0.8 -0.4,3.6 -0.9,5 -0.3,0.7 -1.8,2.7 -2.3,3.5 -1.6,2.3 -3.4,4.2 -5.1,6.4 -2.2,2.8 0,5 1.1,8.2 0.8,2.2 1.4,7.9 2.1,9.4 C 71.9,102.4 70.6,91.8 67.6,89.9 l -0.6,7.6 0.1,0.2 c 0,5 3.6,12.3 5.9,15 1.1,1.3 4.3,3.6 5.9,4.6 1.1,0.7 2.5,1 3.7,1.6 0.4,0.2 3.2,1.9 3.2,1.9 2.1,0 9.9,-7.4 11.5,-9 1.8,-1.8 5.8,-11 5.8,-14.4 v -6.3 c 0,-2.1 -0.4,-2.6 -0.7,-4.2 h -0.8 c -0.2,1.9 -2.2,7.1 -3,8.7 -0.7,1.3 -6.3,5.7 -6.3,3.7 v -1.2 c 0,-3.8 2.4,-7.2 2.4,-10 v -0.8 c 0,-1.5 -4.3,-6.8 -5.4,-7.6 0,2.5 0.1,4.8 -0.8,6.5 -0.5,0.9 -2.5,3.5 -3.6,3.5 -1.1,0 -3.2,-3.4 -3.2,-5.1 z",
    }

    # Missing FF Icons Batch
    icn["GR.IC.FF.INFANTRY"] = {
        "type": "path",
        "d": "M 25,50 L 175,150 M 175,50 L 25,150",
        "fill": False,
    }
    icn["GR.IC.FF.MOTORIZED"] = {"type": "path", "d": "M 100,60 100,140", "fill": False}
    icn["GR.IC.FF.RECONNAISSANCE"] = {
        "type": "path",
        "d": "M 140,80 60,120",
        "fill": False,
    }
    icn["GR.IC.FF.AMPHIBIOUS"] = {
        "type": "path",
        "d": "M 75,120 c 5,-5 10,-5 15,0 5,5 10,5 15,0 5,-5 10,-5 15,0 5,5 10,5 15,0",
        "fill": False,
    }
    icn["GR.IC.FF.AMPHIBIOUS"] = {
        "type": "path",
        "d": "M 80,100 C 80,120 120,120 120,100",
        "fill": False,
    }
    icn["GR.IC.FF.RECONNAISSANCE EQUIPMENT"] = icn["GR.IC.FF.RECONNAISSANCE"]
    icn["GR.IC.FF.SIGNAL"] = {
        "type": "path",
        "d": "M 100,80 l -20,40 l 40,0 z",
        "fill": False,
    }
    icn["GR.IC.FF.BROADCAST TRANSMITTER ANTENNA"] = icn["GR.IC.FF.SIGNAL"]
    icn["GR.IC.FF.SUPPLY"] = {
        "type": "path",
        "d": "M 60,100 l 80,0 M 100,60 l 0,80",
        "fill": False,
    }
    icn["GR.IC.FF.ANTITANK/ANTIARMOUR"] = {
        "type": "path",
        "d": "M 60,120 100,80 140,120",
        "fill": False,
    }

    icn["GR.IC.FF.NAVAL"] = {
        "type": "path",
        "d": "M 100,50 100,150",
        "fill": False,
    }

    for r in ["I", "II", "III", "IV", "V"]:
        icn[f"GR.IC.FF.CLASS {r}"] = text(r)

    icn["GR.IC.FF.MAIN GUN SYSTEM"] = {
        "type": "path",
        "d": "M 100,80 100,50",
        "fill": False,
    }

    missing_keys = [
        "BORDER PATROL",
        "CORPS SUPPORT",
        "CUSTOMS SERVICE",
        "DEPARTMENT OF JUSTICE (DOJ)",
        "DIRECTION FINDING",
        "EMERGENCY OPERATION",
        "FIELD ARTILLERY ROCKET",
        "HEADQUARTERS OR HEADQUARTERS ELEMENT",
        "HORSE",
        "INTERCEPT",
        "JAMMING",
        "LAW ENFORCEMENT",
        "MEDICAL",
        "MEDICAL CORPS",
        "MEDICAL THEATER",
        "MEDICAL TREATMENT FACILITY",
        "MILITARY POLICE",
        "PRISON",
        "SENSOR",
        "SOUND",
        "SUPPLY",
        "SUPPLY CORPS",
        "SUPPLY THEATER",
    ]
    for k in missing_keys:
        icn[f"GR.IC.FF.{k}"] = {
            "type": "path",
            "d": "M 100,100",
            "fill": False,
        }  # Dot placeholder

    icn["GR.I.FF.SATELLITE"] = {
        "type": "path",
        "d": "M 50,50 150,150",
        "fill": False,
    }

    # Emergency Management / Infrastructure / Activity Placeholders
    missing_em_keys = [
        "AC.IC.AFTERSHOCK",
        "AC.IC.AVALANCHE",
        "AC.IC.BANKING FINANCE AND INSURANCE INFRASTRUCTURE",
        "AC.IC.BIRD",
        "AC.IC.CHEMICAL AGENT",
        "AC.IC.CORROSIVE MATERIAL",
        "AC.IC.CRIMINAL.ACTIVITY.INCIDENT",
        "AC.IC.CRIMINAL.CIVIL DISTURBANCE",
        "AC.IC.DROUGHT",
        "AC.IC.EARTHQUAKE EPICENTER",
        "AC.IC.EMERGENCY PUBLIC INFORMATION CENTER",
        "AC.IC.EXPLOSIVE MATERIAL",
        "AC.IC.FIRE EVENT",
        "AC.IC.FIRE HYDRANT",
        "AC.IC.FIRE ORIGIN",
        "AC.IC.FLAMMABLE GAS",
        "AC.IC.FLAMMABLE LIQUID",
        "AC.IC.FLAMMABLE SOLID",
        "AC.IC.FLOOD",
        "AC.IC.HAZARDOUS MATERIALS INCIDENT",
        "AC.IC.HAZARDOUS WHEN WET",
        "AC.IC.HEALTH DEPARTMENT FACILITY",
        "AC.IC.HOT SPOT",
        "AC.IC.INSECT",
        "AC.IC.INVERSION",
        "AC.IC.LANDSLIDE",
        "AC.IC.MEDICAL FACILITIES OUTPATIENT",
        "AC.IC.MICROBIAL",
        "AC.IC.NON-FLAMMABLE GAS",
        "AC.IC.NON-REsIdENTIAL FIRE",
        "AC.IC.OPERATION/EMERGENCY MEDICAL OPERATION",
        "AC.IC.ORGANIC PEROXIDE",
        "AC.IC.OTHER WATER SUPPLY LOCATION",
        "AC.IC.OXIDIZER",
        "AC.IC.PHARMACY",
        "AC.IC.RADIOACTIVE MATERIAL",
        "AC.IC.REPTILE",
        "AC.IC.REsIdENTIAL FIRE",
        "AC.IC.RODENT",
        "AC.IC.SCHOOL FIRE",
        "AC.IC.SHOOTING",
        "AC.IC.SMOKE",
        "AC.IC.SPECIAL NEEDS FIRE",
        "AC.IC.SPONTANEOUSLY COMBUSTIBLE MATERIAL",
        "AC.IC.SUBSIDENCE",
        "AC.IC.TOXIC GAS",
        "AC.IC.TOXIC INFECTIOUS MATERIAL",
        "AC.IC.TRIAGE",
        "AC.IC.TSUNAMI",
        "AC.IC.UNEXPLODED ORDNANCE",
        "AC.IC.VOLCANIC ERUPTION",
        "AC.IC.VOLCANIC THREAT",
        "AC.IC.WILD FIRE",
        "AC.M1.COMMERCIAL",
        "AC.M1.EMERGENCY",
        "AC.M1.EMERGENCY COLLECTION EVACUATION POINT",
        "AC.M1.EMERGENCY INCIDENT COMMAND CENTER",
        "AC.M1.EMERGENCY OPERATIONS CENTER",
        "AC.M1.EMERGENCY SHELTER",
        "AC.M1.EMERGENCY STAGING AREA",
        "AC.M1.GENERATION STATION",
        "AC.M1.MILITARY ARMORY",
        "AC.M1.PRODUCTION",
        "AC.M1.RETAIL",
        "AC.M1.RIOT",
        "AC.M1.THREAT",
        "ATMOSPHERIC.IC.DRIZZLE.INTERMITTENT LIGHT",
        "ATMOSPHERIC.IC.DUST OR SAND.LIGHT TO MODERATE",
        "ATMOSPHERIC.IC.FOG.SKY OBSCURED",
        "ATMOSPHERIC.IC.HAIL.LIGHT NOT ASSOCIATED WITH THUNDER",
        "ATMOSPHERIC.IC.RAIN.INTERMITTENT LIGHT",
        "ATMOSPHERIC.IC.SNOW.INTERMITTENT LIGHT",
        "ATMOSPHERIC.IC.STORMS.FUNNEL CLOUD (TORNADO/WATERSPOUT)",
        "ATMOSPHERIC.IC.STORMS.THUNDERSTORM LIGHT TO MODERATE - WITH HAIL",
        "ATMOSPHERIC.IC.TROPICAL STORM SYSTEMS.TROPICAL STORM",
        "GR.EQ.CIVILIAN VEHICLE.MULTIPLE PASSENGER VEHICLE",
        "GR.EQ.CIVILIAN VEHICLE.UTILITY VEHICLE",
        "GR.EQ.SENSOR",
        "GR.EQ.TRAIN LOCOMOTIVE",
        "GR.IC.HOSPITAL SHIP",
        "GR.I.FF.CIVILIAN ROTARY WING",
        "GR.IN.IC.ADULT DAY CARE",
        "GR.IN.IC.AGRICULTURAL LABORATORY",
        "GR.IN.IC.AGRICULTURE AND FOOD INFRASTRUCTURE",
        "GR.IN.IC.AIR TRAFFIC CONTROL FACILITY",
        "GR.IN.IC.ANIMAL FEEDLOT",
        "GR.IN.IC.ATM",
        "GR.IN.IC.BANK",
        "GR.IN.IC.BASE",
        "GR.IN.IC.BRIDGE",
        "GR.IN.IC.BULLION STORAGE",
        "GR.IN.IC.CHEMICAL PLANT",
        "GR.IN.IC.CHILD DAY CARE",
        "GR.IN.IC.COLLEGE/UNIVERSITY",
        "GR.IN.IC.COMMERCIAL INFRASTRUCTURE",
        "GR.IN.IC.CONTAMINATED HAZARDOUS WASTE SITE",
        "GR.IN.IC.CONTROL VALVE",
        "GR.IN.IC.DAM",
        "GR.IN.IC.DISCHARGE OUTFALL",
        "GR.IN.IC.EDUCATIONAL FACILITIES INFRASTRUCTURE",
        "GR.IN.IC.ELDER CARE",
        "GR.IN.IC.ELECTRIC POWER",
        "GR.IN.IC.ELECTRIC POWER NUCLEAR",
        "GR.IN.IC.ENCLOSED FACITLITY (PUBLIC VENUE)",
        "GR.IN.IC.FARM/RANCH",
        "GR.IN.IC.FEDERAL RESERVE BANK",
        "GR.IN.IC.FINANCIAL EXCHANGE",
        "GR.IN.IC.FINANCIAL SERVICES, OTHER",
        "GR.IN.IC.FIREARMS MANUFACTURER",
        "GR.IN.IC.FIREARMS RETAILER",
        "GR.IN.IC.GOVERNMENT SITE INFRASTRUCTURE",
        "GR.IN.IC.GRAIN STORAGE",
        "GR.IN.IC.GROUND WATER WELL",
        "GR.IN.IC.HAZARDOUS MATERIAL PRODUCTION",
        "GR.IN.IC.HAZARDOUS MATERIAL STORAGE",
        "GR.IN.IC.HELICOPTER LANDING SITE",
        "GR.IN.IC.INDUSTRIAL SITE",
        "GR.IN.IC.LANDFILL",
        "GR.IN.IC.MILITARY INFRASTRUCTURE",
        "GR.IN.IC.NATURAL GAS FACILITY",
        "GR.IN.IC.OPEN FACILITY (OPEN VENUE)",
        "GR.IN.IC.PHARMACEUTICAL MANUFACTURER",
        "GR.IN.IC.POST OFFICE",
        "GR.IN.IC.POSTAL DISTRIBUTION CENTER",
        "GR.IN.IC.POSTAL SERVICE INFRASTRUCTURE",
        "GR.IN.IC.PROPANE FACILITY",
        "GR.IN.IC.PUBLIC VENUES INFRASTRUCTURE",
        "GR.IN.IC.PUMPING STATION",
        "GR.IN.IC.RECREATIONAL AREA",
        "GR.IN.IC.RELIGIOUS INSTITUTION",
        "GR.IN.IC.RESERVOIR",
        "GR.IN.IC.REST STOP",
        "GR.IN.IC.SCHOOL",
        "GR.IN.IC.SPECIAL NEEDS INFRASTRUCTURE",
        "GR.IN.IC.STORAGE TOWER",
        "GR.IN.IC.SURFACE WATER INTAKE",
        "GR.IN.IC.TELECOMMUNICATIONS",
        "GR.IN.IC.TELECOMMUNICATIONS INFRASTRUCTURE",
        "GR.IN.IC.TELECOMMUNICATIONS TOWER",
        "GR.IN.IC.TOLL FACILITY",
        "GR.IN.IC.TOXIC RELEASE INVENTORY",
        "GR.IN.IC.TRAFFIC INSPECTION FACILITY",
        "GR.IN.IC.TRANSPORTATION INFRASTRUCTURE LOCK",
        "GR.IN.IC.TRANSPORTATION INFRASTRUCTURE SHIP ANCHORAGE",
        "GR.IN.IC.TUNNEL",
        "GR.IN.IC.WASTEWATER TREATMENT FACILITY",
        "ST.IC.BOMB",
        "ST.IC.DEMONSTRATION",
        "ST.IC.EXPLOSION",
        "ST.IC.FOOD DISTRIBUTION",
        "ST.IC.GROUP",
        "ST.IC.HIJACKING (AIRPLANE)",
        "ST.IC.HIJACKING (BOAT)",
        "ST.IC.KNOWN INSURGENT VEHICLE",
        "ST.IC.POISONING",
        "ST.M1.ACCIDENT",
        "ST.M1.HIJACKING/HIJACKED",
        "ST.M1.INCIDENT",
        "ST.M1.LOOT",
        "ST.IC.ARREST",
        "ST.IC.BLACK LIST LOCATION",
        "ST.IC.BOOBY TRAP",
        "ST.IC.DRIVE-BY SHOOTING",
        "ST.IC.DRUG RELATED ACTIVITIES",
        "ST.IC.EXTORTION",
        "ST.IC.GRAFFITI",
        "ST.IC.GRAY LIST LOCATION",
        "ST.IC.INDIVIDUAL",
        "ST.IC.INTERNAL SECURITY FORCE",
        "ST.IC.KILLING VICTIM",
        "ST.IC.MINE LAYING",
        "ST.IC.PATROLLING",
        "ST.IC.PSYCHOLOGICAL OPERATIONS",
        "ST.IC.RADIO AND TELEVISION PSYCHOLOGICAL OPERATIONS",
        "ST.IC.SAFE HOUSE",
        "ST.IC.SEARCHING",
        "ST.IC.SNIPING",
        "ST.IC.SPY",
        "ST.IC.VANDALISM/LOOT/RANSACK/PLUNDER/SACK",
        "ST.IC.WHITE LIST LOCATION",
        "ST.M1.COERCED/IMPRESSED",
        "ST.M1.DRUG",
        "ST.M1.HOUSE-TO-HOUSE",
        "ST.M1.KIDNAPPING",
        "ST.M1.WILLING",
        "ST.M1.WRITTEN PSYCHOLOGICAL OPERATIONS",
        "AIR.MISSILE.IC.BOMB",
        "AR.I.FF.CIVILIAN ROTARY WING",
        "GR.EQ.HOWITZER",
        "GR.EQ.MORTAR",
        "GR.EQ.MULTIPLE ROCKET LAUNCHER",
        "GR.IC.ELECTRONIC WARFARE",
    ]
    for k in missing_em_keys:
        icn[k] = icn.get(k, {"type": "path", "d": "M 50,50 150,150", "fill": False})

    for key, value in icn.items():
        if key in iconParts:
            print(f"Override of: {key}")

        defaultProperties(value, iconColor)
        iconParts[key] = value
