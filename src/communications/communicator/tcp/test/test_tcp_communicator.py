import time
import unittest

from src.communications.communicator.tcp.tcp_communicator import TCPCommunicator
from src.communications.communicator.tcp.tcp_listener import TCPListener
from src.communications.communicator.test.mock_dispatcher import MockDispatcher
from src.communications.messages.constants import MESSAGE_ID_HELLO
from src.communications.messages.encoder_decoder import decode
from src.communications.messages.message_factory import MessageFactory


class TestTCPCommunicator(unittest.TestCase):
    def testSuccessfulSendAndReceive(self):
        mock_dispatcher = MockDispatcher()
        server_address = ('127.0.0.1', 7777)
        tcp_listener = TCPListener(dispatcher=mock_dispatcher, address=server_address)
        tcp_listener.start()

        tcp_communicator = TCPCommunicator(dispatcher=mock_dispatcher, address=server_address)

        id_vals = {'message_id':2, 'sender_id':1, 'conversation_id':0}
        m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias", **id_vals)
        tcp_communicator.sendMessage(m1)

        time.sleep(.5)
        self.assertEqual(m1.getAttributes(), decode(mock_dispatcher.received[0].message).getAttributes())

        tcp_communicator.cleanup()
        tcp_listener.cleanup()
        time.sleep(.5)
