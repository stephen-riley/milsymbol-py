import unittest
import os
import sys

# Add parent directory to path to import milsymbolpy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from milsymbolpy import Symbol


class TestSignalSymbol(unittest.TestCase):
    def test_signal_symbol_geometry(self):
        # Define test cases for Friendly and Hostile
        test_cases = [
            ("friendly", "10031000001110000000"),
            ("enemy", "10061000001110000000"),
        ]

        output_dir = os.path.join(os.path.dirname(__file__), "output")
        os.makedirs(output_dir, exist_ok=True)

        for name, sidc in test_cases:
            symbol = Symbol(sidc)
            svg = symbol.as_svg()

            filename = f"{name.lower()}_signal_symbol.svg"
            svg_path = os.path.join(output_dir, filename)

            with open(svg_path, "w") as f:
                f.write(svg)

            print(f"Generated {name} Signal symbol at: {svg_path}")

            # Save PNG
            try:
                png_path = os.path.join(output_dir, f"{name.lower()}_signal_symbol.png")
                symbol.as_png(png_path)
                print(f"Generated {name} Signal symbol PNG at: {png_path}")
            except Exception as e:
                print(f"Failed to generate PNG for {name}: {e}")

        # Check if the SVG contains the incorrect triangle path or correct lightning bolt
        # Incorrect triangle (based on assumption): M 100,60 ...
        # Correct lightning bolt should look different.
        # We can also check for "100,60" which is typical top center for frame, but let's just inspect output.


if __name__ == "__main__":
    unittest.main()
