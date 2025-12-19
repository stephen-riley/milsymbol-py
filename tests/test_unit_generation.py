import unittest
import sys
import os
import xml.etree.ElementTree as ET

# Add parent directory to path to import milsymbol
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from milsymbol import Symbol


class TestUnitGeneration(unittest.TestCase):
    def validate_svg_xml(self, svg_string):
        """Helper to validate if string is valid XML/SVG."""
        try:
            root = ET.fromstring(svg_string)
            self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")
            return root
        except ET.ParseError as e:
            self.fail(f"SVG XML Parse Error: {e}")

    def test_echelons(self):
        # Base SIDC: SFG-UCI--- (Friend, Ground, Unit, Cavalry, Infantry) + Echelon + Country (--)
        # Echelon mapping from symbol.py:
        # 14: Platoon (Code: D?) - Wait, mapping is '14' -> Platoon.
        # But in Letter SIDC, what char is '14'?
        # 2525C: Code position 12 (index 11).
        # Codes:
        # A: Team/Crew
        # B: Squad
        # C: Section
        # D: Platoon
        # E: Company
        # F: Battalion
        # G: Regiment
        # H: Brigade

        echelons = {"Platoon": "D", "Company": "E", "Battalion": "F"}

        # Expected structure 15 chars: 0-9 functional, 10-11 mod, 12-13 country, 14 order?
        # Actually 15 chars:
        # 0: S
        # 1: F
        # 2: G
        # 3: -
        # 4: U
        # 5: C
        # 6: I
        # 7: -
        # 8: -
        # 9: -
        # 10: - (Modifier 1)
        # 11: Echelon (Modifier 2)
        # 12-13: Country
        # 14: Order of Battle

        # Example SIDC: SFG-UCI----D--

        for name, code in echelons.items():
            sidc = f"SFG-UCI----{code}"
            with self.subTest(echelon=name, sidc=sidc):
                sym = Symbol(sidc)
                svg = sym.asSVG()
                self.validate_svg_xml(svg)
                # print(f"Verified {name}: {sidc}")

    def test_units(self):
        # Test different units
        # Infantry: SFG-UCI----
        # Armor: SFG-UCA----
        # Artillery: SFG-UCAF--- (Field Artillery?) - check codes later if fail

        units = [
            "SFG-UCI----",  # Infantry
            "SFG-UCA----",  # Armor
            # "SFG-UCF----", # Fire Support / Artillery?
        ]

        for sidc in units:
            with self.subTest(sidc=sidc):
                sym = Symbol(sidc)
                svg = sym.asSVG()
                self.validate_svg_xml(svg)

    def test_affiliations(self):
        # Friend: F, Hostile: H, Neutral: N, Unknown: U
        affiliations = ["F", "H", "N", "U"]
        base = "SG-UCI----"  # Missing affiliation at pos 1

        for aff in affiliations:
            sidc = f"S{aff}{base}"
            with self.subTest(affiliation=aff, sidc=sidc):
                sym = Symbol(sidc)
                svg = sym.asSVG()
                self.validate_svg_xml(svg)


if __name__ == "__main__":
    unittest.main()
