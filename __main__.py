import logging
import sys

import pygame as pg

import networking.network_client as client
from Screen import Screen
from game.Game import Game
from player.PlayerManager import PlayerManager


def main(multiplayer=False):
    """" The main function of the game. """
    FPS = 60
    pg.init()  # initializes pyGame
    pg.display.set_caption("ChessCraft")
    pg.display.set_icon(pg.image.load('images/1/king.png'))
    clock = pg.time.Clock()

    if multiplayer:
        logging.basicConfig(level=logging.DEBUG)
        client.run_network_thread()
    else:
        pm = PlayerManager.get_instance()
        pm.add_own_player_id(0)
        pm.add_other_player_id(1)
        pm.create_players(0, False)

    # itt a board: Game.get_instance().board
    res = (720, 720)

    screen = pg.display.set_mode(res)  # init screen

    bg = pg.image.load("images/bg.png")
    screen.blit(bg, (0, 0))
    while True:
        # screen.blit(bg, (0, 0))
        # update "roots" & pass all the events for handling (it should be chained further to lesser interested objects)
        # they can ask for exit by returning False
        events = pg.event.get()
        pressed_keys = pg.key.get_pressed()
        Screen.get_instance().update(screen, pg.mouse.get_pos())
        # if Screen.get_instance().handle(events, pressed_keys) returns false the game quits
        if not Screen.get_instance().handle(events, pressed_keys):
            break
        clock.tick(1000 // FPS)
        pg.display.update()
    pg.quit()
    Game.get_instance().quit()


if __name__ == "__main__":
    print("running with args", sys.argv)
    if len(sys.argv) > 1:
        if sys.argv[1] == "singleplayer":
            main(False)
    else:
        main(True)
