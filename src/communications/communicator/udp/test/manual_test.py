import time

from src.communications.communicator.udp.udp_communicator import UDPCommunicator
from src.communications.communicator.udp.udp_listener import UDPListener
from src.communications.messages.constants import MESSAGE_ID_HELLO
from src.communications.messages.message_factory import MessageFactory


class MockDispatcher:
    def processEnvelope(self, envelope):
        print("Received {} from {}".format(envelope.message, envelope.address))

mock_dispatcher = MockDispatcher()
server_address = ('127.0.0.1', 7777)
udp_listener = UDPListener(dispatcher=mock_dispatcher, address=server_address)
udp_listener.start()

udp_communicator = UDPCommunicator(dispatcher=mock_dispatcher, address=server_address)

id_vals = {'message_id':2, 'sender_id':1}
m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias", **id_vals)
print("Sending {}".format(m1.getAttributes()))
udp_communicator.sendMessage(m1)

time.sleep(1)
print("Cleaning up...")
udp_communicator.cleanup()
udp_listener.cleanup()
