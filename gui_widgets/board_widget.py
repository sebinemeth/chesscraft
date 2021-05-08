import pygame
from field_widget import FieldWidget


class BoardWidget:
    SIZE = 8

    def __init__(self):
        self.fields = [[FieldWidget([100, 20, 20], 0, 0) for x in range(self.SIZE)] for y in range(self.SIZE)]
        x = 0
        y = 0
        for row in self.fields:
            for field in row:
                field.set_position(x, y)
                y = y + 1
            x = x + 1
            y = 0

    def draw(self, screen):
        screen.fill((100, 100, 50))
        for row in self.fields:
            for field in row:
                field.draw(screen)

    def handle(self, event):
        for row in self.fields:
            for field in row:
                if field.is_over(event.pos[0], event.pos[1]):
                    print(f'field {field.ind} has been clicked')

    def mouse_pos(self, x, y):
        for row in self.fields:
            for field in row:
                if field.is_over(x, y):
                    field.set_color([120, 250, 120])
                else:
                    field.reset_color()
