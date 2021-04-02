from dataclasses import dataclass
from typing import List

from enums.FieldOccupation import FieldOccupation


class SimplifiedBoard(dataclass):
    fields: List[List[FieldOccupation]]

