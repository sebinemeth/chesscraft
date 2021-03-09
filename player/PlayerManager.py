class PlayerManager:  # TODO make it Singleton
    def __init__(self):
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
        """Should be called when starting game."""
        pass

    def turn_passed(self):
        """Should be called after each turn."""
        pass
