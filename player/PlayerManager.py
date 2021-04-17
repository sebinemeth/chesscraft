from __future__ import annotations

from player.Player import Player
from player.HumanPlayer import HumanPlayer
from player.AIPlayer import AIPlayer
from enums.Direction import Direction


class PlayerManager:
    __instance = None

    @staticmethod
    def get_instance() -> PlayerManager:
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
            self.__own_player = None
            self.__other_player = None
            self.__current_player = None
            self.__player_ids = {}

    # region properties
    @property
    def my_player(self) -> Player:
        return self.__own_player

    @property
    def other_player(self) -> Player:
        return self.__other_player

    @property
    def current_player(self) -> Player:
        return self.__current_player

    @property
    def is_current_player_finished(self) -> bool:
        """ If we want automatic turn passing, GUI can check this repeatedly and call Game's turn ending when
            it's true. Or combine this with some timer or whatever GUI feels good. :) """
        return self.current_player.is_finished_turn()
    # endregion

    def add_own_player_id(self, some_id):
        self.__player_ids["own player"] = some_id

    def add_other_player_id(self, some_id):
        self.__player_ids["other player"] = some_id

    def create_players(self, starting_player_id, other_is_human: bool = True):
        """ Should be called when starting game."""
        if len(self.__player_ids) < 2:
            raise Exception(f"Ostoba! Nem kaptam meg minden játékos id-ját! Megadottak: {self.__player_ids}")
        other_cls = HumanPlayer  # type: type (Player)
        if not other_is_human:
            other_cls = AIPlayer
        if starting_player_id == self.__player_ids["own player"]:
            self.__own_player = Player(starting_player_id, Direction.LEFT)
            self.__other_player = other_cls(self.__player_ids["other player"], Direction.RIGHT)
            self.__current_player = self.__own_player
        elif starting_player_id == self.__player_ids["other player"]:
            self.__own_player = Player(self.__player_ids["own player"], Direction.RIGHT)
            self.__other_player = other_cls(starting_player_id, Direction.LEFT)
            self.__current_player = self.__other_player
        else:
            raise Exception(f"Ostoba! Elszúrtál valamit az id-kkal! Megadott id-k: {self.__player_ids}, "
                            f"kezdő id-ja: {starting_player_id}")
        self.__current_player.turn_started()

    def turn_passed(self):
        if self.__own_player == self.__current_player:
            self.__current_player = self.__other_player
        else:
            self.__current_player = self.__own_player
        self.__current_player.turn_started()
