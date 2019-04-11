import time
import unittest

from src.communications.communicator.test.mock_dispatcher import MockDispatcher
from src.communications.communicator.udp.udp_communicator import UDPCommunicator
from src.communications.communicator.udp.udp_listener import UDPListener
from src.communications.messages.constants import MESSAGE_ID_HELLO
from src.communications.messages.encoder_decoder import decode
from src.communications.messages.message_factory import MessageFactory


class TestUDPCommunicator(unittest.TestCase):
    @unittest.skip('key error conversation id at message factory')
    def testSuccessfulSendAndReceive(self):
        mock_dispatcher = MockDispatcher()
        server_address = ('127.0.0.1', 7777)
        udp_listener = UDPListener(dispatcher=mock_dispatcher, address=server_address)
        udp_listener.start()

        udp_communicator = UDPCommunicator(dispatcher=mock_dispatcher, address=server_address)

        id_vals = {'message_id':2, 'sender_id':1}
        m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias", **id_vals)
        udp_communicator.sendMessage(m1)

        time.sleep(.5)
        self.assertEqual(m1.getAttributes(), decode(mock_dispatcher.received[0].message).getAttributes())

        udp_communicator.cleanup()
        udp_listener.cleanup()
        time.sleep(.5)
