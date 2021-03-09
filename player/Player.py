from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def turn_started(self):
        """ Turn-controller* should call this. """
        pass

    @abstractmethod
    def is_finished_turn(self) -> bool:
        """ Turn-controller*  should check this."""
        pass

    # *probably specific state of game
