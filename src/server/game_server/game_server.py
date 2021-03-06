from threading import Thread

from src.communications.communicator.tcp.tcp_listener import TCPListener
from src.communications.communicator.udp.udp_listener import UDPListener
from src.communications.conversation.conversation_dictionary import ConversationDictionary
from src.communications.conversation.conversation_factory import ConversationFactory
from src.processors.dispatcher import Dispatcher
from src.server.game_server.constants import DEFAULT_GAME_SERVER_UDP_ADDRESS, DEFAULT_GAME_SERVER_TCP_ADDRESS


class GameServer(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.alive = True
        self._initAddresses(kwargs)
        self._initConversations()
        self._initDispatcher()
        self._initListeners()

    def _initConversations(self):
        self.conversation_dict = ConversationDictionary()
        self.conversation_factory = ConversationFactory()

    def _initDispatcher(self):
        self.dispatcher = Dispatcher(conversation_dict=self.conversation_dict,
                                     conversation_factory=self.conversation_factory)

    def _initListeners(self):
        self.tcp_listener = TCPListener(address=self.tcp_address, dispatcher=self.dispatcher)
        self.udp_listener = UDPListener(address=self.udp_address, dispatcher=self.dispatcher)

        self.tcp_listener.start()
        self.udp_listener.start()
        print("Listening for TCP messages on {}".format(self.tcp_address))
        print("Listening for UDP messages on {}".format(self.udp_address))

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

    def getNextProcessID(self):
        return 1 # TODO: return a new unique process id for connecting processes

    def cleanup(self):
        self.udp_listener.cleanup()
        self.tcp_listener.cleanup()
