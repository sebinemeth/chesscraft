from figure.Figure import Figure
from enums.FieldOccupation import FieldOccupation
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
        self._figure = None

    def get_occupation_type(self, player: Player) -> FieldOccupation:
        if self._figure is None:
            return FieldOccupation.EMPTY
        else:
            if self._figure.owner == player:
                return FieldOccupation.FRIENDLY
            else:
                return FieldOccupation.ENEMY

    def get_all_data(self):
        pass
