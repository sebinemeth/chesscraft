from board.Field import Field
from data_classes.SimplifiedBoard import SimplifiedBoard
from data_classes.FigureActOptions import FigureActOptions
from enums.FieldOccupation import FieldOccupation
from figure.Figure import Figure
from figure.Peasant import Peasant
from player.Player import Player
from enums.Direction import Direction
from player.PlayerManager import PlayerManager


class Board:
    """ Store fields. Handle figure choosing, stepping, attacking... maybe fog of war too. """
    SIZE = 8

    def __init__(self):
        self.fields = tuple(tuple(Field(x, y) for y in range(Board.SIZE)) for x in range(Board.SIZE))

        for i in range(Board.SIZE):  # TODO this is not good yet
            self.fields[1][i].add_figure(Peasant(PlayerManager.get_instance().my_player))
            self.fields[Board.SIZE - 1][i].add_figure(Peasant(PlayerManager.get_instance().other_player))
            # TODO add figures other figures to fields
        # TODO refactor the vars below into state?
        self.chosen_field = None  # type: Field
        self.acts = None  # type: FigureActOptions

    def field_clicked(self, x: int, y: int):
        # TODO do something based use state pattern here? - I don't wanna - said Balázs
        player = PlayerManager.get_instance().my_player
        occupation = self.fields[x][y].get_occupation_type(player)
        if occupation == FieldOccupation.FRIENDLY:  # choosing figure
            self.chosen_field = self.fields[x][y]
            self.acts = self.chosen_field.figure.chosen(self.create_simplified_board(player))
        else:  # acting with chosen figure
            if self.chosen_field is None:
                return False    # do nothing
            else:
                we_found_it = False
                  # The clicked field was not in the possible_attacks or in the possible steps
                fig = self.chosen_field.figure  # type: Figure
                if occupation == FieldOccupation.EMPTY:  # step
                    for field in self.acts.possible_steps:
                        if field == (x, y):
                            we_found_it = True
                    if not we_found_it:
                        return False
                    self.fields[x][y].add_figure(fig)  # occupy new field
                    self.chosen_field.remove_figure()  # abandon old field
                if occupation == FieldOccupation.ENEMY:  # attack
                    for field in self.acts.possible_attacks:
                        if field == (x, y):
                            we_found_it = True
                    if not we_found_it:
                        return False
                    self.fields[x][y].remove_figure()  # killing figure there
                    self.fields[x][y].add_figure(fig)  # occupy new field
                    self.chosen_field.remove_figure()  # abandon old field
                self.chosen_field = None    # reset chosen field
                self.acts = None             # reset acts

    def update(self) -> bool:  # TODO figure out how this will work
        pass

    def create_simplified_board(self, player: Player) -> SimplifiedBoard:
        return SimplifiedBoard(tuple(tuple(self.fields[x][y].get_occupation_type(player)
                                           for y in range(Board.SIZE))
                                     for x in range(Board.SIZE)))

    def info_for_networking(self):
