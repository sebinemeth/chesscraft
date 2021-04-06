from game.AbstractGameState import AbstractGameState


class RunningState(AbstractGameState):
    def update(self, events, pressed_keys) -> bool:
        # print("RunningState handles events and input.")
        # print("RunningState wants to change the state of the context. To the FinninshingState.")
        # self.game.transition_to(self.game.finnishingState)
        return True
