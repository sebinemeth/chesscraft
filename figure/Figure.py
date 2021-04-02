from abc import ABC, abstractmethod
from typing import List

from data_classes.SimplifiedBoard import SimplifiedBoard
from data_classes.FigureActOptions import FigureActOptions


class Figure(ABC):
    def __init__(self):
        # Parent field should handle position.
        self.x = -1
        self.y = -1

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def chosen(self, simple_board: SimplifiedBoard) -> FigureActOptions:
        steps = self.collect_possible_steps(simple_board)
        attacks = self.collect_possible_attacks(simple_board)
        return FigureActOptions(True, steps, attacks)

    @abstractmethod
    def collect_possible_steps(self, simple_board: SimplifiedBoard) -> List[(int, int)]:
        """ Retrieves the list of field positions, where it can step. """

    @abstractmethod
    def collect_possible_attacks(self, simple_board: SimplifiedBoard) -> List[(int, int)]:
        """ Retrieves the list of field positions, where it can attack. """


