# import time
# import unittest
# from queue import Queue
# from threading import Thread
#
# from src.server.game_server.game_server import GameServer
# from src.communications.communicator.udp.udp_communicator import UDPCommunicator
# from src.communications.communicator.tcp.tcp_communicator import TCPCommunicator
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
# class Client(Thread):
#     def __init__(self, group=None, target=None, name=None, *args, **kwargs):
#         super().__init__()
#         self.alive = True
#         self._initAddress(kwargs)
#         self.udp_communicator = TCPCommunicator(client=self, address=self.address)
#         self.task_queue = Queue()
#
#     def _initAddress(self, kwargs):
#         self.address = ('172.0.0.1', 7171)
#         try:
#             self.address = kwargs['address']
#         except KeyError:
#             pass
#
#     def enqueueTask(self, task):
#         self.task_queue.put(task)
#
#     def sendMessage(self, message):
#         self.udp_communicator.sendMessage(message)
#
#
# class TestComs(unittest.TestCase):
#     def setUp(self):
#         self.server = GameServer(address=('0.0.0.0', 6666))
#         self.client = Client(address=("127.0.0.1", 7778))
#         self.server.start()
#         self.client.start()
#
#     def tearDown(self):
#         self.client.alive = False
#         self.server.alive = False
#
#     def testSendValidMessage(self):
#         # m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias")
#         message = "hello world"
#         envelope = Envelope(('0.0.0.0', 6666), message)
#         self.client.sendMessage(envelope)
#
#         time.sleep(1)
#
#         if not self.server.task_queue.empty():
#             task = self.server.task_queue.get()
#             self.assertEqual(message, task)
