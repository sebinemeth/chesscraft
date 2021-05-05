import threading
import time

from command import *
from game.Game import Game
from network import Network


def network_thread(some_param):
    print("hello")

    run = True
    n = Network()

    print(Game.get_instance().__board)

    game_is_on = False
    i_am = None
    my_turn = False

    req = HelloCommand()
    res = Command.parse(n.send(req.print()))
    print(f"=> {res.print()}")

    if res.type == CommandType.HELLO:
        i_am = int(res.payload[7:])
        print(f"i am {i_am}")

    while run:

        req = PingCommand()
        res = Command.parse(n.send(req.print()))
        print(f"=> {res.print()}")

        if res.type == CommandType.STATE:
            game_is_on = True
            if int(res.payload[8:9]) == i_am:
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
