from board.Board import Board
from player.PlayerManager import PlayerManager


class Game:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Game.__instance is None:
            Game()
        return Game.__instance

    def __init__(self):
        """ Virtually private constructor. """
        self.__quit = False
        if Game.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Game.__instance = self
            self.__board = Board()

    @property
    def board(self):
        return self.__board

    @staticmethod
    def end_turn():
        PlayerManager.get_instance().turn_passed()

    def quit(self):
        self.__quit = True

    def is_quit(self):
        return self.__quit
