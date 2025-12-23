from dataclasses import dataclass
from typing import List


@dataclass
class MilStd2525Entity:
    hierarchy: List[str]
    value: str
    edition: str

    def get_label(self) -> str:
        """
        Returns a human-readable label based on the hierarchy:
        - If only one element exists, returns that element.
        - Otherwise, returns a comma-separated string of the 2nd and 3rd elements.
        """
        if len(self.hierarchy) == 1:
            return self.hierarchy[0]

        return ", ".join(self.hierarchy[1:3])
