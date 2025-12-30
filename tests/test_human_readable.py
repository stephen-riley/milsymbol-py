import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from milsymbolpy import Symbol


def test_human_readable():
    test_cases = [
        ("130310000012110007001000000000", "Friendly Armored Infantry"),
        ("130310000012110000060100000000", "Friendly Wheeled X (Cross Country) Infantry"),
        ("130310001612110000000000000000", "Friendly Infantry Battalion/Squadron"),
        ("130310001612110600000000000000", "Friendly Infantry, Main Gun System Battalion/Squadron"),
        (
            # test of overrides -- should call this Stryker
            "130310001612110007061100000000",
            "Friendly Stryker Battalion/Squadron",
        ),
        (
            # test of overrides -- should NOT call this Stryker
            "130610001612110007061100000000",
            "Hostile Armored, Wheeled X (Cross Country) Infantry Battalion/Squadron",
        ),
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
