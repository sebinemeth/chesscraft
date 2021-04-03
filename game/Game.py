from game.AbstractGameState import AbstractGameState
from game.FinnishingState import FinnishingState
from game.RunningState import RunningState
from game.WaitingForPlayersState import WaitingForPlayersState

class Game:
    # TODO: implement state-pattern (e.g.: waiting for players, running, finished)
    #   https://refactoring.guru/design-patterns/state/python/example
    #   states can be singletons as well?
    __instance = None
    _state = None
    runningState = None
    finnishingState = None
    waitingForPlayersState = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Game.__instance is None:
            Game()
        return Game.__instance

    def __init__(self):
        """ Virtually private constructor. """
        print ("ASDFASDFDASFSAFDASFASDFASFASFASFASFASFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
        if Game.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Game.__instance = self
            self.runningState = RunningState()
            self.finnishingState = FinnishingState()
            self.waitingForPlayersState = WaitingForPlayersState()
            self.transition_to(self.waitingForPlayersState)
        #__instance.transition_to(state)
        

    def update(self, events, pressed_keys) -> bool:
        self.request_to_hadle_events_and_input(events, pressed_keys)
        return True  # TODO pass to state


    def transition_to(self, state):
        """
        The Game allows changing the GameState object at runtime.
        """

        print(f"Game: Transition to {type(state).__name__}")
        self._state = state
        self._state.game = self

    """
    The Game delegates part of its behavior to the current GameState object.
    """

    def request_to_hadle_events_and_input(self, events, pressed_keys):
        self._state.handle_events_and_input(events, pressed_keys)

    #def request1(self):
    #    self._state.handle1()
