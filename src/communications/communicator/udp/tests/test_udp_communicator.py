import time
import unittest
from unittest.mock import Mock

from src.communications.communicator.udp.udp_communicator import UDPCommunicator
from src.communications.communicator.udp.udp_listener import UDPListener
from src.communications.messages.constants import MESSAGE_ID_HELLO
from src.communications.messages.message_factory import MessageFactory


class TestUDPCommunicator(unittest.TestCase):

    def setUp(self):
        self.mock_client = Mock()
        self.mock_client.alive = True
        self.mock_client.enqueueTask = lambda message: message
        self.communicator = UDPCommunicator(self.mock_client, ("127.0.0.1", 7777))
        self.listener = UDPListener(client=self.mock_client, address=("127.0.0.1", 7777))
        self.listener.start()

    def tearDown(self):
        self.mock_client.alive = False
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
