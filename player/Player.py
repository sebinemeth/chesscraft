from abc import ABC

from enums.Direction import Direction


class Player(ABC):
    steps_per_turn = 1

    def __init__(self, some_id, direction: Direction):
        self._direction = direction
        self.steps_left = 0
        self.some_id = some_id

    @property
    def direction_signed_1(self):
        if self._direction == Direction.LEFT:
            return -1
        else:
            return 1

    def turn_started(self, board=None):
        self.steps_left = Player.steps_per_turn

    def is_finished_turn(self) -> bool:
        return self.steps_left == 0

    @property
    def id(self):
        return self.some_id

    @property
    def direction(self):
        return self._direction
