import socket

from src.communications.communicator.server import Server
from src.communications.communicator.udp.udp_communicator import UDPCommunicator


class UDPServer(Server):
    def _initSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.address)
        self.sock.listen()

    def _createCommunicator(self, conn, addr):
        return UDPCommunicator(self.client, address=addr, sock=conn)

    def _addConnection(self, process_id, communicator):
        self.client.addUDPConnection(process_id, communicator)
