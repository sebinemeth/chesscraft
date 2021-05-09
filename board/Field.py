from enums.FieldOccupation import FieldOccupation
from figure.Figure import Figure
from player.Player import Player


class Field:
    def __init__(self, x, y, figure: Figure = None):
        self.x = x
        self.y = y
        self._figure = figure

    @property
    def figure(self):
        return self._figure

    def add_figure(self, figure: Figure):
        self._figure = figure
        self._figure.set_position(self.x, self.y)

    def remove_figure(self):
        f = self._figure
        self._figure = None
        return f

    def get_occupation_type(self, player: Player) -> FieldOccupation:
        if self._figure is None:
            return FieldOccupation.EMPTY
        else:
            if self._figure.owner == player:
                return FieldOccupation.FRIENDLY
            else:
                return FieldOccupation.ENEMY

    def export_state(self):
        if self.figure is None:
            return None
        return self.figure.export_state()
