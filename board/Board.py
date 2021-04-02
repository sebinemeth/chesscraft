from board.Field import Field


class Board:
    """ Store fields. Handle figure choosing, stepping, attacking... maybe fog of war too. """
    SIZE = 8

    def __init__(self):
        self.fields = tuple(tuple(Field(x, y) for y in range(Board.SIZE)) for x in range(Board.SIZE))
        # TODO add figures to fields

    def field_clicked(self, x, y):
        # TODO do something based on state (select figure on field/step with figure there...)
        #   probably do with state pattern
        pass

    def check_mouse_clicks(self, events):
        # TODO check mouse events, position for mouse clicks -> call self.field_clicked
        pass

    def update(self, events, pressed_keys) -> bool:
        self.check_mouse_clicks(events)
        return True
