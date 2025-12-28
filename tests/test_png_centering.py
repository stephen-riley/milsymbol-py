import sys
import os
from PIL import Image
import io

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from milsymbolpy import Symbol


def test_png_centering():
    sidc = "130310001612110007061100000000"
    s = Symbol(sidc)

    # Test training True (Centered)
    print("Generating Training PNG (default 384x384, centered)...")
    png_bytes_training = s.as_png(training=True)
    if not png_bytes_training:
        print("FAIL: No PNG bytes returned (cairosvg likely missing or error)")
        return
    img_training = Image.open(io.BytesIO(png_bytes_training))
    print(f"Training Dimensions: {img_training.size}")

    if img_training.size == (384, 384):
        print("PASS: Training dimensions are 384x384")
    else:
        print(f"FAIL: Expected 384x384, got {img_training.size}")

    # Check if corner is white (opaque)
    corner_pixel = img_training.getpixel((0, 0))
    # Expect (255, 255, 255, 255)
    if corner_pixel == (255, 255, 255, 255):
        print("PASS: Background is white opaque")
    else:
        print(f"FAIL: Expected white opaque bg, got {corner_pixel}")

    # Test training False (Default/Original)
    print("\nGenerating Standard PNG (should be fit to symbol)...")
    png_bytes_std = s.as_png(training=False)
    if not png_bytes_std:
        print("FAIL: No PNG bytes returned (cairosvg likely missing or error)")
        return
    img_std = Image.open(io.BytesIO(png_bytes_std))
    print(f"Standard Dimensions: {img_std.size}")

    # Dimensions should be roughly typical symbol size (e.g. 150x150 range), NOT 384x384
    if img_std.size != (384, 384):
        print("PASS: Standard dimensions differ from training fixed size.")
    else:
        print(
            "WARN: Standard dimensions match training size, might be coincidence or error."
        )

    if img_std.size[0] < 200 and img_std.size[1] < 200:
        print("PASS: Standard dimensions seem appropriate for raw symbol.")
    else:
        print(f"WARN: Standard dimensions {img_std.size} seem large for raw symbol.")

    # Test custom training
    print("\nGenerating Custom Training PNG (500x500)...")
    png_bytes_custom = s.as_png(width=500, height=500, training=True)
    if not png_bytes_custom:
        print("FAIL: No PNG bytes returned (cairosvg likely missing or error)")
        return
    img_custom = Image.open(io.BytesIO(png_bytes_custom))
    print(f"Custom Training Dimensions: {img_custom.size}")

    if img_custom.size == (500, 500):
        print("PASS: Custom training dimensions are 500x500")
    else:
        print(f"FAIL: Expected 500x500, got {img_custom.size}")


if __name__ == "__main__":
    test_png_centering()
