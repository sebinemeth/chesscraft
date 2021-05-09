from board.AbstractBoardState import AbstractBoardState
from enums.FieldOccupation import FieldOccupation
from player.PlayerManager import PlayerManager


class ChoosingActingFigureState(AbstractBoardState):
    def field_clicked(self, x: int, y: int):
        my_player = PlayerManager.get_instance().my_player
        occupation = self.field_xy(x, y).get_occupation_type(my_player)
        if occupation == FieldOccupation.FRIENDLY:  # user clicked on its own player
            acts = self.field_xy(x, y).figure.chosen(self._board.create_simplified_board(my_player))
            self._board.transition_to(self._board.choosing_destination_state,
                                      possible_steps=acts.possible_steps, possible_attacks=acts.possible_attacks,
                                      chosen_x=x, chosen_y=y)
            return acts
        return None

    def type_of_state(self):
        return 'choosing_figure'
