from abc import ABC, abstractmethod

from enums.Direction import Direction


class Player(ABC):
    def __init__(self, direction: Direction):
        self._direction = direction

    @property
    def direction_signed_1(self):
        if self._direction == Direction.LEFT:
            return -1
        else:
            return 1

    @abstractmethod
    def turn_started(self):
        """ Turn-controller* should call this. """
        pass

    @abstractmethod
    def is_finished_turn(self) -> bool:
        """ Turn-controller*  should check this."""
        pass

    # *probably specific state of game
