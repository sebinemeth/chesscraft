#class FigureActOptions(dataclass):
#    has_remaining_action: bool = True
#    possible_steps: List[(int, int)] = []
#    possible_attacks: List[(int, int)] = []

class FigureActOptions:
    def __init__(self, has_remaining_action, possible_steps, possible_attacks):
        self.has_remaining_action = True
        self.possible_steps = possible_steps
        self.possible_attacks = possible_attacks
