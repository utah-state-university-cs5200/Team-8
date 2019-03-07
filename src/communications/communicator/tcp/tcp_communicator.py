import socket

from src.communications.communicator.communicator import Communicator
from src.communications.communicator.constants import SOCKET_TIMEOUT
from src.communications.communicator.tcp.tcp_sender import TCPSender
from src.communications.communicator.tcp.tcp_receiver import TCPReceiver


def initTCPSocket(address, sock=None):
    if sock is None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(address)
    sock.settimeout(SOCKET_TIMEOUT)
    return sock


class TCPCommunicator(Communicator):
    def __init__(self, client, address=None, sock=None):
        super().__init__(client, address, sock)
        self.sender = TCPSender(communicator=self, sock=self.sock)
        self.receiver = TCPReceiver(communicator=self, sock=self.sock)
        self.sender.start()
        self.receiver.start()

    def _initSocket(self, sock):
        if not sock:
            self.sock = initTCPSocket(self.address, sock)
        else:
            self.sock = sock
