import pygame as pg
from Screen import Screen
from game.Game import Game


def main():
    """" The main function of the game. """
    FPS = 30

    pg.init()  # initializes pyGame
    clock = pg.time.Clock()
    while "Alma":
        # update "roots" & pass all the events for handling (it should be chained further to lesser interested objects)
        # they can ask for exit by returning False
        events, pressed_keys = pg.event.get(), pg.key.get_pressed()
        if not Screen.get_instance().update(events, pressed_keys):
            break
        if not Game.get_instance().update(events, pressed_keys):
            break
        clock.tick(FPS)
    pg.quit()


if __name__ == "__main__":
    main()
