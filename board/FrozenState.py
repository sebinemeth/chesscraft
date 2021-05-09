from board.AbstractBoardState import AbstractBoardState


class FrozenState(AbstractBoardState):
    """ Does nothing. Use e.g. for waiting the other player's turn."""

    def field_clicked(self, x, y):
        pass

    def type_of_state(self):
        return 'frozen'
