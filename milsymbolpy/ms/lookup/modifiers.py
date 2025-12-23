from typing import Optional, Dict
from .milstd2525modifier import MilStd2525Modifier


class MilStd2525Sector1Modifiers:
    """Encapsulates Table A-IX (Common) and Table A-XXIV (Land Specific) Sector 1 Modifiers."""

    _registry: Dict[str, MilStd2525Modifier] = {
        # --- Common Sector 1 Modifiers (Table A-IX) ---
        "100": MilStd2525Modifier(
            "Unmanned Aircraft (UA/UAV/UAS/RPV)", "100", "E", "Mobility"
        ),
        "101": MilStd2525Modifier("Robotic", "101", "E", "Mobility"),
        "102": MilStd2525Modifier(
            "Fixed Wing", "102", "E", "Mobility", "Not used by USAF"
        ),
        "103": MilStd2525Modifier("Rotary Wing", "103", "E", "Mobility"),
        "104": MilStd2525Modifier("Tilt-Rotor", "104", "E", "Mobility"),
        "105": MilStd2525Modifier(
            "VSTOL/VTOL or Helicopter Equipped", "105", "E", "Mobility"
        ),
        "106": MilStd2525Modifier("Attack or Attack/Strike", "106", "E", "Capability"),
        "107": MilStd2525Modifier("Armored", "107", "E", "Capability"),
        "108": MilStd2525Modifier(
            "Ballistic Missile/Ballistic Missile Defense Shooter",
            "108",
            "E",
            "Capability",
        ),
        "109": MilStd2525Modifier("Bridge/Bridging", "109", "E", "Capability"),
        "110": MilStd2525Modifier("Cargo", "110", "E", "Capability"),
        "111": MilStd2525Modifier("Utility", "111", "E", "Capability"),
        "112": MilStd2525Modifier("Light", "112", "E", "Capability"),
        "113": MilStd2525Modifier("Medium", "113", "E", "Capability"),
        "114": MilStd2525Modifier("Heavy", "114", "E", "Capability"),
        "115": MilStd2525Modifier("Cyberspace", "115", "E", "Capability"),
        "116": MilStd2525Modifier("Command Post Node", "116", "E", "Capability"),
        "117": MilStd2525Modifier("Joint Network Node", "117", "E", "Capability"),
        "118": MilStd2525Modifier("Retransmission Site", "118", "E", "Capability"),
        "119": MilStd2525Modifier("Brigade", "119", "E", "Support Level"),
        "120": MilStd2525Modifier("Close Protection", "120", "E", "Capability"),
        "121": MilStd2525Modifier("Combat", "121", "E", "Capability"),
        "122": MilStd2525Modifier("Command and Control", "122", "E", "Capability"),
        "123": MilStd2525Modifier("Crowd and Riot Control", "123", "E", "Capability"),
        "124": MilStd2525Modifier(
            "Explosive Ordnance Disposal", "124", "E", "Capability"
        ),
        "125": MilStd2525Modifier(
            "Intelligence Surveillance Reconnaissance", "125", "E", "Capability"
        ),
        "126": MilStd2525Modifier("Maintenance", "126", "E", "Capability"),
        "127": MilStd2525Modifier("Medevac/Medic/Medical", "127", "E", "Capability"),
        "128": MilStd2525Modifier("Search and Rescue", "128", "E", "Capability"),
        "129": MilStd2525Modifier("Security", "129", "E", "Capability"),
        "130": MilStd2525Modifier("Sniper", "130", "E", "Capability"),
        "131": MilStd2525Modifier(
            "Special Operations Forces", "131", "E", "Capability"
        ),
        "132": MilStd2525Modifier(
            "Special Weapons and Tactics (SWAT)", "132", "E", "Capability"
        ),
        "133": MilStd2525Modifier("Guided Missile", "133", "E", "Capability"),
        "134": MilStd2525Modifier("Other Guided Missile", "134", "E", "Capability"),
        "135": MilStd2525Modifier(
            "Petroleum/Petroleum Oil and Lubricants", "135", "E", "Capability"
        ),
        "136": MilStd2525Modifier("Water", "136", "E", "Capability"),
        "137": MilStd2525Modifier("Weapon or Weapons", "137", "E", "Capability"),
        "138": MilStd2525Modifier("Chemical", "138", "E", "CBRN"),
        "140": MilStd2525Modifier("Radiological", "140", "E", "CBRN"),
        "141": MilStd2525Modifier("Nuclear", "141", "E", "CBRN"),
        "142": MilStd2525Modifier("Decontamination", "142", "E", "CBRN"),
        "143": MilStd2525Modifier("Civilian", "143", "E", "Organization"),
        "144": MilStd2525Modifier(
            "Government Organization", "144", "E", "Organization"
        ),
        "156": MilStd2525Modifier("Command", "156", "E", "Support Level"),
        "157": MilStd2525Modifier("Company", "157", "E", "Support Level"),
        "158": MilStd2525Modifier("Platoon/Detachment", "158", "E", "Support Level"),
        "159": MilStd2525Modifier("Regiment Group", "159", "E", "Support Level"),
        "160": MilStd2525Modifier("Section", "160", "E", "Support Level"),
        "161": MilStd2525Modifier("Squad", "161", "E", "Support Level"),
        "162": MilStd2525Modifier("Team/Crew", "162", "E", "Support Level"),
        "163": MilStd2525Modifier("Battalion", "163", "E", "Support Level"),
        "164": MilStd2525Modifier("Directed Energy", "164", "E", "Capability"),
        # --- Land Unit Specific Sector 1 Modifiers (Table A-XXIV) ---
        "00": MilStd2525Modifier("Unspecified", "00", "E"),
        "01": MilStd2525Modifier(
            "Tactical Satellite Communications", "01", "E", "Capability"
        ),
        "02": MilStd2525Modifier("Area", "02", "E", "Capability"),
        "04": MilStd2525Modifier("Biological", "04", "E", "Capability"),
        "05": MilStd2525Modifier("Border", "05", "E", "Capability"),
        "11": MilStd2525Modifier(
            "Communications Contingency Package", "11", "E", "Capability"
        ),
        "12": MilStd2525Modifier("Construction", "12", "E", "Capability"),
        "13": MilStd2525Modifier(
            "Cross Cultural Communication", "13", "E", "Capability"
        ),
        "16": MilStd2525Modifier("Detention", "16", "E", "Capability"),
        "17": MilStd2525Modifier("Direct Communications", "17", "E", "Capability"),
        "18": MilStd2525Modifier("Diving", "18", "E", "Capability"),
        "19": MilStd2525Modifier("Division", "19", "E", "Capability"),
        "20": MilStd2525Modifier("Dog", "20", "E", "Capability"),
        "21": MilStd2525Modifier("Drilling", "21", "E", "Capability"),
        "22": MilStd2525Modifier("Electro-Optical", "22", "E", "Capability"),
        "25": MilStd2525Modifier("Fire Direction Center", "25", "E", "Capability"),
        "26": MilStd2525Modifier("Force", "26", "E", "Capability"),
        "27": MilStd2525Modifier("Forward", "27", "E", "Capability"),
        "28": MilStd2525Modifier("Ground Station Module", "28", "E", "Capability"),
        "29": MilStd2525Modifier("Landing Support", "29", "E", "Capability"),
        "32": MilStd2525Modifier("Meteorological", "32", "E", "Capability"),
        "34": MilStd2525Modifier("Missile", "34", "E", "Capability"),
        "35": MilStd2525Modifier("Mobile Advisor and Support", "35", "E", "Capability"),
        "36": MilStd2525Modifier(
            "Mobile Subscriber Equipment", "36", "E", "Capability"
        ),
        "37": MilStd2525Modifier("Mobility Support", "37", "E", "Capability"),
        "39": MilStd2525Modifier("Multinational", "39", "E", "Capability"),
        "40": MilStd2525Modifier(
            "Multinational Specialized Unit", "40", "E", "Capability"
        ),
        "41": MilStd2525Modifier("Multiple Rocket Launcher", "41", "E", "Capability"),
        "42": MilStd2525Modifier("NATO Medical Role 1", "42", "E", "Capability"),
        "43": MilStd2525Modifier("NATO Medical Role 2", "43", "E", "Capability"),
        "44": MilStd2525Modifier("NATO Medical Role 3", "44", "E", "Capability"),
        "45": MilStd2525Modifier("NATO Medical Role 4", "45", "E", "Capability"),
        "46": MilStd2525Modifier("Naval", "46", "E", "Capability"),
        "47": MilStd2525Modifier(
            "Unmanned Aerial Systems (UAS)", "47", "E", "Capability"
        ),
        "49": MilStd2525Modifier("Operations", "49", "E", "Capability"),
        "50": MilStd2525Modifier("Radar", "50", "E", "Capability"),
        "51": MilStd2525Modifier(
            "Radio Frequency Identification (RFID) Interrogator/Sensor",
            "51",
            "E",
            "Capability",
        ),
        "55": MilStd2525Modifier("Sensor", "55", "E", "Capability"),
        "57": MilStd2525Modifier("Signal Intelligence", "57", "E", "Capability"),
        "59": MilStd2525Modifier("Single Rocket Launcher", "59", "E", "Capability"),
        "60": MilStd2525Modifier("Smoke", "60", "E", "Capability"),
        "62": MilStd2525Modifier("Sound Ranging", "62", "E", "Capability"),
        "65": MilStd2525Modifier("Survey", "65", "E", "Capability"),
        "66": MilStd2525Modifier("Tactical Exploitation", "66", "E", "Capability"),
        "67": MilStd2525Modifier("Target Acquisition", "67", "E", "Capability"),
        "68": MilStd2525Modifier("Topographic/Geospatial", "68", "E", "Capability"),
        "70": MilStd2525Modifier(
            "Video Imagery (Combat Camera)", "70", "E", "Capability"
        ),
        "71": MilStd2525Modifier("Mobility Assault", "71", "E", "Capability"),
        "72": MilStd2525Modifier("Amphibious Warfare Ship", "72", "E", "Capability"),
        "73": MilStd2525Modifier("Load Handling System", "73", "E", "Capability"),
        "74": MilStd2525Modifier("Palletized Load System", "74", "E", "Capability"),
        "77": MilStd2525Modifier("Support", "77", "E", "Capability"),
        "79": MilStd2525Modifier(
            "Route, Reconnaissance, and Clearance", "79", "E", "Capability"
        ),
        "84": MilStd2525Modifier("Assault", "84", "E", "Capability"),
        "86": MilStd2525Modifier(
            "Criminal Investigation Division", "86", "E", "Capability"
        ),
        "87": MilStd2525Modifier("Digital", "87", "E", "Capability"),
        "88": MilStd2525Modifier(
            "Network or Network Operations", "88", "E", "Capability"
        ),
        "89": MilStd2525Modifier(
            "Airfield, Aerial Port of Debarkation, or Aerial Port of Embarkation",
            "89",
            "E",
            "Capability",
        ),
        "90": MilStd2525Modifier("Pipeline", "90", "E", "Capability"),
        "91": MilStd2525Modifier("Postal", "91", "E", "Capability"),
        "94": MilStd2525Modifier("Theater", "94", "E", "Capability"),
        "95": MilStd2525Modifier("Army or Theater Army", "95", "E", "Capability"),
        "96": MilStd2525Modifier("Corps", "96", "E", "Capability"),
        "98": MilStd2525Modifier(
            "Headquarters or headquarters staff element", "98", "E", "Capability"
        ),
        "99": MilStd2525Modifier("Multi-Domain Operations", "99", "E", "Capability"),
    }

    def __getitem__(self, key: str) -> Optional[MilStd2525Modifier]:
        return self._registry.get(key)


