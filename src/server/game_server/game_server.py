from src.server.constants import DEFAULT_GAME_SERVER_UDP_ADDRESS, DEFAULT_GAME_SERVER_TCP_ADDRESS
from src.server.server import Server


class GameServer(Server):
    """
    Specialization of a server.

    Should contain game-server related logic
    """
    def _getDefaultAddresses(self):
        self.udp_address = DEFAULT_GAME_SERVER_UDP_ADDRESS
        self.tcp_address = DEFAULT_GAME_SERVER_TCP_ADDRESS
