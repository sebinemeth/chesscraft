class Field:
    def __init__(self, x, y, figure=None):
        self.x = x
        self.y = y
        self._figure = figure

    @property
    def figure(self):
        return self._figure

    def add_figure(self, figure):
        self._figure = figure

    def remove_figure(self):
        self._figure = None
