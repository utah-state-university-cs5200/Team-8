from src.communications.client_test.client import Client
from src.communications.communicator.udp.udp_communicator import UDPCommunicator
from src.communications.messages.message_factory import MessageFactory


new_client = Client()
new_client.start()
test_comms = UDPCommunicator(new_client, ("127.0.0.1", 12001))
test_msg = MessageFactory.build(message_type_id=14, player_alias="David")
test_comms.sendMessage(test_msg, test_comms.address)
# new_client.alive = False
