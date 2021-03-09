# TODO possibly refactor this to some GUI system
class Screen:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Screen.__instance is None:
            Screen()
        return Screen.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Screen.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Screen.__instance = self

    def update(self, events, pressed_keys) -> bool:
        return True
