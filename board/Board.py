from board.Field import Field
from data_classes.SimplifiedBoard import SimplifiedBoard
from data_classes.FigureActOptions import FigureActOptions
from enums.FieldOccupation import FieldOccupation
from player.Player import Player
from enums.Direction import Direction


class Board:
    """ Store fields. Handle figure choosing, stepping, attacking... maybe fog of war too. """
    SIZE = 8

    def __init__(self):  # TODO create instance in Game when game starts
        self.fields = tuple(tuple(Field(x, y) for y in range(Board.SIZE)) for x in range(Board.SIZE))
        # TODO add figures to fields
        # TODO refactor the vars below into state?
        self.chosen_field = None  # type: Field
        self.acts = None  # type: FigureActOptions

    def field_clicked(self, x: int, y: int):
        # TODO do something based use state pattern here?
        # TODO check if current player is my player (don't let clients control the enemy's figures!)
        #   if not, then return/only show some detailed info of field or something like that
        player = Player(Direction.LEFT)  # TODO use PlayerManager's current/my player instead
        occupation = self.chosen_field.get_occupation_type(player)
        if self.chosen_field is None and occupation == FieldOccupation.FRIENDLY:  # choosing figure
            self.chosen_field = self.fields[x][y]
            self.acts = self.chosen_field.figure.chosen(self.create_simplified_board(player))
        if self.chosen_field is not None:  # acting with chosen figure (with the assumption
            fig = self.chosen_field.figure
            if occupation == FieldOccupation.EMPTY:  # step
                self.fields[x][y].add_figure(fig)  # occupy new field
                self.chosen_field.remove_figure()  # abandon old field
            if occupation == FieldOccupation.ENEMY:  # attack
                self.fields[x][y].remove_figure()  # killing figure there
                self.fields[x][y].add_figure(fig)  # occupy new field
                self.chosen_field.remove_figure()  # abandon old field

    def check_mouse_clicks(self, events):
        # TODO check mouse events, position for mouse clicks -> call self.field_clicked
        pass

    def update(self, events, pressed_keys) -> bool:  # TODO call this update from Game's update (if game is running)
        self.check_mouse_clicks(events)
        return True

    def create_simplified_board(self, player: Player) -> SimplifiedBoard:
        return SimplifiedBoard(tuple(tuple(self.fields[x][y].get_occupation_type(player)
                                           for y in range(Board.SIZE))
                                     for x in range(Board.SIZE)))
