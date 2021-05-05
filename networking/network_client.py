import threading
import time

from command import *
from game.Game import Game
from network import Network
from player.PlayerManager import PlayerManager


def network_thread(some_param):
    print("hello")

    run = True
    n = Network()

    pm = PlayerManager.get_instance()

    game_is_on = False
    my_id = None
    my_turn = False

    req = HelloCommand()
    res = Command.parse(n.send(req.print()))
    print(f"=> {res.print()}")

    if res.type == CommandType.HELLO:
        my_id = int(res.payload[7:])
        print(f"i am {my_id}")

    pm.add_own_player_id(my_id)
    pm.add_other_player_id(1 - my_id)

    pm.create_players(0)

    while run:

        if my_turn:
            state = Game.get_instance().board.export_json()
            req = StepCommand(str(state))
        else:
            req = PingCommand()

        res = Command.parse(n.send(req.print()))
        print(f"=> {res.print()}")

        if res.type == CommandType.STATE:
            game_is_on = True
            if int(res.payload[8:9]) == my_id:
                print("my turn")
                my_turn = True
            else:
                my_turn = False

        elif res.type == CommandType.WAIT:
            pass
        else:
            print("unexpected message")

        time.sleep(5)


def run_network_thread():
    x = threading.Thread(target=network_thread, args=(1,))
    x.start()


if __name__ == '__main__':
    run_network_thread()
