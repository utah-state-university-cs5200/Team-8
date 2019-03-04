import socket

from src.communications.communicator.constants import SOCKET_TIMEOUT
from src.communications.communicator.listener import Listener
from src.communications.communicator.udp.udp_communicator import UDPCommunicator


class UDPListener(Listener):
    # TODO: UDP bind returns a message, address. Won't work like the tcp listener
    def run(self):
        self.sock.bind(self.address)
        while self.client.alive:
            buf, addr = self.sock.accept()
            process_id = self.client.getNextProcessID()
            conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            conn.connect(self.address)
            conn.settimeout(SOCKET_TIMEOUT)
            communicator = self._createCommunicator(conn, addr)
            self._addConnection(process_id, communicator)
        self.cleanup()

    def _initSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def _createCommunicator(self, conn, addr):
        return UDPCommunicator(self.client, address=addr, sock=conn)

    def _addConnection(self, process_id, communicator):
        self.client.addUDPConnection(process_id, communicator)
