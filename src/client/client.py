from threading import Thread

from src.communications.communicator.tcp.tcp_communicator import TCPCommunicator
from src.communications.communicator.udp.udp_communicator import UDPCommunicator
from src.communications.conversation.conversation_dictionary import ConversationDictionary
from src.communications.conversation.conversation_factory import ConversationFactory

from src.server.constants import DEFAULT_LOBBY_UDP_ADDRESS, DEFAULT_LOBBY_TCP_ADDRESS
from src.server.dispatcher import Dispatcher


class Client(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self._initServerAddresses()
        self._initConversations()
        self._initDispatcher()
        self._initCommunicators()

    def _initServerAddresses(self):
        self.serverUDPAddress = DEFAULT_LOBBY_UDP_ADDRESS
        self.serverTCPAddress = DEFAULT_LOBBY_TCP_ADDRESS

    def _initConversations(self):
        self.conversation_id = 0
        self.conversation_dict = ConversationDictionary()
        self.conversation_factory = ConversationFactory()

    def _initDispatcher(self):
        self.dispatcher = Dispatcher(conversation_dict=self.conversation_dict,
                                     conversation_factory=self.conversation_factory)

    def _initCommunicators(self):
        self.udp_communicator = UDPCommunicator(self.dispatcher, address=self.serverUDPAddress)
        self.tcp_communicator = TCPCommunicator(self.dispatcher, address=self.serverTCPAddress)

    def cleanup(self):
        self.udp_communicator.cleanup()
        self.tcp_communicator.cleanup()

    def getNextConversationID(self):
        """
        Gets a new unique conversation id for this client

        :return: int: conversation_id
        """
        self.conversation_id += 1
        return self.conversation_id
