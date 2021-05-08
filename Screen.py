# TODO possibly refactor this to some GUI system
from game.Game import Game
from gui_widgets.field_widget import FieldWidget
import pygame


def gui_log(func):
    def console_log(*args, **kwargs):
        print(f'Screen log: {func.__name__}', end='')
        print('With parameters: ', end='')
        for arg in args:
            k = arg.split("=")[0]
            v = arg.split("=")[1]
            print(f"{k}={v} ", end='')
        for kwarg in kwargs:
            k = kwarg.split("=")[0]
            v = kwarg.split("=")[1]
            print(f"{k}={v} ", end='')
        return func(*args, **kwargs)
    return console_log()


class Screen:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Screen.__instance is None:
            Screen()
        return Screen.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Screen.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Screen.__instance = self
            size = Game.get_instance().board.SIZE
            self.__fields = tuple(tuple(FieldWidget(x, y) for y in range(size)) for x in range(size))

    @property
    def fields(self):
        return self.__fields

    @gui_log
    def update(self, screen, mouse):
        screen.fill((100, 100, 50))

        board_fields = Game.get_instance().board.fields
        for x in range(len(board_fields)):
            for y in range(len(board_fields[0])):
                if self.fields[x][y].is_over(mouse):
                    self.fields[x][y].set_color([120, 250, 120])
                else:
                    self.fields[x][y].reset_color()
                self.fields[x][y].draw(screen)
                if board_fields[x][y].figure is not None:
                    self.fields[x][y].drawFigure(screen, board_fields[x][y].figure)

    @gui_log
    def handle(self, events, pressed_keys):
        for ev in events:
            if ev.type == pygame.quit():
                return False
            # Handle mouse buttons
            if ev.type == pygame.MOUSEBUTTONDOWN:
                for x in range(len(self.fields)):
                    for y in range(len(self.fields[0])):
                        if self.fields[x][y].is_over(events.pos):
                            Game.get_instance().board.field_clicked(x, y)
