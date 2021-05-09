from board.AbstractBoardState import AbstractBoardState


class LostGameState(AbstractBoardState):
    def field_clicked(self, x: int, y: int):
        pass

    def type_of_state(self):
        return 'lost_game'
