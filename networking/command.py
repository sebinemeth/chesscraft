from enum import Enum


class CommandType(Enum):
    NONE = "NONE"
    HELLO = "HELLO"
    STATE = "STATE"
    WAIT = "WAIT"
    STEP = "STEP"
    PING = "PING"


class Command:
    def __init__(self):
        self.type = CommandType.NONE
        self.payload = ""

    @staticmethod
    def parse(raw):
        c = Command()
        c.type = CommandType[raw[:raw.find(':')]]
        c.payload = raw[raw.find(':') + 1:]
        return c

    def print(self):
        return f'{str(self.type)[12:]}:{self.payload}'


class GameStateCommand(Command):
    def __init__(self, game):
        self.type = CommandType.STATE
        self.payload = f"ROUNDOF:{game.round_of}:{game.state}"


class WaitCommand(Command):
    def __init__(self):
        self.type = CommandType.WAIT
        self.payload = ""


class HelloCommand(Command):
    def __init__(self):
        self.type = CommandType.HELLO
        self.payload = ""


class PingCommand(Command):
    def __init__(self):
        self.type = CommandType.PING
        self.payload = ""


class StepCommand(Command):
    def __init__(self, state):
        self.type = CommandType.STEP
        self.payload = state
