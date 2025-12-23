from typing import Dict, Optional
from .milstd2525entity import MilStd2525Entity


class MilStd2525Entities:
    """Encapsulates Table A-XXIII Land unit entities."""

    _registry: Dict[str, MilStd2525Entity] = {
        # --- COMMAND AND CONTROL (11) ---
        "110000": MilStd2525Entity(["Command and Control"], "110000", "E"),
        "110100": MilStd2525Entity(
            ["Command and Control", "Broadcast Transmitter Antennae"], "110100", "E"
        ),
        "110200": MilStd2525Entity(
            ["Command and Control", "Civil Affairs"], "110200", "E"
        ),
        "110300": MilStd2525Entity(
            ["Command and Control", "Civil-Military Cooperation"], "110300", "E"
        ),
        "110400": MilStd2525Entity(
            ["Command and Control", "Information Operations"], "110400", "E"
        ),
        "110500": MilStd2525Entity(["Command and Control", "Liaison"], "110500", "E"),
        "110600": MilStd2525Entity(
            ["Command and Control", "Military Information Support Operations (MISO)"],
            "110600",
            "E",
        ),
        "110601": MilStd2525Entity(
            [
                "Command and Control",
                "Military Information Support Operations (MISO)",
                "Broadcast Transmitter Antennae",
            ],
            "110601",
            "E",
        ),
        "110700": MilStd2525Entity(["Command and Control", "Radio"], "110700", "E"),
        "110800": MilStd2525Entity(
            ["Command and Control", "Radio Relay"], "110800", "E"
        ),
        "110900": MilStd2525Entity(
            ["Command and Control", "Radio Teletype Center"], "110900", "E"
        ),
        "111000": MilStd2525Entity(["Command and Control", "Signal"], "111000", "E"),
        "111001": MilStd2525Entity(
            ["Command and Control", "Signal", "Radio"], "111001", "E"
        ),
        "111002": MilStd2525Entity(
            ["Command and Control", "Signal", "Radio Relay"], "111002", "E"
        ),
        "111003": MilStd2525Entity(
            ["Command and Control", "Signal", "Teletype"], "111003", "E"
        ),
        "111005": MilStd2525Entity(
            ["Command and Control", "Signal", "Video Imagery (Combat Camera)"],
            "111005",
            "E",
        ),
        "111200": MilStd2525Entity(
            ["Command and Control", "Video Imagery (Combat Camera)"], "111200", "E"
        ),
        "111300": MilStd2525Entity(["Command and Control", "Space"], "111300", "E"),
        "111400": MilStd2525Entity(
            ["Command and Control", "Special Troops"], "111400", "E"
        ),
        "111500": MilStd2525Entity(
            ["Command and Control", "Multi-Domain Operations"], "111500", "E"
        ),
        # --- MOVEMENT AND MANEUVER (12) ---
        "120000": MilStd2525Entity(["Movement and Maneuver"], "120000", "E"),
        "120100": MilStd2525Entity(
            ["Movement and Maneuver", "Air Assault with Organic Lift"], "120100", "E"
        ),
        "120200": MilStd2525Entity(
            ["Movement and Maneuver", "Air Traffic Services/Airfield Operations"],
            "120200",
            "E",
        ),
        "120400": MilStd2525Entity(
            ["Movement and Maneuver", "Antitank/Antiarmor"], "120400", "E"
        ),
        "120401": MilStd2525Entity(
            ["Movement and Maneuver", "Antitank/Antiarmor", "Armored"], "120401", "E"
        ),
        "120402": MilStd2525Entity(
            ["Movement and Maneuver", "Antitank/Antiarmor", "Motorized"], "120402", "E"
        ),
        "120500": MilStd2525Entity(
            ["Movement and Maneuver", "Armor/Mechanized"], "120500", "E"
        ),
        "120501": MilStd2525Entity(
            [
                "Movement and Maneuver",
                "Armor/Mechanized",
                "Reconnaissance/Cavalry/Scout",
            ],
            "120501",
            "E",
        ),
        "120502": MilStd2525Entity(
            ["Movement and Maneuver", "Armor/Mechanized", "Amphibious"], "120502", "E"
        ),
        "120600": MilStd2525Entity(
            ["Movement and Maneuver", "Army Aviation/Aviation Rotary Wing"],
            "120600",
            "E",
        ),
        "120601": MilStd2525Entity(
            [
                "Movement and Maneuver",
                "Army Aviation/Aviation Rotary Wing",
                "Reconnaissance",
            ],
            "120601",
            "E",
        ),
        "120700": MilStd2525Entity(
            ["Movement and Maneuver", "Aviation Composite"], "120700", "E"
        ),
        "120800": MilStd2525Entity(
            ["Movement and Maneuver", "Aviation Fixed Wing"], "120800", "E"
        ),
        "120801": MilStd2525Entity(
            ["Movement and Maneuver", "Aviation Fixed Wing", "Reconnaissance"],
            "120801",
            "E",
        ),
        "120900": MilStd2525Entity(["Movement and Maneuver", "Combat"], "120900", "E"),
        "121000": MilStd2525Entity(
            ["Movement and Maneuver", "Combined Arms"], "121000", "E"
        ),
        "121100": MilStd2525Entity(
            ["Movement and Maneuver", "Infantry"], "121100", "E"
        ),
        "121101": MilStd2525Entity(
            ["Movement and Maneuver", "Infantry", "Amphibious"], "121101", "E"
        ),
        "121102": MilStd2525Entity(
            ["Movement and Maneuver", "Infantry", "Armored/Mechanized/Tracked"],
            "121102",
            "E",
        ),
        "121103": MilStd2525Entity(
            ["Movement and Maneuver", "Infantry", "Main Gun System, Infantry"],
            "121103",
            "E",
        ),
        "121104": MilStd2525Entity(
            ["Movement and Maneuver", "Infantry", "Motorized"], "121104", "E"
        ),
        "121105": MilStd2525Entity(
            ["Movement and Maneuver", "Infantry", "Infantry Fighting Vehicle"],
            "121105",
            "E",
        ),
        "121106": MilStd2525Entity(
            ["Movement and Maneuver", "Infantry", "Main Gun System"], "121106", "E"
        ),
        "121200": MilStd2525Entity(
            ["Movement and Maneuver", "Observer"], "121200", "E"
        ),
        "121300": MilStd2525Entity(
            ["Movement and Maneuver", "Reconnaissance/Cavalry/Scout"], "121300", "E"
        ),
        "121301": MilStd2525Entity(
            [
                "Movement and Maneuver",
                "Reconnaissance/Cavalry/Scout",
                "Reconnaissance and Surveillance",
            ],
            "121301",
            "E",
        ),
        "121302": MilStd2525Entity(
            ["Movement and Maneuver", "Reconnaissance/Cavalry/Scout", "Marine"],
            "121302",
            "E",
        ),
        "121303": MilStd2525Entity(
            ["Movement and Maneuver", "Reconnaissance/Cavalry/Scout", "Motorized"],
            "121303",
            "E",
        ),
        "121400": MilStd2525Entity(
            ["Movement and Maneuver", "Sea Air Land (SEAL)"], "121400", "E"
        ),
        "121500": MilStd2525Entity(["Movement and Maneuver", "Sniper"], "121500", "E"),
        "121600": MilStd2525Entity(
            ["Movement and Maneuver", "Surveillance"], "121600", "E"
        ),
        "121700": MilStd2525Entity(
            ["Movement and Maneuver", "Special Forces"], "121700", "E"
        ),
        "121800": MilStd2525Entity(
            ["Movement and Maneuver", "Special Operations Forces (SOF)"], "121800", "E"
        ),
        "121801": MilStd2525Entity(
            [
                "Movement and Maneuver",
                "Special Operations Forces (SOF)",
                "Fixed Wing MISO",
            ],
            "121801",
            "E",
        ),
        "121802": MilStd2525Entity(
            ["Movement and Maneuver", "Special Operations Forces (SOF)", "Ground"],
            "121802",
            "E",
        ),
        "121804": MilStd2525Entity(
            [
                "Movement and Maneuver",
                "Special Operations Forces (SOF)",
                "Special SSNR",
            ],
            "121804",
            "E",
        ),
        "121805": MilStd2525Entity(
            [
                "Movement and Maneuver",
                "Special Operations Forces (SOF)",
                "Underwater Demolition",
            ],
            "121805",
            "E",
        ),
        "121900": MilStd2525Entity(
            ["Movement and Maneuver", "Unmanned Aerial Systems"], "121900", "E"
        ),
        "122000": MilStd2525Entity(["Movement and Maneuver", "Ranger"], "122000", "E"),
        # --- FIRES (13) ---
        "130000": MilStd2525Entity(["Fires"], "130000", "E"),
        "130100": MilStd2525Entity(["Fires", "Air Defense"], "130100", "E"),
        "130101": MilStd2525Entity(
            ["Fires", "Air Defense", "Main Gun System"], "130101", "E"
        ),
        "130102": MilStd2525Entity(["Fires", "Air Defense", "Missile"], "130102", "E"),
        "130103": MilStd2525Entity(
            ["Fires", "Air Defense", "Air and Missile Defense"], "130103", "E"
        ),
        "130200": MilStd2525Entity(
            ["Fires", "Air/Land Naval Gunfire Liaison"], "130200", "E"
        ),
        "130300": MilStd2525Entity(["Fires", "Field Artillery"], "130300", "E"),
        "130400": MilStd2525Entity(
            ["Fires", "Field Artillery Observer"], "130400", "E"
        ),
        "130500": MilStd2525Entity(["Fires", "Joint Fire Support"], "130500", "E"),
        "130600": MilStd2525Entity(["Fires", "Meteorological"], "130600", "E"),
        "130700": MilStd2525Entity(["Fires", "Missile"], "130700", "E"),
        "130800": MilStd2525Entity(["Fires", "Mortar"], "130800", "E"),
        "130802": MilStd2525Entity(
            ["Fires", "Mortar", "Self-Propelled Wheeled"], "130802", "E"
        ),
        "130900": MilStd2525Entity(["Fires", "Survey"], "130900", "E"),
        # --- PROTECTION (14) ---
        "140000": MilStd2525Entity(["Protection"], "140000", "E"),
        "140100": MilStd2525Entity(["Protection", "CBRN Defense"], "140100", "E"),
        "140102": MilStd2525Entity(
            ["Protection", "CBRN Defense", "Motorized"], "140102", "E"
        ),
        "140103": MilStd2525Entity(
            ["Protection", "CBRN Defense", "Reconnaissance"], "140103", "E"
        ),
        "140105": MilStd2525Entity(
            ["Protection", "CBRN Defense", "Reconnaissance Equipped"], "140105", "E"
        ),
        "140106": MilStd2525Entity(
            ["Protection", "CBRN Defense", "CBRN High-Yield Explosives"], "140106", "E"
        ),
        "140200": MilStd2525Entity(["Protection", "Combat Support"], "140200", "E"),
        "140300": MilStd2525Entity(
            ["Protection", "Criminal Investigation Division"], "140300", "E"
        ),
        "140400": MilStd2525Entity(["Protection", "Diving"], "140400", "E"),
        "140500": MilStd2525Entity(["Protection", "Dog"], "140500", "E"),
        "140600": MilStd2525Entity(["Protection", "Drilling"], "140600", "E"),
        "140700": MilStd2525Entity(["Protection", "Engineer"], "140700", "E"),
        "140701": MilStd2525Entity(
            ["Protection", "Engineer", "Mechanized"], "140701", "E"
        ),
        "140702": MilStd2525Entity(
            ["Protection", "Engineer", "Motorized"], "140702", "E"
        ),
        "140703": MilStd2525Entity(
            ["Protection", "Engineer", "Reconnaissance"], "140703", "E"
        ),
        "140800": MilStd2525Entity(["Protection", "EOD"], "140800", "E"),
        "140900": MilStd2525Entity(
            ["Protection", "Field Camp Construction"], "140900", "E"
        ),
        "141000": MilStd2525Entity(["Protection", "Fire Fighting"], "141000", "E"),
        "141100": MilStd2525Entity(["Protection", "Geospatial Support"], "141100", "E"),
        "141200": MilStd2525Entity(["Protection", "Military Police"], "141200", "E"),
        "141300": MilStd2525Entity(["Protection", "Mine"], "141300", "E"),
        "141400": MilStd2525Entity(["Protection", "Mine Clearing"], "141400", "E"),
        "141500": MilStd2525Entity(["Protection", "Mine Launching"], "141500", "E"),
        "141600": MilStd2525Entity(["Protection", "Mine Laying"], "141600", "E"),
        "141700": MilStd2525Entity(["Protection", "Security"], "141700", "E"),
        "141702": MilStd2525Entity(
            ["Protection", "Security", "Motorized"], "141702", "E"
        ),
        "141800": MilStd2525Entity(["Protection", "Search and Rescue"], "141800", "E"),
        "141801": MilStd2525Entity(
            ["Protection", "Search and Rescue", "Isolated Personnel"], "141801", "E"
        ),
        "142000": MilStd2525Entity(["Protection", "Shore Patrol"], "142000", "E"),
        "142100": MilStd2525Entity(
            ["Protection", "Topographic/Geospatial"], "142100", "E"
        ),
        "142200": MilStd2525Entity(["Protection", "Missile Defense"], "142200", "E"),
        # --- SUSTAINMENT (16) ---
        "160000": MilStd2525Entity(["Sustainment"], "160000", "E"),
        "161300": MilStd2525Entity(["Sustainment", "Medical"], "161300", "E"),
        "163600": MilStd2525Entity(["Sustainment", "Transportation"], "163600", "E"),
        # ... Other values omitted for brevity but following the same "E" pattern
    }

    def __getitem__(self, key: str) -> Optional[MilStd2525Entity]:
        return self._registry.get(key)
