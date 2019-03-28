from threading import Thread

from src.communications.conversation.conversation_dictionary import ConversationDictionary
from src.communications.conversation.conversation_factory import ConversationFactory
from src.communications.communicator.tcp.tcp_listener import TCPListener
from src.communications.communicator.udp.udp_listener import UDPListener
from src.server.constants import DEFAULT_SERVER_UDP_ADDRESS, DEFAULT_SERVER_TCP_ADDRESS
from src.server.dispatcher import Dispatcher


class Server(Thread):
    """
    Parent server class to inherit from

    Contains code necessary to listen on a port, manage conversations, and dispatch incoming envelopes
    """
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.alive = True
        self._initAddresses(kwargs)
        self._initConversations()
        self._initDispatcher()
        self._initListeners()

    def _initConversations(self):
        self.conversation_id = 0
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

    def _initDefaultAddresses(self):
        self.udp_address = DEFAULT_SERVER_UDP_ADDRESS
        self.tcp_address = DEFAULT_SERVER_TCP_ADDRESS

    def _initAddresses(self, kwargs):
        self._initDefaultAddresses()
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

    def getNextConversationID(self):
        """
        Gets a new unique conversation id for this client

        :return: int: conversation_id
        """
        self.conversation_id += 1
        return self.conversation_id


    def cleanup(self):
        self.udp_listener.cleanup()
        self.tcp_listener.cleanup()
