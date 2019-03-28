from src.server.constants import DEFAULT_LOBBY_UDP_ADDRESS, DEFAULT_LOBBY_TCP_ADDRESS
from src.server.server import Server


class Lobby(Server):
    """
    Specialization of a server.

    Should contain lobby related logic
    """
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.games = []
        self.players = []

    def _getDefaultAddresses(self):
        self.udp_address = DEFAULT_LOBBY_UDP_ADDRESS
        self.tcp_address = DEFAULT_LOBBY_TCP_ADDRESS
