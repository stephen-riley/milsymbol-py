import unittest
import xml.etree.ElementTree as ET
import sys
import os

# Add parent directory to path to import milsymbol
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from milsymbol import Symbol


class TestSVGSyntax(unittest.TestCase):
    def validate_svg_xml(self, svg_string):
        """Helper to validate if string is valid XML/SVG."""
        try:
            root = ET.fromstring(svg_string)
            self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")
            return root
        except ET.ParseError as e:
            self.fail(f"SVG XML Parse Error: {e}")

    def test_simple_symbol_svg(self):
        # 2525C simple symbol
        sidc = "SFG-UCI----D"
        sym = Symbol(sidc)
        svg = sym.asSVG()
        root = self.validate_svg_xml(svg)

        # Check basic attributes
        self.assertIn("width", root.attrib)
        self.assertIn("height", root.attrib)
        self.assertIn("viewBox", root.attrib)

    def test_number_sidc_svg(self):
        # 2525D number sidc
        sidc = "10031000001211000000"
        sym = Symbol(sidc)
        svg = sym.asSVG()
        root = self.validate_svg_xml(svg)

        self.assertIn("width", root.attrib)
        self.assertIn("height", root.attrib)

    def test_modifiers(self):
        sidc = "SFG-UCI----D"
        options = {"uniqueDesignation": "1st Plt", "higherFormation": "2nd Bn"}
        sym = Symbol(sidc, options)
        svg = sym.asSVG()
        root = self.validate_svg_xml(svg)

        # Simple check if text exists in SVG (not perfect, but good sanity check)
        self.assertTrue("1st Plt" in svg)
        self.assertTrue("2nd Bn" in svg)


if __name__ == "__main__":
    unittest.main()
