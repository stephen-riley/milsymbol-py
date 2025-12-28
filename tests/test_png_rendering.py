import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from milsymbolpy import Symbol


def test_png_rendering(sidc, symbol_size=150):
    s = Symbol(sidc, {"size": symbol_size})
    ident = "FR" if sidc[2:4] == "03" else "EN"

    # Test training True (Centered, default size)
    print("Generating Training PNG (default 384x384, centered)...")
    s.as_png(f"tests/output/{ident}_png_training_384.png", training=True)

    # Test training True (Centered, 500x500)
    print("Generating Training PNG (default 500x500, centered)...")
    s.as_png(
        f"tests/output/{ident}_png_training_500.png",
        training=True,
        width=500,
        height=500,
    )

    # Test training False (default rendering)
    print("Generating Training PNG (default size)...")
    s.as_png(f"tests/output/{ident}_png_default_size.png")


if __name__ == "__main__":
    test_png_rendering("130310001612110007061100000000")
    test_png_rendering("130610001612110007061100000000")
