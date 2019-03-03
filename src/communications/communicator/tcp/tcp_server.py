import socket

from src.communications.communicator.server import Server
from src.communications.communicator.tcp.tcp_communicator import TCPCommunicator


class TCPServer(Server):
    def _initSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(self.address)
        self.sock.listen()

    def _createCommunicator(self, conn, addr):
        return TCPCommunicator(self.client, address=addr, sock=conn)

    def _addConnection(self, process_id, communicator):
        self.client.addTCPConnection(process_id, communicator)
