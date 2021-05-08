from gui_widgets.button import Button

SIZE = 50
SIDE_MARGIN = 100
TOP_MARGIN = 70


class FieldWidget(Button):

    def __init__(self, color, x, y):
        super().__init__(color, x*SIZE+SIDE_MARGIN, y*SIZE+TOP_MARGIN, SIZE, SIZE)
        self.figure = None
        self.original_color = [200, 100, 200]

    def set_position(self, x, y):
        self.x = x*SIZE+SIDE_MARGIN
        self.y = y*SIZE+TOP_MARGIN
        if (x - y) % 2 == 0:
            self.original_color = [200, 200, 200]
        else:
            self.original_color = [20, 20, 20]
        self.reset_color()

    def set_color(self, color):
        self.color = color

    def reset_color(self):
        self.color = self.original_color
