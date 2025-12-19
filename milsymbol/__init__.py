from .ms.ms import ms
from .ms.symbol import Symbol

# Expose ms and Symbol
# In JS: import { ms } from "./ms.js"; import Symbol from "./ms/symbol.js"; ms.Symbol = Symbol; export { ms };
ms.Symbol = Symbol

from .symbolfunctions.basegeometry import basegeometry
from .symbolfunctions.icon import icon
from .symbolfunctions.modifier import modifier
from .symbolfunctions.statusmodifier import statusmodifier
from .symbolfunctions.engagmentbar import engagmentbar
from .symbolfunctions.affliationdimension import affliationdimension
from .symbolfunctions.textfields import textfields
from .symbolfunctions.directionarrow import directionarrow

ms.addSymbolPart(basegeometry)
ms.addSymbolPart(icon)
ms.addSymbolPart(modifier)
ms.addSymbolPart(statusmodifier)
ms.addSymbolPart(engagmentbar)
ms.addSymbolPart(affliationdimension)
ms.addSymbolPart(textfields)
ms.addSymbolPart(directionarrow)

from .symbolfunctions.symbolgeometries import load_symbol_geometries

load_symbol_geometries(ms)

# Import definitions
from .lettersidc import std2525b, std2525c, app6b
from .numbersidc import std2525d

# Add icons to ms
ms.addIcons(std2525b)
ms.addIcons(std2525c)
ms.addIcons(app6b)
ms.addIcons(std2525d)

# but the user requested 1:1 port.
# JS index.js:
# import { ms } from "./index.mjs";
# import { app6b, std2525b, ... } from "./index.mjs";
# ms.addIcons(app6b); ...

# So we should probably do the same here if we want 1:1 exact behavior on import.
# However, I haven't ported the icon sets yet. I will add them later.

__all__ = ["ms", "Symbol"]
