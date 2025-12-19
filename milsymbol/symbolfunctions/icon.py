def icon(symbol, ms):
    drawArray1 = []
    drawArray2 = []
    gbbox = ms.BBox({"x1": 50, "x2": 150, "y1": 50, "y2": 150})
    icons = None
    iconColor = None

    iconParts = []
    m1 = []
    m2 = []
    specialbbox = {}

    if symbol.style.get("icon"):
        fill_colors = symbol.colors.get("fillColor")

        # Helper to get color
        def get_color(color_obj, affiliation):
            if isinstance(color_obj, dict):
                return color_obj.get(affiliation)
            return getattr(color_obj, affiliation, None)

        affiliation = symbol.metadata.get("affiliation")
        fillColor = get_color(fill_colors, affiliation)
        neutralColor = get_color(fill_colors, "Neutral")

        icon_colors = symbol.colors.get("iconColor")
        iconColor = get_color(icon_colors, affiliation)

        icon_fill_colors = symbol.colors.get("iconFillColor")
        iconFillColor = get_color(icon_fill_colors, affiliation)

        none_colors = symbol.colors.get("none")
        none = get_color(none_colors, affiliation)

        black_colors = symbol.colors.get("black")
        black = get_color(black_colors, affiliation)

        white_colors = symbol.colors.get("white")
        white = get_color(white_colors, affiliation)

        # Store previous used icons in memory.
        icnet = (
            "standard:"
            + ("2525" if symbol.metadata.get("STD2525") else "APP6")
            + ",edition:"
            + str(symbol.metadata.get("edition") or "")
            + ","
            + str(symbol.metadata.get("dimension"))
            + str(symbol.metadata.get("affiliation"))
            + str(symbol.metadata.get("notpresent"))
            + str(symbol.metadata.get("numberSIDC"))
            + ",frame:"
            + str(symbol.style.get("frame"))
            + ",alternateMedal:"
            + str(symbol.style.get("alternateMedal"))
            + ",colors:{fillcolor:"
            + str(fillColor)
            + ",neutralColor:"
            + str(
                neutralColor
            )  # fixed typo in JS string concat if any, but sticking to JS logic mostly ok
            + ",iconColor:"
            + str(iconColor)
            + ",iconFillColor:"
            + str(iconFillColor)
            + ",none:"
            + str(none)
            + ",black:"
            + str(black)
            + ",white:"
            + str(white)
            + "}"
        )
        # JS typo "neutralColor" + neutralColor (missing colon or comma?)
        # JS: ",neutralColor" + neutralColor +
        # Python: let's reproduce the string exactly just in case key matters,
        # but really it's just a unique key.

        if icnet in ms._iconCache:
            cached = ms._iconCache[icnet]
            iconParts = cached.get("iconParts", [])
        else:
            ms._iconCache[icnet] = {}
            try:
                iconParts = ms._getIconParts(
                    symbol.metadata,
                    symbol.colors,
                    symbol.metadata.get("STD2525"),
                    symbol.style.get("monoColor"),
                    symbol.style.get("alternateMedal"),
                )
                ms._iconCache[icnet]["iconParts"] = iconParts
            except Exception:
                del ms._iconCache[icnet]
                raise

        # Letter based SIDCs
        if not symbol.metadata.get("numberSIDC"):
            functionid = symbol.metadata.get("functionid")

            # Sea mine exercise fix
            if functionid in ["WMGX--", "WMMX--", "WMFX--", "WMX---", "WMSX--"]:
                gbbox.y1 = 10
                if affiliation != "Unknown":
                    # JS: gbbox.x2 = this.metadata.baseGeometry.bbox.x2 + 20;
                    # We need baseGeometry bbox.
                    bg_bbox = symbol.metadata.get("baseGeometry", {}).get("bbox")
                    if bg_bbox:
                        gbbox.x2 = bg_bbox.x2 + 20

            # Try to fetch icons from cache
            if "letterSIDC" in ms._iconCache[icnet]:
                cached_letter = ms._iconCache[icnet]["letterSIDC"]
                icons = cached_letter.get("icons")
                specialbbox = cached_letter.get("bbox")
            else:
                get_icons_letter = ms._getIcons.get("letter")
                if callable(get_icons_letter):
                    # ms._getIcons.letter(ms, iconParts, STD2525)
                    ret = get_icons_letter(
                        ms, iconParts, symbol.metadata.get("STD2525")
                    )
                    ms._iconCache[icnet]["letterSIDC"] = ret
                    icons = ret.get("icons")
                    specialbbox = ret.get("bbox")
                else:
                    print("Warning: ms._getIcons.letter() is not present.")

        # Number based SIDCs
        if symbol.metadata.get("numberSIDC"):
            sidc = str(symbol.options.get("sidc"))
            symbolSet = sidc[4:6]

            cached_number = ms._iconCache[icnet].get("numberSIDC")

            # Check cache structure
            # JS: ms._iconCache[icnet].numberSIDC.symbolSet[symbolSet]
            # If cached_number is None, initialize it
            if cached_number is None:
                cached_number = {}
                ms._iconCache[icnet]["numberSIDC"] = cached_number
                cached_number["symbolSet"] = {}

            if hasattr(cached_number, "get") and "symbolSet" not in cached_number:
                cached_number["symbolSet"] = {}

            symbol_set_cache = cached_number.get("symbolSet")

            if symbolSet in symbol_set_cache:
                cached_set = symbol_set_cache[symbolSet]
                icons = cached_set.get("icons")
                m1 = cached_set.get("m1")
                m2 = cached_set.get("m2")
                specialbbox = cached_set.get("bbox")
            else:
                get_icons_number = ms._getIcons.get("number")
                if callable(get_icons_number):
                    # ms._getIcons.number(ms, symbolSet, iconParts, STD2525, edition)
                    ret = get_icons_number(
                        symbol,
                        ms,
                        symbolSet,
                        iconParts,
                        symbol.metadata.get("STD2525"),
                        symbol.metadata.get("edition"),
                    )
                    symbol_set_cache[symbolSet] = ret
                    icons = ret.get("icons")
                    m1 = ret.get("m1")
                    m2 = ret.get("m2")
                    specialbbox = ret.get("bbox")
                else:
                    print("Warning: ms._getIcons.number() is not present.")

        # Put all together
        # Re-get iconColor (JS line 241 repeats this)
        iconColor = get_color(icon_colors, affiliation)

        undefinedIcon = [
            {
                "type": "path",
                "stroke": False,
                "fill": iconColor,
                "d": "m 94.8206,78.1372 c -0.4542,6.8983 0.6532,14.323 5.3424,19.6985 4.509,5.6933 11.309,9.3573 14.98,15.7283 3.164,6.353 -0.09,14.245 -5.903,17.822 -7.268,4.817 -18.6219,2.785 -22.7328,-5.249 -1.5511,-2.796 -2.3828,-5.931 -2.8815,-9.071 -3.5048,0.416 -7.0093,0.835 -10.5142,1.252 0.8239,8.555 5.2263,17.287 13.2544,21.111 7.8232,3.736 17.1891,3.783 25.3291,1.052 8.846,-3.103 15.737,-11.958 15.171,-21.537 0.05,-6.951 -4.272,-12.85 -9.134,-17.403 -4.526,-4.6949 -11.048,-8.3862 -12.401,-15.2748 -1.215,-2.3639 -0.889,-8.129 -0.889,-8.129 z m -0.6253,-20.5177 0,11.6509 11.6527,0 0,-11.6509 z",
            }
        ]

        if symbol.metadata.get("numberSIDC"):
            functionid = symbol.metadata.get("functionid")
            # Number based SIDC
            # JS: let mainIcon = icons[this.metadata.functionid.substr(0, 6)];
            key = functionid[0:6]
            mainIcon = icons.get(key) if icons else None

            if mainIcon is None and int(functionid[4:6] or 0) >= 95:
                # Special entity subtype
                alt_key = functionid[0:4] + "00"
                mainIcon = icons.get(alt_key) if icons else None

            if mainIcon is None:
                if not (key == "000000" or key == ""):
                    drawArray2.append(undefinedIcon)
                    symbol.validIcon = False
            else:
                # Special cases for dismounted individual
                sidc = str(symbol.options.get("sidc"))
                symbolSet = sidc[4:6]
                mainSIDC = int(key) if key.isdigit() else 0

                # JS scaling logic
                # ... (list of scaling exceptions)
                no_scale_list = [
                    130100,
                    170000,
                    170400,
                    170600,
                    170700,
                    170800,
                    170900,
                    171100,
                    200200,
                    200300,
                    200600,
                    200700,
                    200800,
                    200900,
                    201100,
                    201301,
                    201302,
                    201400,
                    210100,
                    210200,
                    210300,
                    210400,
                    210500,
                    230200,
                    250000,
                ]

                should_scale = False
                if symbolSet == "27" and 110301 <= mainSIDC <= 110403:
                    should_scale = True
                elif symbolSet == "15" and mainSIDC not in no_scale_list:
                    should_scale = True

                if should_scale:
                    mod1 = symbol.metadata.get("_modifier1")
                    mod2 = symbol.metadata.get("_modifier2")

                    if mod1 != "000" and mod2 != "000":
                        mainIcon = [ms._scale(0.45, mainIcon, True)]
                    elif mod1 == "000" and mod2 != "000":
                        mainIcon = [
                            ms._translate(0, -10, ms._scale(0.7, mainIcon, True))
                        ]
                    elif mod1 != "000" and mod2 == "000":
                        mainIcon = [
                            ms._translate(0, 10, ms._scale(0.7, mainIcon, True))
                        ]
                    elif mod1 == "000" and mod2 == "000":
                        mainIcon = [ms._scale(1, mainIcon, True)]

                drawArray2.append(mainIcon)

            # Special bbox
            if specialbbox and key in specialbbox:
                gbbox = ms.BBox(specialbbox[key])

            # Support parts
            sub_id = functionid[4:6]
            if (
                sub_id == "95"
                and "GR.IC.FF.HEADQUARTERS OR HEADQUARTERS ELEMENT" in iconParts
            ):
                drawArray2.append(
                    iconParts["GR.IC.FF.HEADQUARTERS OR HEADQUARTERS ELEMENT"]
                )
            if sub_id == "96" and "GR.IC.FF.DIVISION AND BELOW SUPPORT" in iconParts:
                drawArray2.append(iconParts["GR.IC.FF.DIVISION AND BELOW SUPPORT"])
            if sub_id == "97" and "GR.IC.FF.CORPS SUPPORT" in iconParts:
                drawArray2.append(iconParts["GR.IC.FF.CORPS SUPPORT"])
            if sub_id == "98" and "GR.IC.FF.THEATRE SUPPORT" in iconParts:
                drawArray2.append(iconParts["GR.IC.FF.THEATRE SUPPORT"])

            # Modifiers 1 & 2
            mod1_code = symbol.metadata.get("_modifier1", "000")
            if mod1_code[0] == "0":
                if functionid[6:8] != "00":
                    modifier1 = m1.get(functionid[6:8]) if m1 else None
                    if modifier1 is None:
                        symbol.validIcon = False
                    else:
                        drawArray2.append(modifier1)
            else:
                modifier1 = m1.get(mod1_code) if m1 else None
                if modifier1 is None:
                    symbol.validIcon = False
                else:
                    drawArray2.append(modifier1)

            mod2_code = symbol.metadata.get("_modifier2", "000")
            if mod2_code[0] == "0":
                if functionid[8:10] != "00":
                    modifier2 = m2.get(functionid[8:10]) if m2 else None
                    if modifier2 is None:
                        symbol.validIcon = False
                    else:
                        drawArray2.append(modifier2)
            else:
                modifier2 = m2.get(mod2_code) if m2 else None
                if modifier2 is None:
                    symbol.validIcon = False
                else:
                    drawArray2.append(modifier2)
        else:
            # Letter based SIDC
            sidc = symbol.options.get("sidc")
            genericSIDC = sidc[0:1] + "-" + sidc[2:3] + "-" + sidc[4:10]

            if icons and genericSIDC in icons:
                drawArray2.append(icons[genericSIDC])
            else:
                if not (sidc[4:10] == "------" or sidc[4:10] == ""):
                    drawArray2.append(undefinedIcon)
                    symbol.validIcon = False

            if specialbbox and genericSIDC in specialbbox:
                gbbox = ms.BBox(specialbbox[genericSIDC])

    # outline
    if (
        not (symbol.style.get("frame") and symbol.metadata.get("fill"))
        or symbol.style.get("monoColor")
        or symbol.metadata.get("controlMeasure")
    ):
        if symbol.style.get("outlineWidth", 0) > 0:
            outline_color_obj = symbol.style.get("outlineColor")
            outline_color = outline_color_obj
            if isinstance(outline_color_obj, dict) or hasattr(
                outline_color_obj, "Friend"
            ):
                outline_color = get_color(
                    outline_color_obj, symbol.metadata.get("affiliation")
                )

            outlined = ms.outline(
                drawArray2,
                symbol.style.get("outlineWidth"),
                symbol.style.get("strokeWidth"),
                outline_color,
            )
            if outlined:
                drawArray1.append(outlined)

    return {"pre": drawArray1, "post": drawArray2, "bbox": gbbox}
