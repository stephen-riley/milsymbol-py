from .sidc import (
    space,
    air,
    ground,
    equipment,
    installations,
    sea,
    subsurface,
    sof,
    signals_intelligence as signalsIntelligence,
    stabilityoperations,
    emergencymanagementsymbols,
    _2525b_ch2 as std2525bextra,
    tactical_points_2525 as tacticalpoints2525,
    tactical_points_app6 as tacticalpointsapp6,
)

app6b = [
    space.exports,
    air.exports,
    ground.exports,
    equipment.exports,
    installations.exports,
    sea.exports,
    subsurface.exports,
    sof.exports,
    tacticalpointsapp6.exports,
]

std2525b = [
    space.exports,
    air.exports,
    ground.exports,
    equipment.exports,
    installations.exports,
    sea.exports,
    subsurface.exports,
    sof.exports,
    signalsIntelligence.exports,
    stabilityoperations.exports,
    std2525bextra.exports,
    tacticalpoints2525.exports,
]

std2525c = [
    space.exports,
    air.exports,
    ground.exports,
    equipment.exports,
    installations.exports,
    sea.exports,
    subsurface.exports,
    sof.exports,
    signalsIntelligence.exports,
    stabilityoperations.exports,
    emergencymanagementsymbols.exports,
    tacticalpoints2525.exports,
]
