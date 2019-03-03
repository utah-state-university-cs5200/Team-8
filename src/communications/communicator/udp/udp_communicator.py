import socket

from src.communications.communicator.communicator import Communicator
from src.communications.communicator.udp.udp_sender import UDPSender
from src.communications.communicator.udp.udp_receiver import UDPReceiver


class UDPCommunicator(Communicator):
    def __init__(self, client, address=None, sock=None):
        super().__init__(client, address, sock)
        self._initSocket(sock)
        self.sender = UDPSender(communicator=self, sock=self.sock)
        self.receiver = UDPReceiver(communicator=self, sock=self.sock)
        self.sender.run()
        self.receiver.run()

    def _initSocket(self, sock):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.sock = sock
        self.sock.connect(self.address)
