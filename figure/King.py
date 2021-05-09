from data_classes.SimplifiedBoard import SimplifiedBoard
from figure.Figure import Figure
from player.Player import Player
from utils.balazs_utils import possible_fields_one_step, possible_attacks_one_step


class King(Figure):
    def __init__(self, owner: Player):
        super(Figure, self).__init__()
        self.owner = owner
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def collect_possible_steps(self, simple_board: SimplifiedBoard):  # -> List[(int, int)]:
        return possible_fields_one_step((self.x, self.y), self.directions, simple_board)

    def collect_possible_attacks(self, simple_board: SimplifiedBoard):  # -> List[(int, int)]:
        return possible_attacks_one_step((self.x, self.y), self.directions, simple_board)

    def export_state(self):
        d = super().export_state()
        d['figure_name'] = "king"
        return d
