import socket

from src.communications.communicator.listener import Listener
from src.communications.communicator.tcp.tcp_communicator import TCPCommunicator


class TCPListener(Listener):
    def _initSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _createCommunicator(self, conn, addr):
        return TCPCommunicator(self.client, address=addr, sock=conn)

    def _addConnection(self, process_id, communicator):
        self.client.addTCPConnection(process_id, communicator)
