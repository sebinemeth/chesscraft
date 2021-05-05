from game.AbstractGameState import AbstractGameState
from game.FinishingState import FinishingState
from game.RunningState import RunningState
from game.WaitingForPlayersState import WaitingForPlayersState


class Game:
    # TODO: states can be singletons as well?
    __instance = None
    _state = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Game.__instance is None:
            Game()
        return Game.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Game.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Game.__instance = self
            self.running_state = RunningState(self)
            self.finishing_state = FinishingState(self)
            self.waiting_for_players_state = WaitingForPlayersState(self)
            self.transition_to(self.waiting_for_players_state)

    def update(self, events, pressed_keys) -> bool:
        return self._state.update(events, pressed_keys)

    def transition_to(self, state: AbstractGameState):
        """
        The Game allows changing the GameState object at runtime.
        """
        self._state = state