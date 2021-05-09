from abc import ABC

from figure.Bishop import Bishop
from figure.King import King
from figure.Knight import Knight
from figure.Peasant import Peasant
from figure.Queen import Queen
from figure.Rook import Rook


class FigureFactory(ABC):
    @staticmethod
    def get_figure(figure_type, player):
        if figure_type == 'peasant':
            return Peasant(player)
        if figure_type == 'rook':
            return Rook(player)
        if figure_type == 'knight':
            return Knight(player)
        if figure_type == "bishop":
            return Bishop(player)
        if figure_type == 'queen':
            return Queen(player)
        if figure_type == 'king':
            return King(player)
        raise Exception(f'{figure_type} is not a figure type')
