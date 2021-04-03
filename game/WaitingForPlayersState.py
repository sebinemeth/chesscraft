from game.AbstractGameState import AbstractGameState


class WaitingForPlayersState(AbstractGameState):
    def handle_events_and_input(self, events, pressed_keys) -> None:
        #print("WaitingForPlayers handles events and input.")
        #print("WaitingForPlayers wants to change the state of the context.")
        #self.game.transition_to(self.game.runningState)