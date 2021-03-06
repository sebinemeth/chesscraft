import logging
import socket


def counter():
    n = 0
    while True:
        yield n
        n += 1


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "chesscraft.remetelak.com"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        self.counter = counter()
        logging.debug(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(4096).decode()
        except socket.error as e:
            logging.error(e)

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            response = self.client.recv(4096).decode()
            logging.debug(f"message #{next(self.counter)}")
            return response
        except socket.error as e:
            logging.error(e)
