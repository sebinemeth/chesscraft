from abc import ABC, abstractmethod


class AbstractGameState(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def game(self): #-> Game:
        return self._game

    @game.setter 
    def game(self, game):#: Game) -> None:
        self._game = game

    @abstractmethod
    def handle_events_and_input(self, events, pressed_keys) -> None:
        pass   

    #@abstractmethod
    #def handle1(self) -> None:
    #    pass