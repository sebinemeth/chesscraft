class Game:
    # TODO: implement state-pattern (e.g.: waiting for players, running, finished)
    #   https://refactoring.guru/design-patterns/state/python/example
    #   states can be singletons as well?
    __instance = None

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

    def update(self, events, pressed_keys) -> bool:
        return True  # TODO pass to state
