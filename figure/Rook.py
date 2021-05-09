from data_classes.SimplifiedBoard import SimplifiedBoard
from figure.Figure import Figure
from player.Player import Player
from utils.balazs_utils import possible_fields_long_step, possible_attacks_long_step


class Rook(Figure):
    def __init__(self, owner: Player):
        super(Figure, self).__init__()
        self.owner = owner

    def collect_possible_steps(self, simple_board: SimplifiedBoard):  # -> List[(int, int)]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # direction of a step of a rook
        return possible_fields_long_step((self.x, self.y), directions, simple_board)

    def collect_possible_attacks(self, simple_board: SimplifiedBoard):  # -> List[(int, int)]:
        # ret = []
        # if simple_board.fields[self.x + self.owner.direction_signed_1][self.y + 1] == FieldOccupation.ENEMY:
        #     ret.append((self.x + self.owner.direction_signed_1, self.y + 1))
        # if simple_board.fields[self.x + self.owner.direction_signed_1][self.y - 1] == FieldOccupation.ENEMY:
        #     ret.append((self.x + self.owner.direction_signed_1, self.y - 1))
        # return ret
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # direction of a step of a rook
        return possible_attacks_long_step((self.x, self.y), directions, simple_board)

    def export_state(self):
        d = super().export_state()
        d.append("rook")
        return d
