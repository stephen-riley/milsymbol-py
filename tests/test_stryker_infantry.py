import unittest
import sys
import os
import xml.etree.ElementTree as ET

# Add parent directory to path to import milsymbol
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from milsymbolpy import Symbol


class TestFriendlyStrykerInfantry(unittest.TestCase):
    def test_generate_symbol(self):
        sidc = "130310001612110007061100000000"

        symbol = Symbol(sidc)
        svg_content = symbol.as_svg()

        # Validate XML structure
        try:
            root = ET.fromstring(svg_content)
            self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")
        except ET.ParseError as e:
            self.fail(f"Generated SVG is not valid XML: {e}")

        # Ensure output directory exists (using existing tests/output)
        output_dir = os.path.join(os.path.dirname(__file__), "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save to file
        svg_path = os.path.join(output_dir, "friendly_stryker_infantry_bn.svg")
        png_path = os.path.join(output_dir, "friendly_stryker_infantry_bn.png")

        with open(svg_path, "w") as f:
            f.write(svg_content)

        print(f"Generated SVG saved to: {svg_path}")

        # Save PNG
        try:
            symbol.as_png(png_path)
            print(f"Generated PNG saved to: {png_path}")
        except Exception as e:
            print(f"Error generating PNG: {e}")
            # Fail the test if PNG generation fails, as user requested it
            self.fail(f"PNG generation failed: {e}")

        # Optional: verify file content is not empty
        self.assertGreater(len(svg_content), 0)
        self.assertTrue(os.path.exists(png_path), "PNG file was not created")


if __name__ == "__main__":
    unittest.main()
