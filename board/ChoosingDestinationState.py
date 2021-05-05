from board.AbstractBoardState import AbstractBoardState
from data_classes.FigureActOptions import FigureActOptions
from player.PlayerManager import PlayerManager
from enums.FieldOccupation import FieldOccupation
from figure.Figure import Figure


class ChoosingDestinationState(AbstractBoardState):
    """ Handles simple moving/attacking. """
    def __init__(self, board):
        super(AbstractBoardState, self).__init__()
        self._board = board
        self.__possible_steps = []
        self.__possible_attacks = []
        self.__chosen_x = -1
        self.__chosen_y = -1

    def reset(self, **messages):
        self.__possible_steps = messages["possible_steps"]
        self.__possible_steps = messages["possible_acts"]
        self.__chosen_x = messages["chosen_x"]
        self.__chosen_y = messages["chosen_y"]

    def field_clicked(self, x: int, y: int):
        chosen_field = self.field_xy(self.__chosen_x, self.__chosen_y)
        clicked_field = self.field_xy(x, y)
        occupation = clicked_field.get_occupation_type(PlayerManager.get_instance().my_player)
        chosen_fig = chosen_field.figure
        if occupation == FieldOccupation.EMPTY and (x, y) in self.__possible_steps:  # step
            clicked_field.add_figure(chosen_fig)  # occupy new field
            chosen_field.remove_figure()  # abandon old field
        elif occupation == FieldOccupation.ENEMY and (x, y) in self.__possible_attacks:  # attack
            clicked_field.remove_figure()  # killing figure there
            clicked_field.add_figure(chosen_fig)  # occupy new field
            chosen_field.remove_figure()  # abandon old field
        self._board.transition_to(self._board.choosing_acting_figure_state)  # TODO somehow count player steps
