from .colormode import ColorMode
from ..colormodes import ColorModes
from .bbox import BBox


class MS:
    def __init__(self):
        self._autoValidation = False
        self.version = "3.0.3"
        self._colorModes = {}
        self._symbolParts = []
        self._iconParts = []
        self._labelOverrides = {}
        self._iconSIDC = {"letter": [], "number": []}
        self._getIcons = {}
        self._getMetadata = {}

        # Initialize default state
        self.reset()

        # Classes attached to ms
        self.BBox = BBox
        self.ColorMode = ColorMode

    def setColorMode(self, mode, colorMode):
        self._colorModes[mode] = {}
        self._colorModes[mode]["Hostile"] = colorMode.get("Hostile")
        self._colorModes[mode]["Friend"] = colorMode.get("Friend")
        self._colorModes[mode]["Neutral"] = colorMode.get("Neutral")
        self._colorModes[mode]["Unknown"] = colorMode.get("Unknown")
        self._colorModes[mode]["Civilian"] = colorMode.get("Civilian")
        self._colorModes[mode]["Suspect"] = colorMode.get("Suspect")
        return self._colorModes[mode]

    def addSymbolPart(self, part):
        if callable(part):
            if part not in self._symbolParts:
                self._symbolParts.append(part)
        return self

    def getSymbolParts(self):
        return self._symbolParts[:]

    def setSymbolParts(self, parts):
        self._symbolParts = parts
        return self

    def reset(self):
        self._brokenPath2D = None
        self._colorModes = {}
        for name, mode in ColorModes.items():
            self.setColorMode(name, mode)

        self._dashArrays = {
            "pending": "4,4",
            "anticipated": "8,12",
            "feintDummy": "8,8",
        }
        self._getIcons = {}
        self._getMetadata = {}
        self._hqStaffLength = 100
        self._iconCache = {}
        self._iconParts = []
        self._labelCache = {}
        self._labelOverrides = {}
        self._iconSIDC = {}
        self._iconSIDC["letter"] = []
        self._iconSIDC["number"] = []
        self._STD2525 = True
        self._svgNS = "http://www.w3.org/2000/svg"
        self._symbolParts = []

        # We will add default symbol parts later as they are imported
        # ms.addSymbolPart(basegeometry) etc...

    def setBrokenPath2D(self, broken):
        self._brokenPath2D = broken

    def _getIconParts(self, metadata, colors, _STD2525, monoColor, alternateMedal):
        icn = {}
        for part in self._iconParts:
            part(self, icn, metadata, colors, _STD2525, monoColor, alternateMedal)
        if not isinstance(icn, dict):
            raise TypeError(f"icn is not a dict! It is {type(icn)}")
        return icn

    def _scale(self, factor, instruction, non_scaling_stroke=False):
        def recurse_scale(instr, f):
            if isinstance(instr, list):
                for d in instr:
                    if isinstance(d, dict):  # Should be dict or object
                        d["non_scaling_stroke"] = 1 / f
                        if "draw" in d:
                            recurse_scale(d["draw"], f)
                    if isinstance(d, list):
                        for e in d:
                            recurse_scale(e, f)
            elif isinstance(instr, dict):
                instr["non_scaling_stroke"] = 1 / f

        if non_scaling_stroke:
            recurse_scale(instruction, factor)

        return {
            "type": "translate",
            "x": 100 - factor * 100,
            "y": 100 - factor * 100,
            "draw": [{"type": "scale", "factor": factor, "draw": [instruction]}],
        }

    def _translate(self, x, y, instruction):
        return {"type": "translate", "x": x, "y": y, "draw": [instruction]}

    def addIconParts(self, parts):
        if not isinstance(parts, list):
            parts = [parts]
        for part in parts:
            if callable(part) and part not in self._iconParts:
                self._iconParts.append(part)
        return self

    def addLabelOverrides(self, parts, type_):
        self._labelCache = {}
        if callable(parts):
            if type_ not in self._labelOverrides:
                self._labelOverrides[type_] = []
            self._labelOverrides[type_].append(parts)
        return self

    def addIcons(self, obj):
        self._iconCache = {}
        if not isinstance(obj, list):
            obj = [obj]
        for item in obj:
            if hasattr(item, "getMetadata") or "getMetadata" in item:
                self._getMetadata[item["type"]] = item["getMetadata"]
            if hasattr(item, "getIcons") or "getIcons" in item:
                self._getIcons[item["type"]] = item["getIcons"]
            if hasattr(item, "iconParts") or "iconParts" in item:
                self.addIconParts(item["iconParts"])
            if hasattr(item, "labels") or "labels" in item:
                self.addLabelOverrides(item["labels"], item["type"])
            if hasattr(item, "icons") or "icons" in item:
                self.addSIDCicons(item["icons"], item["type"])

    def addSIDCicons(self, parts, type_):
        if callable(parts):
            if parts not in self._iconSIDC.get(type_, []):
                self._iconSIDC.setdefault(type_, []).append(parts)
        return self

    def getColorMode(self, mode):
        c = self._colorModes.get(mode)
        if c:
            return ColorMode(
                c["Civilian"],
                c["Friend"],
                c["Hostile"],
                c["Neutral"],
                c["Unknown"],
                c["Suspect"],
            )
        return None

    def getDashArrays(self):
        return self._dashArrays

    def getHqStaffLength(self):
        return self._hqStaffLength

    def getVersion(self):
        return self.version

    def outline(self, geom, width, stroke_width, color):
        # Implementation of outline logic, likely calling another module's function
        # For now, placeholder or needs to be set from outside as in the JS code
        # JS: ms.outline = outline; imported from ./ms/outline.js
        if hasattr(self, "_outline_func"):
            return self._outline_func(geom, width, stroke_width, color)
        return None

    def setDashArrays(self, pending, anticipated, feintDummy):
        self._dashArrays["pending"] = pending
        self._dashArrays["anticipated"] = anticipated
        self._dashArrays["feintDummy"] = feintDummy
        return self._dashArrays

    def setHqStaffLength(self, length):
        self._hqStaffLength = length
        return self._hqStaffLength

    def setStandard(self, standard):
        if standard == "2525":
            self._STD2525 = True
            return True
        if standard == "APP6":
            self._STD2525 = False
            return True
        return False

    def showOctagon(self):
        # ms.addSymbolPart(debug)
        pass


# Create singleton instance
ms = MS()
