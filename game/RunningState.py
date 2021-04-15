from board.Board import Board
from game.AbstractGameState import AbstractGameState


class RunningState(AbstractGameState):

    def __init__(self, game):
        super().__init__(game)
        self.__board = Board()

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, var):
        self.__board = var

    def update(self, events, pressed_keys) -> bool:
        # print("RunningState handles events and input.")
        # print("RunningState wants to change the state of the context. To the FinninshingState.")
        # self.game.transition_to(self.game.finishing_state)
        return True
