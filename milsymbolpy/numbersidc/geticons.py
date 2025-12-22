def geticons(symbol, ms, symbolSet, iconParts, STD2525, edition):
    iconSIDC = {}
    iconModifier1 = {}
    iconModifier2 = {}
    iconBbox = {}

    # ms._iconSIDC['number'] expects list of functions
    if hasattr(ms, "_iconSIDC") and "number" in ms._iconSIDC:
        for func in ms._iconSIDC["number"]:
            # The SIDC functions (like landunit) take:
            # (symbol, sId, sIdm1, sIdm2, bbox, symbolSet, icn, _STD2525, edition)
            # We assume we pass symbol as first arg, just in case, though usually unused.
            func(
                ms,
                iconSIDC,
                iconModifier1,
                iconModifier2,
                iconBbox,
                symbolSet,
                iconParts,
                STD2525,
                edition,
            )

    return {
        "icons": iconSIDC,
        "m1": iconModifier1,
        "m2": iconModifier2,
        "bbox": iconBbox,
    }
