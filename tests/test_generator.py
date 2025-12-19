import os
import csv
import sys

# Add parent directory to path to import milsymbol
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from milsymbol import Symbol


def generate_symbols():
    # Paths
    current_dir = os.path.dirname(__file__)
    fixtures_dir = os.path.join(current_dir, "fixtures")
    output_dir = os.path.join(current_dir, "output")
    tsv_path = os.path.join(fixtures_dir, "test_set.tsv")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    print(f"Reading from: {tsv_path}")
    print(f"Writing to: {output_dir}")

    count = 0

    with open(tsv_path, "r") as f:
        reader = csv.DictReader(f, delimiter="\t")

        for row in reader:
            # Parse row data
            scheme = row["codingscheme"]
            affiliation_raw = row["affiliation"]
            battle_dim = row["battledimension"]
            status_raw = row["status"]
            function_id = row["functionid"]
            name = (
                row["name"].replace(" ", "_").replace("/", "_")
            )  # Sanitize for filename
            sizes = row["sizes"]

            # Defaults
            affiliation = "F" if affiliation_raw == "*" else affiliation_raw
            status = "P" if status_raw == "*" else status_raw

            # Echelon iteration
            echelons_to_generate = []
            if not sizes:
                echelons_to_generate.append(("-", ""))  # (Code, Suffix_Name)
            else:
                # Handle range like "A-D"
                if "-" in sizes and len(sizes) == 3:
                    start_char = sizes[0]
                    end_char = sizes[2]
                    # ASCII iteration
                    for i in range(ord(start_char), ord(end_char) + 1):
                        char_code = chr(i)
                        echelons_to_generate.append((char_code, f"_{char_code}"))
                else:
                    # Single char or non-standard format, just use it
                    echelons_to_generate.append((sizes, f"_{sizes}"))

            for ech_code, ech_suffix in echelons_to_generate:
                # Construct SIDC (15 chars)
                # 0: Scheme
                # 1: Affiliation
                # 2: Battle Dimension
                # 3: Status
                # 4-9: Function ID (6 chars)
                # 10: Modifier 1 (-)
                # 11: Echelon
                # 12-13: Country (--)
                # 14: Order of Battle (-)

                # UCD--- is 6 chars.
                # SIDC construction:
                # S + F + G + P + UCD--- + - + D + -- + -

                sidc = f"{scheme}{affiliation}{battle_dim}{status}{function_id}-{ech_code}--"

                # Check length (should be 15)
                # function_id in TSV is "UCD---" (6 chars)
                # Let's verify string construction
                # S F G P UCD--- - - -- - (Too long?)
                # Wait. function_id in TSV is UCD---.
                # Let's look at test_unit_generation.py example: SFG-UCI----
                # S: Scheme
                # F: Affiliation
                # G: Dimension
                # -: Status (Not P?)
                # U: Function ID
                # C: Function ID
                # I: Function ID
                # -: Function ID
                # -: Function ID
                # -: Function ID
                # -: Mod 1
                # -: Echelon

                # TSV has:
                # Scheme: S
                # Affiliation: *
                # Dim: G
                # Status: *
                # FunctionID: UCD---

                # If I use defaults F and P:
                # S F G P U C D - - - - [Ech] - -
                # That is 15 chars.

                # However, many test cases use '-' for Status.
                # The prompt said '*'. Standard usually allows '-' or 'P'.
                # Let's stick to 'P' for * as planned, unless visual confirms otherwise.

                filename_base = f"{name}{ech_suffix}_{sidc}"
                svg_path = os.path.join(output_dir, f"{filename_base}.svg")
                png_path = os.path.join(output_dir, f"{filename_base}.png")

                try:
                    sym = Symbol(sidc)

                    # Generate SVG
                    with open(svg_path, "w") as svg_file:
                        svg_file.write(sym.asSVG())

                    # Generate PNG
                    sym.as_png(png_path)

                    count += 1
                    # print(f"Generated {filename_base}")

                except Exception as e:
                    print(f"Error generating {sidc}: {e}")

    print(f"Successfully generated {count} symbols.")


if __name__ == "__main__":
    generate_symbols()
