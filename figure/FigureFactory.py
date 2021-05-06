from abc import ABC

from figure.Peasant import Peasant
from figure.Rook import Rook


class FigureFactory(ABC):
    @staticmethod
    def get_figure(figure_type, player):
        if figure_type == 'peasant':
            return Peasant(player)
        if figure_type == 'rook':
            return Rook(player)
        # TODO other figures
        return None
