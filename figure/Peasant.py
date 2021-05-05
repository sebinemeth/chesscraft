from figure.Figure import Figure
from data_classes.SimplifiedBoard import SimplifiedBoard
from utils.balazs_utils import is_enemy_field
from utils.balazs_utils import is_empty_field
from player.Player import Player

from typing import List


class Peasant(Figure):
    def __init__(self, owner: Player):
        super(Figure, self).__init__()
        self.owner = owner

    def collect_possible_steps(self, simple_board: SimplifiedBoard):  # -> List[(int, int)]:
        if is_empty_field(self.x + self.owner.direction_signed_1, self.y, simple_board):
            return [(self.x + self.owner.direction_signed_1, self.y)]
        else:
            return []

    def collect_possible_attacks(self, simple_board: SimplifiedBoard):  # -> List[(int, int)]:
        ret = []
        candidate_x = self.x + self.owner.direction_signed_1
        candidate_y = self.y + 1
        if is_enemy_field(candidate_x, candidate_y, simple_board):
            ret.append((candidate_x, candidate_y))
        candidate_y = self.y - 1
        if is_enemy_field(candidate_x, candidate_y, simple_board):
            ret.append((candidate_x, candidate_y))
        return ret

    def get_all_data(self):
        return "P" + self.x + self.y;