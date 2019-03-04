import socket

from src.communications.communicator.communicator import Communicator
from src.communications.communicator.constants import SOCKET_TIMEOUT
from src.communications.communicator.tcp.tcp_sender import TCPSender
from src.communications.communicator.tcp.tcp_receiver import TCPReceiver


class TCPCommunicator(Communicator):
    def __init__(self, client, address=None, sock=None):
        super().__init__(client, address, sock)
        self._initSocket(sock)
        self.sender = TCPSender(communicator=self, sock=self.sock)
        self.receiver = TCPReceiver(communicator=self, sock=self.sock)
        self.sender.start()
        self.receiver.start()

    def _initSocket(self, sock):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.sock.connect(self.address)
        self.sock.settimeout(SOCKET_TIMEOUT)
