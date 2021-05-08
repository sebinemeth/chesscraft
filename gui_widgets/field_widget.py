from gui_widgets.button import Button
import pygame

FIELD_SIZE = 50
SIDE_MARGIN = 100
TOP_MARGIN = 70


class FieldWidget(Button):

    def __init__(self, x, y):
        color = [20, 20, 20] if (x-y) % 2 == 0 else [200, 200, 200]
        super().__init__(color, x*FIELD_SIZE+SIDE_MARGIN, y*FIELD_SIZE+TOP_MARGIN, FIELD_SIZE, FIELD_SIZE)
        self.figure = None
        self.original_color = color

    def set_color(self, color):
        self.color = color

    def reset_color(self):
        self.color = self.original_color

    def draw_figure(self, screen, figure):
        pygame.draw.rect(screen, [0, 150, 150], [self.x+5, self.y+5, 40, 40])