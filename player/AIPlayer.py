from AI.Strategies import randomly_attack
from player.Player import Player


class AIPlayer(Player):

    def turn_started(self, board):
        randomly_attack(self, board)
        board.transition_to(board.choosing_acting_figure_state)
        return False
