from src.contact.game import Game
from src.server.constants import DEFAULT_GAME_SERVER_UDP_ADDRESS, DEFAULT_GAME_SERVER_TCP_ADDRESS
from src.server.server import Server


class GameServer(Server):
    """
    Specialization of a server.

    Should contain game-server related logic
    """
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self._initGame()

    def getPlayer(self, id):
        pass # TODO: return player by id

    def getSecretKeeper(self):
        pass # TODO: return the current secret keeper

    def _initGame(self):
        self.game = Game()

    def _getDefaultAddresses(self):
        self.udp_address = DEFAULT_GAME_SERVER_UDP_ADDRESS
        self.tcp_address = DEFAULT_GAME_SERVER_TCP_ADDRESS
