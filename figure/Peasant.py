from figure.Figure import Figure
from data_classes.SimplifiedBoard import SimplifiedBoard
from enums.FieldOccupation import FieldOccupation
from player.Player import Player

from typing import List


class Peasant(Figure):
    def __init__(self, owner: Player):
        super(Figure, self).__init__(owner)

    def collect_possible_steps(self, simple_board: SimplifiedBoard): #-> List[(int, int)]:
        if simple_board[self.x + self.owner.direction_signed_1][self.y] == FieldOccupation.EMPTY:
            return [(self.x + self.owner.direction_signed_1, self.y)]
        else:
            return []

    def collect_possible_attacks(self, simple_board: SimplifiedBoard): #-> List[(int, int)]:
        ret = []
        if simple_board[self.x + self.owner.direction_signed_1][self.y + 1] == FieldOccupation.ENEMY:
            ret.append((self.x + self.owner.direction_signed_1, self.y + 1))
        if simple_board[self.x + self.owner.direction_signed_1][self.y - 1] == FieldOccupation.ENEMY:
            ret.append((self.x + self.owner.direction_signed_1, self.y - 1))
        return ret
