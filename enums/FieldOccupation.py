from enum import Enum


class FieldOccupation(Enum):
    EMPTY = 0
    ENEMY = 1
    FRIENDLY = 2
    # TODO extend with in fog of war
