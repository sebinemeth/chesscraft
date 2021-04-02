from dataclasses import dataclass
from typing import List


class FigureActOptions(dataclass):
    has_remaining_action: bool = True
    possible_steps: List[(int, int)] = []
    possible_attacks: List[(int, int)] = []
