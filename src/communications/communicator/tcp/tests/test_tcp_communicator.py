import time
import unittest
from unittest.mock import Mock

from src.communications.communicator.tcp.tcp_communicator import TCPCommunicator
from src.communications.communicator.tcp.tcp_listener import TCPListener
from src.communications.messages.constants import MESSAGE_ID_HELLO
from src.communications.messages.message_factory import MessageFactory


class TestTCPCommunicator(unittest.TestCase):

    def setUp(self):
        self.mock_client = Mock()
        self.mock_client.alive = True
        self.mock_client.enqueueTask = lambda message: message
        self.communicator = TCPCommunicator(self.mock_client, ("127.0.0.1", 7779))

        self.mock_server = Mock()
        self.mock_server.alive = True
        self.mock_server.addTCPConnection = lambda process_id, communicator: (process_id, communicator)
        self.listener = TCPListener(client=self.mock_server, address=("127.0.0.1", 7779))
        self.listener.start()
        # TODO: fix connection refused error

    def tearDown(self):
        self.mock_client.alive = False
        self.mock_server.alive = False
        self.communicator.cleanup()
        self.listener.cleanup()
        while self.communicator.sender.is_alive() or self.communicator.receiver.is_alive() or self.listener.is_alive():
            print(self.communicator.sender.is_alive(), self.communicator.receiver.is_alive(), self.listener.is_alive())
            time.sleep(1)
        # TODO: figure out why sockets aren't getting closed. May need to use a resource manager('with' statement)

    def testSendValidMessage(self):
        m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias")
        self.communicator.sendMessage(m1)
        # TODO: verify listener creates a new udp connection, and recieves the message
