from dataclasses import dataclass
from typing import Optional


@dataclass
class MilStd2525Modifier:
    name: str
    value: str
    edition: str
    category: Optional[str] = None
    remarks: Optional[str] = None
