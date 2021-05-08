from data_classes.SimplifiedBoard import SimplifiedBoard
from enums.FieldOccupation import FieldOccupation
from utils.balazs_utils import possible_fields_one_step, possible_attacks_one_step
from figure.Figure import Figure
from player.Player import Player


class Peasant(Figure):
    def __init__(self, owner: Player):
        super(Figure, self).__init__()
        self.owner = owner
        self.step_direction = [(self.owner.direction_signed_1, 0)]
        self.attack_direction = [(self.owner.direction_signed_1, 1), (self.owner.direction_signed_1, -1)]

    def collect_possible_steps(self, simple_board: SimplifiedBoard): #-> List[(int, int)]:
        # if simple_board[self.x + self.owner.direction_signed_1][self.y] == FieldOccupation.EMPTY:
        #     return [(self.x + self.owner.direction_signed_1, self.y)]
        # else:
        #     return []
        # TODO: double step from the first row
        return possible_fields_one_step((self.x, self.y), self.step_direction, simple_board)


    def collect_possible_attacks(self, simple_board: SimplifiedBoard):  # -> List[(int, int)]:
        # ret = []
        # if simple_board[self.x + self.owner.direction_signed_1][self.y + 1] == FieldOccupation.ENEMY:
        #     ret.append((self.x + self.owner.direction_signed_1, self.y + 1))
        # if simple_board[self.x + self.owner.direction_signed_1][self.y - 1] == FieldOccupation.ENEMY:
        #     ret.append((self.x + self.owner.direction_signed_1, self.y - 1))
        # return ret
        # TODO: en_passant
        return possible_attacks_one_step((self.x, self.y), self.attack_direction, simple_board)


    def export_state(self):
        d = super().export_state()
        d['figure_name'] = "peasant"
        return d
