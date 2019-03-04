import unittest

from src.server.game_server.game_server import GameServer


class TestComs(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.server = GameServer()

    def runSomething(self):
        pass