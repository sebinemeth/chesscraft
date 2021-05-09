import random
from enums.FieldOccupation import FieldOccupation


def attack(starting_field, target_field):
    target_field.remove_figure()
    target_field.add_figure(starting_field.figure)
    starting_field.remove_figure()


def step(starting_field, target_field):
    target_field.add_figure(starting_field.figure)
    starting_field.remove_figure()


def randomly_attack(ai_player, board):
    possible_attacks = []
    for row in board.fields:
        for field in row:
            if field.get_occupation_type(ai_player) == FieldOccupation.FRIENDLY:
                simplified_board = board.create_simplified_board(ai_player)
                attacks = field.figure.collect_possible_attacks(simplified_board)
                if attacks is not None and len(attacks) > 0:
                    possible_attacks.append([field, board.fields[attacks[0][0]][attacks[0][1]]])

    if len(possible_attacks) > 0:
        randi = random.randint(0, len(possible_attacks)-1)
        attack(*possible_attacks[randi])
        return True
    possible_steps = []
    for row in board.fields:
        for field in row:
            if field.get_occupation_type(ai_player) == FieldOccupation.FRIENDLY:
                simplified_board = board.create_simplified_board(ai_player)
                steps = field.figure.collect_possible_steps(simplified_board)
                if steps is not None and len(steps) > 0:

                    possible_steps.append([field, board.fields[steps[0][0]][steps[0][1]]])

    if len(possible_steps) > 0:
        randi = random.randint(0, len(possible_steps)-1)
        step(*possible_steps[randi])
        return True
    return False
