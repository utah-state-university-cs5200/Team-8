import socket

from src.communications.communicator.listener import Listener
from src.communications.communicator.udp.udp_communicator import UDPCommunicator, initUDPSocket
from src.communications.messages.encoder_decoder import encoding


class UDPListener(Listener):
    def run(self):
        self.sock.bind(self.address)
        while self.dispatcher.alive:
            buf, addr = self.sock.accept()
            process_id = self.dispatcher.getNextProcessID()
            conn = initUDPSocket(addr)
            communicator = self._createCommunicator(conn, addr)
            communicator.enqueueTask(encoding(buf))
            self._addConnection(process_id, communicator)
        self.cleanup()

    def _initSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def _createCommunicator(self, conn, addr):
        return UDPCommunicator(self.dispatcher, address=addr, sock=conn)

    def _addConnection(self, process_id, communicator):
        self.dispatcher.addUDPConnection(process_id, communicator)
