from src.communications.server_test.server import Server
from src.communications.communicator.udp.udp_communicator import UDPCommunicator
from src.communications.messages.message_factory import MessageFactory

new_server = Server()
test_comms = UDPCommunicator(new_server, ("127.0.0.1", 12001))
new_server.run()
