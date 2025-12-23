from .bbox import BBox
from .lookup.entities import MilStd2525Entities
from .lookup.modifiers import MilStd2525Sector1Modifiers, MilStd2525Sector2Modifiers


class Symbol:
    def __init__(self, *args):
        # =======================================================================================
        self.bbox = BBox()  # Contains the bounding box of the current symbol
        self.colors = {}  # Contains the colors for the current symbol
        self.metadata = {}  # Metadata of the current symbol
        self.octagonAnchor = {"x": 50, "y": 50}  # The anchor point for the octagon

        self.options = {
            "quantity": "",  # FieldID C
            "reinforcedReduced": "",  # FieldID F
            "staffComments": "",  # FieldID G
            "additionalInformation": "",  # FieldID H
            "evaluationRating": "",  # FieldID J
            "combatEffectiveness": "",  # FieldID K
            "signatureEquipment": "",  # FieldID L
            "higherFormation": "",  # FieldID M
            "hostile": "",  # FieldID N
            "iffSif": "",  # FieldID P
            "direction": None,  # FieldID Q
            "sigint": "",  # FieldID R2
            "uniqueDesignation": "",  # FieldID T
            "type": "",  # FieldID V
            "dtg": "",  # FieldID W
            "altitudeDepth": "",  # FieldID X
            "location": "",  # FieldID Y
            "speed": "",  # FieldID Z
            "speedLeader": 0,  # This is the length of the speed leader
            "specialHeadquarters": "",  # FieldID AA
            "country": "",  # AC Country
            "platformType": "",  # FieldID AD
            "equipmentTeardownTime": "",  # FieldID AE
            "commonIdentifier": "",  # FieldID AF
            "auxiliaryEquipmentIndicator": "",  # FieldID AG
            "headquartersElement": "",  # FieldID AH
            "installationComposition": "",  # FieldID AI
            # FieldID AM Distance
            # FieldID AN Azimuth
            "engagementBar": "",  # FieldID AO EngagementBar
            "engagementType": "",  # Engagement Bar Type: "TARGET", "NON-TARGET", or "EXPIRED"
            "guardedUnit": "",  # FieldID AQ
            "specialDesignator": "",  # FieldID AR
            "sidc": "",  # SIDC
        }

        self.style = {
            "alternateMedal": False,  # 2525D lets you choose between MEDAL icn and alternate MEDAL icn for Mines
            "civilianColor": True,  # Should we use the Civilian Purple defined in 2525?
            "colorMode": "Light",  # "Dark", "Medium" or "Light"
            "fill": True,  # Should the icon be filled with color
            "fillColor": "",  # Override the frame fill with any color
            "fillOpacity": 1,  # Possibility to change the fill opacity
            "fontfamily": "Arial",  # The font family to use
            "frame": True,  # Should the icon be framed
            "frameColor": "",
            "hqStaffLength": 0,  # The default length of the HQ staf
            "icon": True,  # Should we display the icon?
            "iconColor": "",
            "infoBackground": "",  # Color of square behind texts
            "infoBackgroundFrame": "",  # Color of the squares frame
            "infoColor": "",  # Changes the color of the info fields
            "infoFields": True,  # If you have set all info fields but don't want the displayed
            "infoOutlineColor": "rgb(239, 239, 239)",  # Color of the text outline.
            "infoOutlineWidth": False,  # Width of the text-field outline.
            "infoSize": 40,  # Relative size of the info fields
            "monoColor": "",  # Should the icon be monocromatic and if so what color
            "outlineColor": "rgb(239, 239, 239)",  # Color of the outline
            "outlineWidth": 0,  # Width of the outline.
            "padding": 0,  # Extra padding around the symbol
            "simpleStatusModifier": False,  # Force use of simple status modifiers
            "size": 100,  # The symbol size is actually the L variable in the symbols
            "square": False,  # If the symbol should be square
            "standard": "",  # Set standard override
            "strokeWidth": 4,  # The stroke width of he icon frame.
        }

        self.symbolAnchor = {
            "x": 50,
            "y": 50,
        }  # The anchor point for the current symbol
        self.validIcon = True  # If we were able to find a valid icon or not.
        self.drawInstructions = []
        self.width = 100
        self.height = 100
        self.baseWidth = 100
        self.baseHeight = 100

        if args:
            self.setOptions(*args)

    def setOptions(self, *args):
        # Implementation of setOptions
        # Deferred import to avoid circular dependency
        from .ms import ms

        for options in args:
            if isinstance(options, dict):
                for key, value in options.items():
                    if key == "SIDC":
                        self.options["sidc"] = value
                        continue
                    if key in self.style:
                        self.style[key] = value
                    else:
                        self.options[key] = value
            else:
                # if there just is something not an object, we asume that it is the SIDC
                self.options["sidc"] = options

        self.validIcon = True
        self.metadata = self.getMetadata()
        self.colors = self.getColors()
        self.drawInstructions = []
        self.bbox = BBox()

        # Processing all parts of the symbol
        for part in ms.getSymbolParts():
            m = part(self, ms)  # Call symbol part function
            # Expect m to be {pre: [], post: [], bbox: ...}
            if not m:
                continue

            notEmpty = (len(m.get("pre", [])) > 0) or (len(m.get("post", [])) > 0)

            pre = m.get("pre", [])
            if pre:
                while len(pre) == 1 and isinstance(pre[0], list):
                    pre = pre[0]
                if pre:
                    self.drawInstructions = pre + self.drawInstructions

            post = m.get("post", [])
            if post:
                while len(post) == 1 and isinstance(post[0], list):
                    post = post[0]
                if post:
                    self.drawInstructions = self.drawInstructions + post

            bbox_val = m.get("bbox")
            if bbox_val and notEmpty:
                self.bbox.merge(bbox_val)

        if self.style["padding"]:
            pad = self.style["padding"]
            self.bbox.x1 -= pad
            self.bbox.x2 += pad
            self.bbox.y1 -= pad
            self.bbox.y2 += pad

        anchor = {"x": 100, "y": 100}

        sw = float(self.style["strokeWidth"])
        ow = float(self.style["outlineWidth"])
        sz = self.style["size"]

        self.octagonAnchor = {
            "x": ((anchor["x"] - self.bbox.x1 + sw + ow) * sz) / 100,
            "y": ((anchor["y"] - self.bbox.y1 + sw + ow) * sz) / 100,
        }

        # Headquarters anchor adjustment
        if self.metadata.get("headquarters"):
            hqStaffLength = self.style["hqStaffLength"] or ms.getHqStaffLength()
            bg_bbox = self.metadata.get("baseGeometry", {}).get("bbox")
            if bg_bbox:
                # bg_bbox might be BBox object
                # In JS: self.metadata.baseGeometry.bbox.x1
                x1 = bg_bbox.x1
                y2 = bg_bbox.y2
                anchor = {"x": x1, "y": y2 + hqStaffLength}

        if self.style["square"]:
            maxx = max(anchor["x"] - self.bbox.x1, self.bbox.x2 - anchor["x"])
            maxy = max(anchor["y"] - self.bbox.y1, self.bbox.y2 - anchor["y"])
            max_val = max(maxx, maxy)
            self.bbox.x1 = anchor["x"] - max_val
            self.bbox.y1 = anchor["y"] - max_val
            self.bbox.x2 = anchor["x"] + max_val
            self.bbox.y2 = anchor["y"] + max_val

        self.baseWidth = self.bbox.width() + sw * 2 + ow * 2
        self.baseHeight = self.bbox.height() + sw * 2 + ow * 2

        self.width = (self.baseWidth * sz) / 100
        self.height = (self.baseHeight * sz) / 100

        self.symbolAnchor = {
            "x": ((anchor["x"] - self.bbox.x1 + sw + ow) * sz) / 100,
            "y": ((anchor["y"] - self.bbox.y1 + sw + ow) * sz) / 100,
        }

        if ms._autoValidation:
            if not self.isValid():
                print(f"Error in symbol: {self.options.get('sidc')}")

        return self

    def getMetadata(self):
        from .ms import ms

        # Default metadata structure
        metadata = {
            "activity": False,
            "affiliation": "undefined",
            "baseAffilation": "",
            "baseDimension": "",
            "baseGeometry": {"g": {}, "bbox": BBox()},
            "civilian": False,
            "condition": "",
            "context": "",
            "dimension": "undefined",
            "dimensionUnknown": False,
            "echelon": "",
            "faker": False,
            "feintDummy": False,
            "fill": self.style["fill"],
            "frame": self.style["frame"],
            "functionid": "",
            "headquarters": False,
            "installation": False,
            "joker": False,
            "mobility": "",
            "notpresent": "",
            "numberSIDC": False,
            "space": False,
            "STD2525": ms._STD2525,
            "taskForce": False,
            "unit": False,
            # Added
            "controlMeasure": False,
            "cyberspace": False,
            "landequipment": False,
            "dismounted": False,
            "_modifier1": "",
            "_modifier2": "",
            "leadership": "",  # Added from getmetadata.js check
        }

        mapping = {}
        mapping["context"] = ["Reality", "Exercise", "Simulation"]
        mapping["status"] = [
            "Present",
            "Planned",
            "FullyCapable",
            "Damaged",
            "Destroyed",
            "FullToCapacity",
        ]
        mapping["echelonMobility"] = {
            "11": "Team/Crew",
            "12": "Squad",
            "13": "Section",
            "14": "Platoon/detachment",
            "15": "Company/battery/troop",
            "16": "Battalion/squadron",
            "17": "Regiment/group",
            "18": "Brigade",
            "21": "Division",
            "22": "Corps/MEF",
            "23": "Army",
            "24": "Army Group/front",
            "25": "Region/Theater",
            "26": "Command",
            "31": "Wheeled limited cross country",
            "32": "Wheeled cross country",
            "33": "Tracked",
            "34": "Wheeled and tracked combination",
            "35": "Towed",
            "36": "Rail",
            "37": "Pack animals",
            "41": "Over snow (prime mover)",
            "42": "Sled",
            "51": "Barge",
            "52": "Amphibious",
            "61": "Short towed array",
            "62": "Long towed Array",
            "71": "Leader Individual",
            "72": "Deputy Individual",
        }
        mapping["affiliation"] = ["Hostile", "Friend", "Neutral", "Unknown"]
        mapping["dimension"] = ["Air", "Ground", "Sea", "Subsurface"]

        metadata["context"] = mapping["context"][0]

        if self.style["standard"]:
            metadata["STD2525"] = False if self.style["standard"] == "APP6" else True

        if self.style["monoColor"]:
            metadata["fill"] = False

        # string adjustments
        self.options["sidc"] = (
            str(self.options["sidc"]).replace("*", "-").replace(" ", "")
        )

        # Check if number base
        try:
            int(self.options["sidc"][:2])
            metadata["numberSIDC"] = True
        except ValueError:
            metadata["numberSIDC"] = False

        if metadata["numberSIDC"]:
            if hasattr(ms._getMetadata, "get") and ms._getMetadata.get("number"):
                metadata = ms._getMetadata["number"](self, ms, metadata, mapping)
            else:
                # TODO: Implement fallback or warning
                pass
        else:
            if hasattr(ms._getMetadata, "get") and ms._getMetadata.get("letter"):
                metadata = ms._getMetadata["letter"](self, ms, metadata, mapping)

        # Geometry lookup
        key = metadata["dimension"] + metadata["affiliation"]
        # ms._symbolGeometries is not yet fully populated in my port, but will be.
        # It's a dict.
        if hasattr(ms, "_symbolGeometries") and key in ms._symbolGeometries:
            metadata["baseGeometry"] = ms._symbolGeometries[key]
        else:
            metadata["baseGeometry"]["bbox"] = BBox()

        if not self.style["frame"] and not self.style["icon"]:
            if (
                hasattr(ms, "_symbolGeometries")
                and "PositionMarker" in ms._symbolGeometries
            ):
                metadata["baseGeometry"] = ms._symbolGeometries["PositionMarker"]

        return metadata

    def getColors(self):
        from .ms import ms

        def get_cm(mode):
            if isinstance(mode, dict):
                return mode
            return ms.getColorMode(mode)

        baseFillColor = get_cm(self.style["colorMode"])
        baseFrameColor = (
            get_cm(self.style["frameColor"])
            if self.style["frameColor"]
            else ms.getColorMode("FrameColor")
        )
        baseIconColor = (
            get_cm(self.style["iconColor"])
            if self.style["iconColor"]
            else ms.getColorMode("IconColor")
        )
        baseIconFillColor = baseFillColor

        baseColorBlack = ms.getColorMode("Black")
        baseColorWhite = ms.getColorMode("White")
        baseColorOffWhite = ms.getColorMode("OffWhite")
        baseColorNone = ms.getColorMode("None")

        # copy logic from getcolors.js
        # Cloning colors to avoid mutating the global definitions?
        # In Python we should be careful.
        # Ideally we create new dicts.
        # But here we are modifying 'baseFillColor' fields possibly.
        # Let's clone them for safety.
        import copy

        baseFillColor = copy.deepcopy(baseFillColor)
        baseFrameColor = copy.deepcopy(baseFrameColor)
        baseIconColor = copy.deepcopy(baseIconColor)

        if self.style["civilianColor"] and self.metadata["civilian"]:
            baseFillColor.Friend = baseFillColor.Neutral = baseFillColor.Unknown = (
                baseFillColor.Civilian
            )
            baseFrameColor.Friend = baseFrameColor.Neutral = baseFrameColor.Unknown = (
                baseFrameColor.Civilian
            )
            baseIconColor.Friend = baseIconColor.Neutral = baseIconColor.Unknown = (
                baseIconColor.Civilian
            )

        if self.metadata.get("joker") or self.metadata.get("faker"):
            baseFillColor.Friend = baseFillColor.Hostile
            baseFrameColor.Friend = baseFrameColor.Hostile
            baseIconColor.Friend = baseIconColor.Hostile

        if self.metadata.get("suspect"):
            # .Suspect attribute exists
            baseFillColor.Friend = baseFillColor.Hostile = baseFillColor.Suspect
            baseFrameColor.Friend = baseFrameColor.Hostile = baseFrameColor.Suspect
            baseIconColor.Friend = baseIconColor.Hostile = baseIconColor.Suspect

        if self.style["monoColor"]:
            mono = self.style["monoColor"]
            baseFrameColor.Friend = baseFrameColor.Neutral = baseFrameColor.Hostile = (
                baseFrameColor.Unknown
            ) = baseFrameColor.Civilian = mono
            baseColorBlack = baseFrameColor
            baseColorWhite = baseFillColor = baseColorNone

        colors = {
            "fillColor": baseFillColor,
            "frameColor": baseFrameColor,
            "iconColor": baseIconColor,
            "iconFillColor": baseIconFillColor,
            "none": baseColorNone,
            "black": baseColorBlack,
            "white": baseColorWhite,
        }

        # Logic for frame off
        if self.metadata["frame"]:
            if self.style["frameColor"]:
                colors["frameColor"] = get_cm(self.style["frameColor"])
            else:
                pass  # keep default
        else:
            colors["frameColor"] = baseColorNone

        if self.metadata["fill"]:
            if not self.metadata["frame"] and not (
                not self.metadata["frame"] and not self.style["icon"]
            ):
                colors["fillColor"] = baseColorNone
            else:
                colors["fillColor"] = baseFillColor

            colors["iconColor"] = (
                get_cm(self.style["iconColor"])
                if self.style["iconColor"]
                else baseColorBlack
            )

            colors["iconFillColor"] = (
                baseFillColor if not self.metadata["frame"] else baseColorOffWhite
            )
            colors["white"] = baseColorOffWhite
        else:
            colors["fillColor"] = baseColorNone
            colors["frameColor"] = (
                baseColorNone if not self.metadata["frame"] else baseFrameColor
            )
            colors["iconColor"] = baseFrameColor
            colors["iconFillColor"] = baseColorNone

            if (
                not self.metadata["frame"]
                and not self.metadata["fill"]
                and not self.style["icon"]
            ):
                colors["frameColor"] = baseColorBlack
                colors["fillColor"] = baseColorBlack

        return colors

    def isValid(self, extended=False):
        # Simple check
        def has_none(obj):
            if obj is None:
                return True
            if isinstance(obj, list):
                return any(has_none(x) for x in obj)
            if isinstance(obj, dict):
                return any(has_none(v) for v in obj.values())
            return False

        draw_valid = not has_none(self.drawInstructions)

        affiliation = self.metadata.get("affiliation")
        dimension = self.metadata.get("dimension")
        cm = self.metadata.get("controlMeasure")

        valid = (
            not (affiliation == "undefined" or (dimension == "undefined" and not cm))
            and draw_valid
            and self.validIcon
            # and self.metadata.mobility != undefined # handled by get
        )

        if extended:
            return {"valid": valid, "draw": draw_valid, "icon": self.validIcon}
        return valid

    def as_svg(self):
        from .ms import ms

        def process_instructions(instructions):
            svgxml = ""
            if isinstance(instructions, list):
                for instr in instructions:
                    if isinstance(instr, list):
                        if instr:
                            svgxml += process_instructions(instr)
                    elif isinstance(instr, dict):
                        # Instruction object
                        type_ = instr.get("type")
                        svg = ""
                        if type_ == "svg":
                            svg += instr.get("svg", "")
                        else:
                            # Clip path
                            if "clipPath" in instr:
                                svg += '<clipPath id="clip">'
                                svg += f'<path d="{instr["clipPath"]}" clip-rule="nonzero" />'
                                svg += "</clipPath>"

                            if type_ == "path":
                                d = instr.get("d", "")
                                svg += f'<path d="{d}" '
                                if "clipPath" in instr:
                                    svg += 'clip-path="url(#clip)" '
                            elif type_ == "circle":
                                svg += f'<circle cx="{instr.get("cx")}" cy="{instr.get("cy")}" r="{instr.get("r")}" '
                                if "clipPath" in instr:
                                    svg += 'clip-path="url(#clip)" '
                            elif type_ == "text":
                                svg += (
                                    f'<text x="{instr.get("x")}" y="{instr.get("y")}" '
                                )
                                svg += f'text-anchor="{instr.get("textanchor")}" '
                                svg += f'font-size="{instr.get("fontsize")}" '
                                svg += f'font-family="{instr.get("fontfamily")}" '
                                if instr.get("fontweight"):
                                    svg += f'font-weight="{instr["fontweight"]}" '
                                if instr.get("alignmentBaseline"):
                                    svg += f'dominant-baseline="{instr["alignmentBaseline"]}" '
                            elif type_ == "translate":
                                svg += f'<g transform="translate({instr.get("x")},{instr.get("y")})" '
                            elif type_ == "rotate":
                                svg += f'<g transform="rotate({instr.get("degree")},{instr.get("x")},{instr.get("y")})" '
                            elif type_ == "scale":
                                svg += f'<g transform="scale({instr.get("factor")})" '

                            # Stroke and Fill attributes
                            if (
                                "stroke" in instr
                                or "strokewidth" in instr
                                or "strokedasharray" in instr
                            ):
                                sw = instr.get("strokewidth", self.style["strokeWidth"])
                                nss = instr.get("non_scaling_stroke", 1)
                                final_sw = nss * sw
                                svg += f'stroke-width="{final_sw}" '

                                if instr.get("strokedasharray"):
                                    svg += f'stroke-dasharray="{instr["strokedasharray"]}" '
                                if instr.get("linecap"):
                                    svg += f'stroke-linecap="{instr["linecap"]}" stroke-linejoin="{instr["linecap"]}" '

                                stroke = instr.get("stroke")
                                if stroke:
                                    svg += f'stroke="{stroke}" '
                                else:
                                    svg += 'stroke="none" '

                            if "fill" in instr:
                                fill = instr["fill"]
                                svg += f'fill="{fill if fill else "none"}" '
                            if "fillopacity" in instr:
                                svg += f'fill-opacity="{instr["fillopacity"]}" '

                            svg += ">"

                            # Closing tags
                            if type_ == "path":
                                svg += "</path>"
                            elif type_ == "circle":
                                svg += "</circle>"
                            elif type_ == "text":
                                text = str(instr.get("text", ""))
                                text = (
                                    text.replace("&", "&amp;")
                                    .replace("<", "&lt;")
                                    .replace(">", "&gt;")
                                )
                                svg += f"{text}</text>"
                            elif type_ in ["translate", "rotate", "scale"]:
                                svg += process_instructions(instr.get("draw", []))
                                svg += "</g>"
                        svgxml += svg
            return svgxml

        xml = f'<svg xmlns="{ms._svgNS}" version="1.2" baseProfile="tiny" width="{self.width}" height="{self.height}" viewBox="{self.bbox.x1 - self.style["strokeWidth"] - self.style["outlineWidth"]} {self.bbox.y1 - self.style["strokeWidth"] - self.style["outlineWidth"]} {self.baseWidth} {self.baseHeight}">'
        xml += process_instructions(self.drawInstructions)
        xml += "</svg>"

    def get_desc(self):
        """
        Returns a human-readable description for the symbol.
        Format: "entity, entity_type [sector1 modifier, sector2 modifier] (echelon)"
        """
        sidc = self.options.get("sidc", "")

        # Basic check for numeric SIDC length (at least 20 chars)
        if not sidc or len(sidc) < 20 or not sidc.isdigit():
            return "Unknown Symbol"

        entities = MilStd2525Entities()
        mod1_lookup = MilStd2525Sector1Modifiers()
        mod2_lookup = MilStd2525Sector2Modifiers()

        entity_name = ""
        modifiers = []
        echelon = ""

        # 1. Entity (Digits 11-16)
        entity_code = sidc[10:16]
        entity_obj = entities[entity_code]
        if entity_obj:
            entity_name = entity_obj.get_label()

        # 2. Modifiers
        mod1_prefix = sidc[20] if len(sidc) > 20 else "0"
        mod2_prefix = sidc[21] if len(sidc) > 21 else "0"
        mod1_suffix = sidc[16:18]
        mod2_suffix = sidc[18:20]

        mod1_code = mod1_prefix + mod1_suffix
        mod2_code = mod2_prefix + mod2_suffix

        if mod1_code and mod1_code != "000":
            mod1 = mod1_lookup[mod1_code]
            if mod1:
                modifiers.append(mod1.name)

        if mod2_code and mod2_code != "000":
            mod2 = mod2_lookup[mod2_code]
            if mod2:
                modifiers.append(mod2.name)

        # 3. Echelon / Mobility (Digits 9-10)
        echelon_mobility = sidc[8:10]
        echelon_map = {
            "11": "Team/Crew",
            "12": "SQD",
            "13": "SEC",
            "14": "PLT/DET",
            "15": "CO/BAT/TRP",
            "16": "BN/SQDN",
            "17": "REG/GRP",
            "18": "BDE",
            "21": "DIV",
            "22": "Corps/MEF",
            "23": "Army",
            "24": "Army Group/front",
            "25": "Region/Theater",
            "26": "Command",
            "31": "Wheeled limited cross country",
            "32": "Wheeled cross country",
            "33": "Tracked",
            "34": "Wheeled and tracked combination",
            "35": "Towed",
            "36": "Rail",
            "37": "Pack animals",
            "41": "Over snow (prime mover)",
            "42": "Sled",
            "51": "Barge",
            "52": "Amphibious",
            "61": "Short towed array",
            "62": "Long towed Array",
            "71": "Leader Individual",
            "72": "Deputy Individual",
        }
        if echelon_mobility in echelon_map:
            echelon = echelon_map[echelon_mobility]

        # Construct Name
        # Format: "entity, entity_type [sector1 modifier, sector2 modifier] (echelon)"
        parts = []
        if entity_name:
            parts.append(entity_name)

        if modifiers:
            parts.append(f"[{', '.join(modifiers)}]")

        if echelon:
            parts.append(f"({echelon})")

        if not parts:
            return "Unknown Symbol"

        return " ".join(parts)

    def toDataURL(self):
        # Renders SVG to Data URL (base64)
        # But user wants PNG export.
        # "Add the ability to export the symbols as PNG images."
        # I'll implement as_png() using cairosvg instead of toDataURL
        return "data:image/svg+xml;utf8," + self.as_svg()

    def as_png(self, filename=None):
        import cairosvg

        svg = self.as_svg()
        if filename:
            cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=filename)
        else:
            return cairosvg.svg2png(bytestring=svg.encode("utf-8"))
