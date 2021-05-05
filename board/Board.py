import sys

from board.AbstractBoardState import AbstractBoardState
from board.ChoosingActingFigureState import ChoosingActingFigureState
from board.ChoosingDestinationState import ChoosingDestinationState
from board.Field import Field
from board.FrozenState import FrozenState
from data_classes.FigureActOptions import FigureActOptions
from data_classes.SimplifiedBoard import SimplifiedBoard
from figure.Peasant import Peasant
from player.Player import Player
from player.PlayerManager import PlayerManager


class Board:
    """ Store fields. Handle figure choosing, stepping, attacking... maybe fog of war too. """
    SIZE = 8

    def __init__(self):
        self.__state = None  # type: AbstractBoardState
        self.__frozen_state = FrozenState(self)
        self.__choosing_acting_figure_state = ChoosingActingFigureState(self)
        self.__choosing_destination_state = ChoosingDestinationState(self)
        self.fields = tuple(tuple(Field(x, y) for y in range(Board.SIZE)) for x in range(Board.SIZE))

        for i in range(Board.SIZE):  # TODO this is not good yet
            self.fields[1][i].add_figure(Peasant(PlayerManager.get_instance().my_player))
            self.fields[Board.SIZE - 1][i].add_figure(Peasant(PlayerManager.get_instance().other_player))
            # TODO add figures other figures to fields
        # TODO refactor the vars below into state?
        self.chosen_field = None  # type: Field
        self.acts = None  # type: FigureActOptions

    @property
    def state(self) -> AbstractBoardState:
        return self.__state

    # region specific state getters
    @property
    def frozen_state(self):
        return self.__frozen_state

    @property
    def choosing_acting_figure_state(self):
        return self.__choosing_acting_figure_state

    @property
    def choosing_destination_state(self):
        return self.__choosing_destination_state
    # endregion

    def field_clicked(self, x: int, y: int):
        self.state.field_clicked(x, y)

    def transition_to(self, state: AbstractBoardState, **messages):
        try:
            state.reset(**messages)
        except KeyError:
            print("Kedves Balázs, Marci vagy Sebi! Legyél szíves rendesen kezelni a messages szótárat!", sys.exc_info())
        self.__state = state

    def create_simplified_board(self, player: Player) -> SimplifiedBoard:
        return SimplifiedBoard(tuple(tuple(self.fields[x][y].get_occupation_type(player)
                                           for y in range(Board.SIZE))
                                     for x in range(Board.SIZE)))

    def export_json(self):
        json = []
        for row in self.fields:
            json.append([])
            for field in row:
                json[-1].append(field.export_json())
        return json

    def import_json(self):
        pass  # TODO
