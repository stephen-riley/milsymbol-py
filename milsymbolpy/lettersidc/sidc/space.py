from ..metadata import metadata as metadata_letter
from ..geticons import geticons as getIcons_letter
from ...iconparts.space import space as icons


def space(ms, sId, bbox, icn, _STD2525):
    # SPACE =========================================================================
    sId["S-P-------"] = []
    sId["S-P-S-----"] = [icn["SP.I.FF.SATELLITE"]]
    sId["S-P-V-----"] = [icn["SP.I.FF.CREWED SPACE VEHICLE"]]
    sId["S-P-T-----"] = [icn["SP.I.FF.SPACE STATION"]]
    sId["S-P-L-----"] = [icn["SP.I.SPACE LAUNCH VEHICLE"]]


exports = {
    "type": "letter",
    "getMetadata": metadata_letter,
    "getIcons": getIcons_letter,
    "iconParts": [icons],
    "icons": space,
}
