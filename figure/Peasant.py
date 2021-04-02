from figure.Figure import Figure
from data_classes.SimplifiedBoard import SimplifiedBoard
from enums.FieldOccupation import FieldOccupation

from typing import List


class Peasant(Figure):
    def __init__(self, direction: int):
        super(Figure, self).__init__()
        self.direction = direction  # -1 or 1 TODO ensure this using enum TODO2 this might be player attribute

    def collect_possible_steps(self, simple_board: SimplifiedBoard) -> List[(int, int)]:
        if simple_board[self.x + self.direction][self.y] == FieldOccupation.EMPTY:
            return [(self.x + self.direction, self.y)]
        else:
            return []

    def collect_possible_attacks(self, simple_board: SimplifiedBoard) -> List[(int, int)]:
        ret = []
        if simple_board[self.x + self.direction][self.y + 1] == FieldOccupation.ENEMY:
            ret.append((self.x + self.direction, self.y + 1))
        if simple_board[self.x + self.direction][self.y - 1] == FieldOccupation.ENEMY:
            ret.append((self.x + self.direction, self.y - 1))
        return ret
