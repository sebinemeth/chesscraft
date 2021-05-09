import json
import logging
import sys
import threading
import time

from game.Game import Game
from networking.command import *
from networking.network import Network
from player.PlayerManager import PlayerManager


def network_thread(some_param):
    logging.info("hello")

    run = True
    n = Network()

    pm = PlayerManager.get_instance()

    game_is_on = False
    my_id = None

    req = HelloCommand()
    res = Command.parse(n.send(req.print()))
    logging.info(f"=> {res.print()}")

    if res.type == CommandType.HELLO:
        my_id = int(res.payload[7:])
        logging.info(f"i am {my_id}")

    while run:

        if game_is_on:
            if Game.get_instance().is_quit():
                print("Game is over, network thread exiting")
                break

            if pm.get_instance().my_turn():
                if Game.get_instance().board.state.type_of_state() == 'frozen' \
                        or Game.get_instance().board.state.type_of_state() == 'won_game':
                    # player chose action, we can send it to the network
                    state_json = json.dumps(Game.get_instance().board.export_state())
                    req = StepCommand(state_json)
                else:
                    # player is choosing figure and destination
                    time.sleep(.5)
                    continue
            else:
                req = PingCommand()
        else:
            req = PingCommand()

        res_raw = n.send(req.print())
        if res_raw is None or res_raw == "":
            print(f"got: {res_raw}")
            continue
        res = Command.parse(res_raw)
        logging.info(f"=> {res.print()}")

        if res.type == CommandType.STATE:
            game_is_on = True

            if pm.get_instance().my_player is None:
                pm.add_own_player_id(my_id)
                pm.add_other_player_id(1 - my_id)

                pm.create_players(0)

            new_state_json = res.payload[10:]
            new_state = None
            try:
                if len(new_state_json) > 0:
                    new_state = json.loads(new_state_json)
            except Exception as e:
                logging.error(f"json decode error {e}")
                continue

            if len(new_state_json) > 0 and new_state is not None:
                Game.get_instance().board.import_state(new_state)

            if int(res.payload[8:9]) == my_id:
                logging.info("my turn")
                pm.get_instance().turn_of(my_id)
                Game.get_instance().board.transition_to(Game.get_instance().board.choosing_acting_figure_state)
            else:
                pm.get_instance().turn_of(1 - my_id)

        elif res.type == CommandType.WAIT:
            pass

        elif res.type == CommandType.ERROR:
            print("recieved error")
            pass

        else:
            logging.warning("unexpected message")

        time.sleep(1)


def run_network_thread():
    x = threading.Thread(target=network_thread, args=(1,))
    x.start()


if __name__ == '__main__':
    print("running with args", sys.argv)
    if len(sys.argv) > 1:
        if sys.argv[1] == "debug":
            logging.basicConfig(level=logging.DEBUG)

    run_network_thread()
