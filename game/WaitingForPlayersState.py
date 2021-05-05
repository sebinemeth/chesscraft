from game.AbstractGameState import AbstractGameState


class WaitingForPlayersState(AbstractGameState):
    def update(self, events, pressed_keys) -> bool:
        # print("WaitingForPlayers handles events and input.")
        # print("WaitingForPlayers wants to change the state of the context.")
        # self.game.transition_to(self.game.runningState)
        return True