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
