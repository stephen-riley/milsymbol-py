import unittest
import sys
import os

# Add parent directory to path to import milsymbol
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from milsymbolpy import Symbol


def render_antiarmor(sidc, filename):
    symbol = Symbol(sidc, {"size": 384 / 178 * 100})
    svg_content = symbol.as_svg()

    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)

    # Save to file
    svg_path = os.path.join(output_dir, filename)

    with open(svg_path, "w") as f:
        f.write(svg_content)

    print(f"Generated SVG saved to: {svg_path}")


class TestAntiarmor(unittest.TestCase):
    render_antiarmor("130610000012040000000000000000", "en_antiarmor.svg")
    render_antiarmor("130310000012040000000000000000", "fr_antiarmor.svg")


if __name__ == "__main__":
    unittest.main()
