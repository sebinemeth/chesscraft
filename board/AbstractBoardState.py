from board.Field import Field

from abc import ABC, abstractmethod


class AbstractBoardState(ABC):
    def __init__(self, board):
        self._board = board

    @abstractmethod
    def field_clicked(self, x: int, y: int):
        """ The state method, called when Board's (@x, @y) field is clicked by the user.
            GUI may filter out irrelevant field clicks."""
        pass

    @abstractmethod
    def type_of_state(self):
        pass

    def reset(self, **messages):
        """ Reset member fields based on @messages.
            Called before transitioning to state. """
        pass

    def cancel(self):
        """ Cancels current state.
            By default transitions to choosing acting figure state, override for different behaviour. """
        self._board.transition_to(self._board.choosing_acting_figure_state)

    def field_xy(self, x, y) -> Field:
        return self._board.fields[x][y]
