from threading import Thread

from src.communications.communicator.tcp.tcp_communicator import TCPCommunicator
from src.communications.communicator.udp.udp_communicator import UDPCommunicator
from src.communications.conversation.conversation_dictionary import ConversationDictionary
from src.client.conversations.conversation_factory import ConversationFactory
from src.server.dispatcher import Dispatcher


class PlayerClient(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        # TODO: should have some sort of UI object to get some of these values from the user
        self._initServerAddresses()
        self._initConversations()
        self._initDispatcher()
        self._initCommunicators()

    def _initServerAddresses(self):
        self.serverUDPAddress = ('127.0.0.1', 7777)
        self.serverTCPAddress = ('127.0.0.1', 7778)

    def _initConversations(self):
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
