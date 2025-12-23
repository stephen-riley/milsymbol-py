from .ms.ms import ms
from .ms.symbol import Symbol

# Lookup classes
from .ms.lookup.entities import MilStd2525Entities
from .ms.lookup.modifiers import MilStd2525Sector1Modifiers, MilStd2525Sector2Modifiers

# Expose ms and Symbol
# In JS: import { ms } from "./ms.js"; import Symbol from "./ms/symbol.js"; ms.Symbol = Symbol; export { ms };
ms.Symbol = Symbol

from .symbolfunctions.basegeometry import basegeometry  # noqa: E402
from .symbolfunctions.icon import icon  # noqa: E402
from .symbolfunctions.modifier import modifier  # noqa: E402
from .symbolfunctions.statusmodifier import statusmodifier  # noqa: E402
from .symbolfunctions.engagmentbar import engagmentbar  # noqa: E402
from .symbolfunctions.affliationdimension import affliationdimension  # noqa: E402
from .symbolfunctions.textfields import textfields  # noqa: E402
from .symbolfunctions.directionarrow import directionarrow  # noqa: E402

ms.addSymbolPart(basegeometry)
ms.addSymbolPart(icon)
ms.addSymbolPart(modifier)
ms.addSymbolPart(statusmodifier)
ms.addSymbolPart(engagmentbar)
ms.addSymbolPart(affliationdimension)
ms.addSymbolPart(textfields)
ms.addSymbolPart(directionarrow)

from .symbolfunctions.symbolgeometries import load_symbol_geometries  # noqa: E402

load_symbol_geometries(ms)

# Import definitions
from .lettersidc import std2525b, std2525c, app6b  # noqa: E402
from .numbersidc import std2525d, std2525e, app6d  # noqa: E402

# Add icons to ms
ms.addIcons(std2525b)
ms.addIcons(std2525c)
ms.addIcons(app6b)
ms.addIcons(std2525d)
ms.addIcons(std2525e)
ms.addIcons(app6d)

# but the user requested 1:1 port.
# JS index.js:
# import { ms } from "./index.mjs";
# import { app6b, std2525b, ... } from "./index.mjs";
# ms.addIcons(app6b); ...

# So we should probably do the same here if we want 1:1 exact behavior on import.
# However, I haven't ported the icon sets yet. I will add them later.


__all__ = [
    "ms",
    "Symbol",
    "MilStd2525Entities",
    "MilStd2525Sector1Modifiers",
    "MilStd2525Sector2Modifiers",
]
