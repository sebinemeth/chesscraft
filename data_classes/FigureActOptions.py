from dataclasses import dataclass
from typing import List


#class FigureActOptions(dataclass):
#    has_remaining_action: bool = True
#    possible_steps: List[(int, int)] = []
#    possible_attacks: List[(int, int)] = []

# class FigureActOptions:
#     def __init__(self, has_remaining_action=True, possible_steps=[], possible_attacks=[]):
#         self.has_remaining_action = has_remaining_action
#         self.possible_steps = possible_steps
#         self.possible_attacks = possible_attacks


#class FigureActOptions(dataclass):
#    has_remaining_action: bool = True
#    possible_steps: List[(int, int)] = []
#    possible_attacks: List[(int, int)] = []

class FigureActOptions:
    def __init__(self, has_remaining_action, possible_steps, possible_attacks):
        self.has_remaining_action = True
        self.possible_steps = []
        self.possible_attacks = []