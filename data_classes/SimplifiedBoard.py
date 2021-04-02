from dataclasses import dataclass
from typing import Tuple

from enums.FieldOccupation import FieldOccupation


class SimplifiedBoard(dataclass):
    fields: Tuple[Tuple[FieldOccupation]]
