from dataclasses import dataclass
from typing import Tuple

from enums.FieldOccupation import FieldOccupation


class SimplifiedBoard:

    def __init__(self, tuple_of_tuple_of_occupations):
        self.fields = tuple_of_tuple_of_occupations


