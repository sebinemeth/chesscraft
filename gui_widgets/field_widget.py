import pygame

from gui_widgets.button import Button
from utils.balazs_utils import figure_image_path

FIELD_SIZE = 50
SIDE_MARGIN = 160
TOP_MARGIN = 100


class FieldWidget(Button):

    def __init__(self, x, y):
        color = [120, 120, 130] if (x - y) % 2 == 0 else [200, 200, 200]
        super().__init__(color, x * FIELD_SIZE + SIDE_MARGIN, y * FIELD_SIZE + TOP_MARGIN, FIELD_SIZE, FIELD_SIZE)
        self.figure = None
        self.original_color = color

    def set_color(self, color):
        self.color = color

    def reset_color(self):
        self.color = self.original_color

    def draw_figure(self, screen, figure):
        img = pygame.image.load(figure_image_path(figure))
        screen.blit(pygame.transform.scale(img, (40, 40)), (self.x + 5, self.y + 5))
