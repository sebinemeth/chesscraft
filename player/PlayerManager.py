from player.HumanPlayer import HumanPlayer
from enums.Direction import Direction

class PlayerManager:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if PlayerManager.__instance is None:
            PlayerManager()
        return PlayerManager.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if PlayerManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PlayerManager.__instance = self
            self.__my_player = None
            self.__other_player = None
            self.__current_player = None

    # region properties
    @property
    def my_player(self):
        return self.__my_player

    @property
    def other_player(self):
        return self.__other_player

    @property
    def current_player(self):
        return self.__current_player
    # endregion

    def create_players(self, my_player_id, other_player_id, starting_player_id):
        """Should be called when starting game."""      # TODO not like this
        self.__my_player = HumanPlayer(Direction.LEFT)
        self.__other_player = HumanPlayer(Direction.RIGHT)
        self.__current_player = self.__my_player
        pass

    def turn_passed(self):
        """Should be called after each turn."""
        pass

