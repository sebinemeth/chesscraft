from game.AbstractGameState import AbstractGameState


class FinnishingState(AbstractGameState):
    def update(self, events, pressed_keys) -> bool:
        # print("FinnnishingState handles events and input.")
        # print("FinnnishingState is the end state.")
        # self.game.transition_to(self.game.waitingForPlayersState)
        return True
