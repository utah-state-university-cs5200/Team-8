from src.server.constants import DEFAULT_GAME_SERVER_UDP_ADDRESS, DEFAULT_GAME_SERVER_TCP_ADDRESS
from src.server.server import Server


class GameServer(Server):
    """
    Specialization of a server.

    Should contain game-server related logic
    """
    def _initAddresses(self, kwargs):
        self.udp_address = DEFAULT_GAME_SERVER_UDP_ADDRESS
        self.tcp_address = DEFAULT_GAME_SERVER_TCP_ADDRESS
        try:
            self.udp_address = kwargs['udp_address']
        except KeyError:
            pass
        try:
            self.tcp_address = kwargs['tcp_address']
        except KeyError:
            pass
