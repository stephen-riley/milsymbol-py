import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from milsymbolpy import Symbol


def test_human_readable():
    test_cases = [
        # Original
        (
            "130310001612110007061100000000",
            "Infantry [Armored, Wheeled X (Cross Country)] (BN/SQDN)",
        ),
        # New Cases
        ("130310000012110007001000000000", "Infantry [Armored]"),
        ("130310000012110000060100000000", "Infantry [Wheeled X (Cross Country)]"),
        ("130310001612110000000000000000", "Infantry (BN/SQDN)"),
    ]

    all_passed = True
    for sidc, expected in test_cases:
        s = Symbol(sidc)
        name = s.get_desc()

        if name == expected:
            print(f"PASS: {sidc} -> '{name}'")
        else:
            print(f"FAIL: {sidc}\n  Expected: '{expected}'\n  Got:      '{name}'")
            all_passed = False

    if all_passed:
        print("\nAll tests passed.")
    else:
        sys.exit(1)


if __name__ == "__main__":
    test_human_readable()
