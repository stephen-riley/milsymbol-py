def geticons(ms, iconParts, STD2525):
    iconSIDC = {}
    iconBbox = {}
    # ms._iconSIDC.letter is expected to be a dict of functions
    if hasattr(ms, "_iconSIDC") and "letter" in ms._iconSIDC:
        for func in ms._iconSIDC["letter"]:
            if callable(func):
                # The JS uses .call(this, ...) where this is the symbol instance.
                # However, geticons is called as ms._getIcons.letter(ms, iconParts, STD2525)
                # In JS: this depends on caller.
                # In icon.js: ms._getIcons.letter(ms, iconParts, this.metadata.STD2525)
                # So 'this' in icon.js is the symbol.
                # But here 'this' inside the loop call?
                # JS: ms._iconSIDC.letter[i].call(this, iconSIDC, iconBbox, iconParts, STD2525);
                # "this" refers to the context geticons was called with.
                # If geticons is called as a method of symbol, then 'this' is symbol.
                # If called as function, 'this' might be undefined or global.
                # Looking at icon.js line 92: ms._getIcons.letter(ms, iconParts, this.metadata.STD2525)
                # It is called as a property of ms._getIcons.
                # Unless ms._getIcons is the symbol? No, ms._getIcons is likely a dict of functions.
                # So 'this' would be ms._getIcons or undefined in strict mode?
                # Actually, wait.
                # In `milsymbol.js` (not seen yet), likely `getIcons` is assigned to `ms`.
                # Let's assume the SIDC functions don't need `this`.
                # Checking `2525b-ch2.js`:
                # icons: function std2525b(sId, bbox, icn, _STD2525) { ... }
                # It doesn't use `this`.
                # So passing (iconSIDC, iconBbox, iconParts, STD2525) is enough.

                func(ms, iconSIDC, iconBbox, iconParts, STD2525)

    return {"icons": iconSIDC, "bbox": iconBbox}
