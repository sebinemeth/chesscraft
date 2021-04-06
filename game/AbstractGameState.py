from abc import ABC, abstractmethod


class AbstractGameState(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    def __init__(self, game):
        """

        :param game: the parent Game
        :type game: Game
        """
        self._game = game

    @property
    def game(self):
        """
        :return: the parent Game
        :rtype: Game
        """
        return self._game

    @abstractmethod
    def update(self, events, pressed_keys) -> bool:
        return True
