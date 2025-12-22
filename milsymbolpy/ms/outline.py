import copy


def outline(geom, outline_width, stroke, color):
    def process(g, width, s, c):
        if isinstance(g, list):
            clone = []
            for item in g:
                clone.append(process(item, width, s, c))
            return clone
        elif isinstance(g, dict):
            clone = {}
            for key, value in g.items():
                if key not in ["fill", "fillopacity"]:
                    clone[key] = value

            if g.get("type") in ["translate", "rotate", "scale"]:
                clone["draw"] = []
                for item in g.get("draw", []):
                    clone["draw"].append(process(item, width, s, c))
            else:
                current_stroke_width = g.get("strokewidth", s)
                if current_stroke_width is None:
                    current_stroke_width = s or 0  # Fallback

                # Check explicit false check in JS: clone.stroke !== false
                # In Python we need to check if key exists or value
                if g.get("stroke") is not False:
                    clone["strokewidth"] = float(current_stroke_width) + 2 * width
                else:
                    clone["strokewidth"] = 2 * width

                clone["stroke"] = c
                clone["fill"] = False
                clone["linecap"] = "round"
            return clone
        else:
            return g  # Should not happen if structure is correct

    return process(geom, outline_width, stroke, color)
