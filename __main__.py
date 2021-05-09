import logging
import sys

import pygame as pg

import networking.network_client as client
from Screen import Screen
from game.Game import Game


def main():
    """" The main function of the game. """
    FPS = 30
    pg.init()  # initializes pyGame
    clock = pg.time.Clock()

    logging.basicConfig(level=logging.DEBUG)

    client.run_network_thread()

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
        clock.tick(1000//FPS)
        pg.display.update()
    pg.quit()
    Game.get_instance().quit()


if __name__ == "__main__":
    main()
