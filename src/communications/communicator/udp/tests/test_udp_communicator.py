import unittest
from unittest.mock import Mock

from src.communications.communicator.udp.udp_communicator import UDPCommunicator
from src.communications.messages.constants import MESSAGE_ID_HELLO
from src.communications.messages.message_factory import MessageFactory


# TODO: WIP messing with mocking, sockets, and testing communicator
class TestUDPCommunicator(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mock_client = Mock()
        self.mock_client.alive = True
        self.mock_client.enqueueTask = lambda message : message
        self.communicator = UDPCommunicator(self.mock_client, ("127.0.0.1", 7777))
        self.server = UDPCommunicator(self.mock_client, ("127.0.0.1", 7777))
        # TODO: try and find a way to send messages from 2 communicators to each other

    def testSendValidMessage(self):
        m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias")
        self.communicator.sendMessage(m1)