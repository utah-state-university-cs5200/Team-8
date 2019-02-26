from src.communications.server_test.server import Server
from src.communications.communicator.udp.udp_communicator import UDPCommunicator
from src.communications.messages.message_factory import MessageFactory

new_server = Server()
test_comms = UDPCommunicator(new_server, ("127.0.0.1", 12001))
print("starting server")
new_server.start()

while True:
    if new_server.message is not None:
        test_msg = MessageFactory.build(message_type_id=1, request_id=1, message_status=0)
        test_comms.sendMessage(test_msg)
        new_server.message = None
