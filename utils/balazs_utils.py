# from figure.Peasant import Peasant
# from figure.Rook import Rook
# from figure.Queen import Queen
# from figure.Bishop import Bishop
# from figure.Knight import Knight
# from figure.King import King
from typing import List

import numpy as np

from data_classes.SimplifiedBoard import SimplifiedBoard
from enums.FieldOccupation import FieldOccupation


def in_board(x, y) -> bool:
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    else:
        return False


def is_empty_field(x, y, simple_board: SimplifiedBoard) -> bool:
    if in_board(x, y) and simple_board.fields[x][y] == FieldOccupation.EMPTY:
        return True
    else:
        return False


def is_enemy_field(x, y, simple_board: SimplifiedBoard) -> bool:
    if in_board(x, y) and simple_board.fields[x][y] == FieldOccupation.ENEMY:
        return True
    else:
        return False


def possible_fields_long_step(field: (int, int), directions,
                              simple_board: SimplifiedBoard):  # -> List[(int, int)]:
    """
        :return: coordinates of empty fields in the directions of "additions" until a not empty field
                 or the edge of the board
        :rtype: List[(int, int)]
    """
    ret = []
    for i in range(len(directions)):
        candidate = tuple(np.add(directions[i], field))
        while is_empty_field(*candidate, simple_board):
            ret.append(candidate)
            candidate = tuple(np.add(directions[i], candidate))
    return ret


def possible_attacks_long_step(field: (int, int), directions,
                               simple_board: SimplifiedBoard):  # -> List[(int, int)]:
    """
        :return: coordinates of the first enemy fields in the directions of "additions"
        :rtype: List[(int, int)]
    """
    ret = []
    for i in range(len(directions)):
        candidate = tuple(np.add(directions[i], field))
        while is_empty_field(*candidate, simple_board):
            candidate = tuple(np.add(directions[i], candidate))
        if is_enemy_field(*candidate, simple_board):
            ret.append(candidate)
    return ret


def possible_fields_one_step(field: (int, int), directions,
                             simple_board: SimplifiedBoard):  # -> List[(int, int)]:
    """
        :return: coordinates of empty fields in the directions of "additions" until a not empty field
                 or the edge of the board
        :rtype: List[(int, int)]
    """
    ret = []
    for i in range(len(directions)):
        candidate = tuple(np.add(directions[i], field))
        if is_empty_field(*candidate, simple_board):
            ret.append(candidate)
    return ret


def possible_attacks_one_step(field: (int, int), directions,
                              simple_board: SimplifiedBoard):  # -> List[(int, int)]:
    """
        :return: coordinates of empty fields in the directions of "additions" until a not empty field
                 or the edge of the board
        :rtype: List[(int, int)]
    """
    ret = []
    for i in range(len(directions)):
        candidate = tuple(np.add(directions[i], field))
        if is_enemy_field(*candidate, simple_board):
            ret.append(candidate)
    return ret


def figure_image_path(figure):
    img_path = 'images/'
    if figure.owner.id == 0:
        img_path = img_path + '0/'
    else:
        img_path = img_path + '1/'
    figure_type = figure.export_state()[1]
    img_path = img_path + figure_type

    return img_path + '.png'
