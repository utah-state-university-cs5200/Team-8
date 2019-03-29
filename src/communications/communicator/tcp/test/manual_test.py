import time

from src.communications.communicator.tcp.tcp_communicator import TCPCommunicator
from src.communications.communicator.tcp.tcp_listener import TCPListener
from src.communications.messages.constants import MESSAGE_ID_HELLO
from src.communications.messages.message_factory import MessageFactory


class MockDispatcher:
    def processEnvelope(self, envelope):
        print("Received {}".format(envelope))

mock_dispatcher = MockDispatcher()
server_address = ('127.0.0.1', 7777)
tcp_listener = TCPListener(dispatcher=mock_dispatcher, address=server_address)

tcp_communicator = TCPCommunicator(dispatcher=mock_dispatcher, address=server_address)

id_vals = {'message_id':2, 'sender_id':1}
m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias", **id_vals)
print("Sending {}".format(m1))
tcp_communicator.sendMessage(m1)

time.sleep(1)

