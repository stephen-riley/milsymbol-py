import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from milsymbolpy import Symbol


class TestHumanReadableDesc(unittest.TestCase):
    def test_human_readable_desc(self):
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
                "Hostile Armored Wheeled X (Cross Country) Infantry Battalion/Squadron",
            ),
        ]

        for sidc, expected in test_cases:
            s = Symbol(sidc)
            name = s.get_desc()

            self.assertEqual(name, expected)

    def test_human_readable_pieces(self):
        test_cases = [
            ("130310000012110007001000000000", ["Friendly", "Armored", None, "Infantry", None]),
            ("130310000012110000060100000000", ["Friendly", None, "Wheeled X (Cross Country)", "Infantry", None]),
            ("130310001612110000000000000000", ["Friendly", None, None, "Infantry", "Battalion/Squadron"]),
            ("130310001612110600000000000000", ["Friendly", None, None, "Infantry, Main Gun System", "Battalion/Squadron"]),
            (
                # test of overrides -- should call this Stryker
                "130310001612110007061100000000",
                ["Friendly", None, None, "Stryker", "Battalion/Squadron"],
            ),
            (
                # test of overrides -- should NOT call this Stryker
                "130610001612110007061100000000",
                ["Hostile", "Armored", "Wheeled X (Cross Country)", "Infantry", "Battalion/Squadron"],
            ),
        ]

        for sidc, expected in test_cases:
            s = Symbol(sidc)
            p = s.get_desc_pieces()
            a = [p[el] for el in ['alignment', 'modifier1', 'modifier2', 'entity', 'echelon']]

            self.assertListEqual(a, expected)


if __name__ == "__main__":
    unittest.main()
