# import time
# import unittest
# from unittest.mock import Mock
#
# from src.communications.communicator.udp.udp_communicator import UDPCommunicator
# from src.communications.communicator.udp.udp_listener import UDPListener
# from src.communications.messages.constants import MESSAGE_ID_HELLO
# from src.communications.messages.message_factory import MessageFactory
#
#
# class Envelope:
#     def __init__(self, address, message):
#         self.address = address
#         self.message = message
#
#
# class TestUDPCommunicator(unittest.TestCase):
#
#     def setUp(self):
#         self.mock_client = Mock()
#         self.mock_client.alive = True
#         self.mock_client.enqueueTask = lambda message: message
#         self.communicator = UDPCommunicator(self.mock_client, ("127.0.0.1", 7777))
#         self.listener = UDPCommunicator(self.mock_client, ("127.0.0.1", 7778))
#         # self.listener = UDPListener(client=self.mock_client, address=("127.0.0.1", 7778))
#         # self.listener.start()
#
#     def tearDown(self):
#         self.mock_client.alive = False
#         self.communicator.cleanup()
#         self.listener.cleanup()
#
#
#     def testSendValidMessage(self):
#         m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias")
#         envelope = Envelope(("127.0.0.1", 7778), m1)
#         self.communicator.sendMessage(envelope)
#         time.sleep(1)
#         # TODO: verify listener creates a new udp connection, and recieves the message
