# import socket
# import time
# import unittest
# from unittest.mock import Mock
#
# from src.communications.communicator.tcp.tcp_communicator import TCPCommunicator
# from src.communications.communicator.tcp.tcp_listener import TCPListener
# from src.communications.messages.constants import MESSAGE_ID_HELLO
# from src.communications.messages.message_factory import MessageFactory
#
# class Envelope:
#     def __init__(self, address, message):
#         self.address = address
#         self.message = message
#
#
# class TestTCPCommunicator(unittest.TestCase):
#
#     def setUp(self):
#         self.mock_server = Mock()
#         self.mock_server.alive = True
#         self.mock_server.addTCPConnection = lambda process_id, communicator: print(process_id, communicator)
#         self.listener = TCPListener(client=self.mock_server, address=('0.0.0.0', 11111))
#         self.listener.start()
#
#         self.mock_client = Mock()
#         self.mock_client.alive = True
#         self.mock_client.enqueueTask = lambda message: message
#         self.communicator = TCPCommunicator(self.mock_client, (socket.gethostname(), 7776))
#
#     def tearDown(self):
#         self.mock_client.alive = False
#         self.mock_server.alive = False
#         self.communicator.cleanup()
#         self.listener.cleanup()
#
#     def testSendValidMessage(self):
#         m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias")
#         envelope = Envelope(('0.0.0.0', 11111), m1)
#         self.communicator.sendMessage(envelope)
#         time.sleep(1)
#         # TODO: verify listener creates a new connection, and receives the message
