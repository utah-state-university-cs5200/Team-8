from threading import Thread

from src.communications.communicator.tcp.tcp_listener import TCPListener
from src.communications.communicator.udp.udp_listener import UDPListener
from src.server.game_server.constants import DEFAULT_GAME_SERVER_UDP_ADDRESS, DEFAULT_GAME_SERVER_TCP_ADDRESS


class GameServer(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.alive = True
        self._initAddress(kwargs)
        self._initDispatcher()
        self.tcp_listener = TCPListener(address=self.tcp_address, dispatcher=self.dispatcher)
        self.udp_listener = UDPListener(address=self.udp_address, dispatcher=self.dispatcher)

        self.tcp_listener.start()
        self.udp_listener.start()

    def _initDispatcher(self):
        self.dispatcher = None # TODO: make a dispatcher

    def _initAddress(self, kwargs):
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

    def getNextProcessID(self):
        return 1 # TODO: return a new unique process id for connecting processes
