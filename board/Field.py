from figure.Figure import Figure


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