class MilStd2525Sector2Modifiers:
    """Encapsulates Table A-X (Common) and Table A-XXV (Land Specific) Sector 2 Modifiers."""

    _registry: Dict[str, MilStd2525Modifier] = {
        # --- Common Sector 2 Modifiers (Table A-X) ---
        "100": MilStd2525Modifier("Airborne", "100", "E", "Mobility"),
        "101": MilStd2525Modifier("Bicycle Equipped", "101", "E", "Mobility"),
        "102": MilStd2525Modifier("Railroad/Railway", "102", "E", "Capability"),
        "103": MilStd2525Modifier("Ski", "103", "E", "Mobility"),
        "104": MilStd2525Modifier("Tracked", "104", "E", "Mobility"),
        "105": MilStd2525Modifier(
            "Wheeled (Limited Cross Country)", "105", "E", "Mobility"
        ),
        "106": MilStd2525Modifier("Wheeled X (Cross Country)", "106", "E", "Mobility"),
        "107": MilStd2525Modifier("Fixed Wing", "107", "E", "Mobility"),
        "108": MilStd2525Modifier("Rotary Wing", "108", "E", "Mobility"),
        "109": MilStd2525Modifier("Robotic", "109", "E", "Mobility"),
        "110": MilStd2525Modifier("Autonomous Control", "110", "E", "Capability"),
        "111": MilStd2525Modifier("Remotely Piloted", "111", "E", "Capability"),
        "112": MilStd2525Modifier("Expendable", "112", "E", "Capability"),
        "113": MilStd2525Modifier("Mountain", "113", "E", "Capability"),
        "114": MilStd2525Modifier("Long Range", "114", "E", "Capability"),
        "115": MilStd2525Modifier("Medium Range", "115", "E", "Capability"),
        "116": MilStd2525Modifier("Short Range", "116", "E", "Capability"),
        "117": MilStd2525Modifier("Close Range", "117", "E", "Capability"),
        "118": MilStd2525Modifier("Heavy", "118", "E", "Capability"),
        "119": MilStd2525Modifier("Medium", "119", "E", "Capability"),
        "120": MilStd2525Modifier("Light and Medium", "120", "E", "Capability"),
        "121": MilStd2525Modifier("Light", "121", "E", "Capability"),
        "122": MilStd2525Modifier("Cyberspace", "122", "E", "Capability"),
        "123": MilStd2525Modifier(
            "Security Force Assistance", "123", "E", "Capability"
        ),
        "124": MilStd2525Modifier("Medical Bed", "124", "E", "Capability"),
        "125": MilStd2525Modifier("Multifunctional", "125", "E", "Capability"),
        # --- Land Unit Specific Sector 2 Modifiers (Table A-XXV) ---
        "00": MilStd2525Modifier("Unspecified", "00", "E"),
        "02": MilStd2525Modifier("Arctic", "02", "E", "Mobility"),
        "03": MilStd2525Modifier("Battle Damage Repair", "03", "E", "Capability"),
        "05": MilStd2525Modifier("Casualty Staging", "05", "E", "Capability"),
        "06": MilStd2525Modifier("Clearing", "06", "E", "Capability"),
        "08": MilStd2525Modifier("Control", "08", "E", "Capability"),
        "09": MilStd2525Modifier("Decontamination", "09", "E", "Capability"),
        "10": MilStd2525Modifier("Demolition", "10", "E", "Capability"),
        "11": MilStd2525Modifier("Dental", "11", "E", "Capability"),
        "12": MilStd2525Modifier("Digital", "12", "E", "Capability"),
        "13": MilStd2525Modifier(
            "Enhanced Position Location Reporting System (EPLRS)",
            "13",
            "E",
            "Capability",
        ),
        "16": MilStd2525Modifier("High Altitude", "16", "E", "Capability"),
        "17": MilStd2525Modifier("Intermodal", "17", "E", "Capability"),
        "18": MilStd2525Modifier("Intensive Care", "18", "E", "Capability"),
        "20": MilStd2525Modifier("Laboratory", "20", "E", "Capability"),
        "21": MilStd2525Modifier("Launcher", "21", "E", "Capability"),
        "23": MilStd2525Modifier("Low Altitude", "23", "E", "Capability"),
        "25": MilStd2525Modifier("Medium Altitude", "25", "E", "Capability"),
        "28": MilStd2525Modifier("High to Medium Altitude", "28", "E", "Capability"),
        "29": MilStd2525Modifier("Multi-Channel", "29", "E", "Capability"),
        "30": MilStd2525Modifier("Optical (Flash)", "30", "E", "Capability"),
        "31": MilStd2525Modifier("Pack Animal", "31", "E", "Capability"),
        "32": MilStd2525Modifier(
            "Patient Evacuation Coordination", "32", "E", "Capability"
        ),
        "33": MilStd2525Modifier("Preventive Maintenance", "33", "E", "Capability"),
        "34": MilStd2525Modifier("Psychological", "34", "E", "Capability"),
        "35": MilStd2525Modifier("Radio Relay Line of Sight", "35", "E", "Capability"),
        "37": MilStd2525Modifier(
            "Recovery (Unmanned Systems)", "37", "E", "Capability"
        ),
        "38": MilStd2525Modifier("Recovery (Maintenance)", "38", "E", "Capability"),
        "39": MilStd2525Modifier("Rescue Coordination Center", "39", "E", "Capability"),
        "40": MilStd2525Modifier("Riverine", "40", "E", "Mobility"),
        "41": MilStd2525Modifier("Single Channel", "41", "E", "Capability"),
        "44": MilStd2525Modifier("Strategic", "44", "E", "Capability"),
        "45": MilStd2525Modifier("Support", "45", "E", "Capability"),
        "46": MilStd2525Modifier("Tactical", "46", "E", "Capability"),
        "47": MilStd2525Modifier("Towed", "47", "E", "Mobility"),
        "48": MilStd2525Modifier("Troop", "48", "E", "Capability"),
        "49": MilStd2525Modifier(
            "Vertical or Short Take-Off and Landing (VTOL/VSTOL)", "49", "E", "Mobility"
        ),
        "50": MilStd2525Modifier("Veterinary", "50", "E", "Capability"),
        "52": MilStd2525Modifier("High to Low Altitude", "52", "E", "Capability"),
        "53": MilStd2525Modifier("Medium to Low Altitude", "53", "E", "Capability"),
        "54": MilStd2525Modifier("Attack", "54", "E", "Capability"),
        "55": MilStd2525Modifier("Refuel", "55", "E", "Capability"),
        "56": MilStd2525Modifier("Utility", "56", "E", "Capability"),
        "57": MilStd2525Modifier("Combat Search and Rescue", "57", "E", "Capability"),
        "58": MilStd2525Modifier("Guerrilla", "58", "E", "Capability"),
        "59": MilStd2525Modifier("Air Assault", "59", "E", "Mobility"),
        "60": MilStd2525Modifier("Amphibious", "60", "E", "Mobility"),
        "61": MilStd2525Modifier("Very Heavy", "61", "E", "Capability"),
        "62": MilStd2525Modifier("Supply", "62", "E", "Capability"),
        "64": MilStd2525Modifier("Navy Barge, Self-Propelled", "64", "E", "Mobility"),
        "65": MilStd2525Modifier(
            "Navy Barge, Not Self-Propelled", "65", "E", "Mobility"
        ),
        "66": MilStd2525Modifier("Launch", "66", "E", "Mobility"),
        "67": MilStd2525Modifier("Landing Craft", "67", "E", "Mobility"),
        "68": MilStd2525Modifier("Landing Ship", "68", "E", "Mobility"),
        "69": MilStd2525Modifier("Service Craft/Yard", "69", "E", "Mobility"),
        "70": MilStd2525Modifier("Tug Harbor", "70", "E", "Mobility"),
        "71": MilStd2525Modifier("Ocean Going Tug Boat", "71", "E", "Mobility"),
        "72": MilStd2525Modifier(
            "Surface Deployment and Distribution", "72", "E", "Capability"
        ),
        "73": MilStd2525Modifier("Noncombatant Generic Vessel", "73", "E", "Mobility"),
        "74": MilStd2525Modifier("Composite", "74", "E", "Capability"),
        "75": MilStd2525Modifier("Shelter", "75", "E", "Capability"),
        "81": MilStd2525Modifier("Surgical", "81", "E", "Capability"),
        "82": MilStd2525Modifier("Blood", "82", "E", "Capability"),
        "83": MilStd2525Modifier(
            "Combat and Operational Stress Control", "83", "E", "Capability"
        ),
        "84": MilStd2525Modifier("Jamming", "84", "E", "Capability"),
        "86": MilStd2525Modifier("Optometry", "86", "E", "Capability"),
        "87": MilStd2525Modifier("Preventive Medicine", "87", "E", "Capability"),
        "89": MilStd2525Modifier("Air Defense", "89", "E", "Capability"),
    }

    def __getitem__(self, key: str) -> Optional[MilStd2525Modifier]:
        return self._registry.get(key)
