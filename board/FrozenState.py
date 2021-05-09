from board.AbstractBoardState import AbstractBoardState


class FrozenState(AbstractBoardState):
    """ Does nothing. Use e.g. for waiting the other player's turn."""

    def field_clicked(self, x, y):
        pass

    def type_of_state(self):
<<<<<<< HEAD
        return 'frozen'
=======
        return "frozen"
>>>>>>> 8207c2d0e2c4d48bccefabb9148f923e86d073be
