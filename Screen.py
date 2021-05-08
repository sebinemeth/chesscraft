# TODO possibly refactor this to some GUI system
from game.Game import Game
from gui_widgets.field_widget import FieldWidget
import pygame
from player.PlayerManager import PlayerManager
from data_classes.FigureActOptions import FigureActOptions


def gui_log(func):
    def console_log(*args, **kwargs):
        print(f'Screen log: {func.__name__} with parameters: ', end='')
        print(args)
        return func(*args, **kwargs)
    return console_log


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
            self.__ready = False
            self.__fields = None
            self.__steps = None
            self.__attacks = None

    @property
    def fields(self):
        return self.__fields

    @property
    def ready(self):
        return self.__ready

    def set_ready(self, ready):
        self.__ready = ready


    def init_fields(self):
        size = Game.get_instance().board.SIZE
        self.__fields = tuple(tuple(FieldWidget(x, y) for y in range(size)) for x in range(size))


    def set_acts(self, act_options: FigureActOptions):
        if act_options is not None:
            self.__steps = act_options.possible_steps
            self.__attacks = act_options.possible_attacks

    def update(self, screen, mouse):
        if not self.ready:
            my_player = PlayerManager.get_instance().my_player
            other_player = PlayerManager.get_instance().other_player
            if my_player is not None and other_player is not None:
                self.set_ready(True)
                self.init_fields()

        if not self.ready:
            screen_width, screen_height = pygame.display.get_surface().get_size()
            FONT = pygame.font.Font('freesansbold.ttf', 32)
            WAITING_TEXT = FONT.render('Waiting for other player...', True, (0, 0, 50))
            text_rect = WAITING_TEXT.get_rect(center=(screen_width / 2, screen_height / 3))
            screen.blit(WAITING_TEXT, text_rect)
        else:
            board = Game.get_instance().board
            if board.state.type_of_state == 'frozen:':
                screen_width, screen_height = pygame.display.get_surface().get_size()
                FONT = pygame.font.Font('freesansbold.ttf', 32)
                OTHER_TURN_TEXT = FONT.render('Opponent\'s turn...', True, (0, 0, 50))
                text_rect = OTHER_TURN_TEXT.get_rect(center=(screen_width / 2, 10))
                screen.blit(OTHER_TURN_TEXT, text_rect)
            board_fields = board.fields
            for x in range(len(board_fields)):
                for y in range(len(board_fields[0])):
                    self.fields[x][y].reset_color()
                    if board.state.type_of_state() == 'choosing_figure':
                        if self.fields[x][y].is_over(mouse):
                            self.fields[x][y].set_color([120, 250, 120])
                    if board.state.type_of_state() == 'choosing_destination':
                        if self.__steps is not None and (x, y) in self.__steps:
                            self.fields[x][y].set_color([100, 155, 0])
                        if self.__attacks is not None and (x, y) in self.__attacks:
                            self.fields[x][y].set_color([230, 80, 0])
                    self.fields[x][y].draw(screen)
                    if board_fields[x][y].figure is not None:
                        self.fields[x][y].draw_figure(screen, board_fields[x][y].figure)

    def handle(self, events, pressed_keys):
        for ev in events:
            if ev.type == pygame.QUIT:
                return False
            # Handle mouse buttons
            if ev.type == pygame.MOUSEBUTTONDOWN:
                for x in range(len(self.fields)):
                    for y in range(len(self.fields[0])):
                        if self.fields[x][y].is_over(ev.pos):
                            self.set_acts(Game.get_instance().board.field_clicked(x, y))
        return True
