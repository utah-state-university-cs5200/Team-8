import socket

from src.communications.communicator.listener import Listener
from src.communications.communicator.udp.udp_communicator import UDPCommunicator


class UDPListener(Listener):
    def _initSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def _createCommunicator(self, conn, addr):
        return UDPCommunicator(self.client, address=addr, sock=conn)

    def _addConnection(self, process_id, communicator):
        self.client.addUDPConnection(process_id, communicator)
