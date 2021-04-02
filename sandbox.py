from board.Board import Board
from board.Field import Field
from figure.Figure import Figure

from enum import Enum


class A:
    def to_B(self):
        States.B.accept()

    def accept(self):
        print("A accept")


class B:
    def accept(self):
        print("B accept")

    def to_A(self):
        States.A.accept()


class States(Enum):
    A = A()
    B = B()







