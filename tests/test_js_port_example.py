import os
import sys

# Add parent directory to path to import milsymbol
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from milsymbol import Symbol


def test_js_port():
    # JavaScript Code:
    # new ms.Symbol("130315003611010300000000000000", {
    #   size: 35,
    #   quantity: 200,
    #   staffComments: "for reinforcements".toUpperCase(),
    #   additionalInformation: "added support for JJ".toUpperCase(),
    #   direction: (750 * 360) / 6400,
    #   type: "machine gun".toUpperCase(),
    #   dtg: "30140000ZSEP97",
    #   location: "0900000.0E570306.0N",
    # }).asSVG();

    sidc = "130315003611010300000000000000"
    options = {
        "size": 35,
        "quantity": 200,
        "staffComments": "FOR REINFORCEMENTS",
        "additionalInformation": "ADDED SUPPORT FOR JJ",
        "direction": (750 * 360) / 6400,  # 750 Mils to Degrees
        "type": "MACHINE GUN",
        "dtg": "30140000ZSEP97",
        "location": "0900000.0E570306.0N",
    }

    print(f"Generating Symbol for SIDC: {sidc}")
    print(f"Options: {options}")

    try:
        sym = Symbol(sidc, options)

        output_dir = os.path.join(os.path.dirname(__file__), "output")
        os.makedirs(output_dir, exist_ok=True)

        svg_path = os.path.join(output_dir, "js_port_example.svg")
        png_path = os.path.join(output_dir, "js_port_example.png")

        # Save SVG
        with open(svg_path, "w") as f:
            f.write(sym.asSVG())
        print(f"Saved SVG to {svg_path}")

        # Save PNG
        sym.as_png(png_path)
        print(f"Saved PNG to {png_path}")

    except Exception as e:
        print(f"Error generating symbol: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_js_port()
