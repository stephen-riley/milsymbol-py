import os
import csv
import sys

# Add parent directory to path to import milsymbol
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from milsymbolpy import Symbol


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

    affiliations_map = [("F", "FR", "FR"), ("H", "EN", "EN")]

    with open(tsv_path, "r") as f:
        reader = csv.DictReader(f, delimiter="\t")

        for row in reader:
            # Parse row data
            scheme = row["codingscheme"]
            # row["affiliation"] is ignored as we iterate both
            battle_dim = row["battledimension"]
            status_raw = row["status"]
            function_id = row["functionid"]
            name = (
                row["name"].replace(" ", "_").replace("/", "_")
            )  # Sanitize for filename
            sizes = row["sizes"]

            # Check if codingscheme is a numeric SIDC (starts with ' or digit)
            is_numeric_sidc = scheme.startswith("'") or (
                len(scheme) > 0 and scheme[0].isdigit()
            )

            if is_numeric_sidc:
                base_sidc = scheme.replace("'", "").strip()

                # Numeric Echelon Mapping (Alpha -> Numeric)
                echelon_map = {
                    "A": "11",
                    "B": "12",
                    "C": "13",
                    "D": "14",
                    "E": "15",
                    "F": "16",
                    "G": "17",
                    "H": "18",
                    "I": "21",
                    "J": "22",
                    "K": "23",
                    "L": "24",
                    "M": "25",
                    "N": "26",
                    "-": "00",
                }

                # Affiliations for Numeric: Friend=3, Hostile=6
                # Parallel structure to affiliations_map: (NumericCode, Folder, Prefix)
                numeric_affiliations = [("3", "FR", "FR"), ("6", "EN", "EN")]

                # Echelon iteration for Numeric
                numeric_echelons = []
                if not sizes:
                    numeric_echelons.append(("00", ""))
                else:
                    if "-" in sizes and len(sizes) == 3:
                        start_char = sizes[0]
                        end_char = sizes[2]
                        for i in range(ord(start_char), ord(end_char) + 1):
                            char_code = chr(i)
                            if char_code in echelon_map:
                                numeric_echelons.append(
                                    (echelon_map[char_code], f"_{char_code}")
                                )
                    else:
                        if sizes in echelon_map:
                            numeric_echelons.append((echelon_map[sizes], f"_{sizes}"))
                        else:
                            # Fallback if unknown size
                            numeric_echelons.append(("00", ""))

                for aff_digit, aff_folder, aff_prefix in numeric_affiliations:
                    sub_output_dir = os.path.join(output_dir, aff_folder)
                    os.makedirs(sub_output_dir, exist_ok=True)

                    for ech_code, ech_suffix in numeric_echelons:
                        # Construct Numeric SIDC
                        # Base: 10 chars Version/Context/Standard/SymbolSet + 2 chars Status/HQ + 2 chars Echelon + ...
                        # We need to replace Affiliation (index 3) and Echelon (index 8-10)
                        # SIDC string indices:
                        # 0-1: Version
                        # 2: Context
                        # 3: Affiliation -> Replace with aff_digit
                        # 4-5: SymbolSet
                        # 6: Status
                        # 7: HQ/TF
                        # 8-9: Echelon -> Replace with ech_code

                        sidc_list = list(base_sidc)
                        if len(sidc_list) >= 10:
                            sidc_list[3] = aff_digit
                            sidc_list[8] = ech_code[0]
                            sidc_list[9] = ech_code[1]

                        sidc = "".join(sidc_list)

                        filename_base = f"{aff_prefix}_{name}{ech_suffix}_{sidc}"
                        svg_path = os.path.join(sub_output_dir, f"{filename_base}.svg")
                        png_path = os.path.join(sub_output_dir, f"{filename_base}.png")

                        try:
                            sym = Symbol(sidc)
                            with open(svg_path, "w") as svg_file:
                                svg_file.write(sym.as_svg())
                            sym.as_png(png_path)
                            count += 1
                        except Exception as e:
                            print(f"Error generating {sidc}: {e}")

            else:
                # Legacy Alpha SIDC Logic
                # Defaults
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

                for aff_code, aff_folder, aff_prefix in affiliations_map:
                    # Ensure sub-output directory exists
                    sub_output_dir = os.path.join(output_dir, aff_folder)
                    os.makedirs(sub_output_dir, exist_ok=True)

                    for ech_code, ech_suffix in echelons_to_generate:
                        # Construct SIDC (15 chars)
                        sidc = f"{scheme}{aff_code}{battle_dim}{status}{function_id}-{ech_code}--"

                        filename_base = f"{aff_prefix}_{name}{ech_suffix}_{sidc}"
                        svg_path = os.path.join(sub_output_dir, f"{filename_base}.svg")
                        png_path = os.path.join(sub_output_dir, f"{filename_base}.png")

                        try:
                            sym = Symbol(sidc)

                            # Generate SVG
                            with open(svg_path, "w") as svg_file:
                                svg_file.write(sym.as_svg())

                            # Generate PNG
                            sym.as_png(png_path)

                            count += 1
                            # print(f"Generated {filename_base}")

                        except Exception as e:
                            print(f"Error generating {sidc}: {e}")

    print(f"Successfully generated {count} symbols.")


if __name__ == "__main__":
    generate_symbols()
