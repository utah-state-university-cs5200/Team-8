import socket
import traceback
from src.communications.communicator.communicator import Communicator
from src.communications.communicator.constants import SOCKET_TIMEOUT
from src.communications.communicator.udp.udp_sender import UDPSender
from src.communications.communicator.udp.udp_receiver import UDPReceiver


def initUDPSocket(address, sock=None):
    if sock is None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.connect(address)
    sock.settimeout(SOCKET_TIMEOUT)
    return sock


class UDPCommunicator(Communicator):
    def __init__(self, dispatcher, address=None, sock=None):
        super().__init__(dispatcher, address, sock)
        # self._initSocket(sock)
        self.sender = UDPSender(communicator=self, sock=self.sock)
        self.receiver = UDPReceiver(communicator=self, sock=self.sock)
        self.sender.start()
        self.receiver.start()

    def _initSocket(self, sock):
        if not sock:
            self.sock = initUDPSocket(self.address, sock)
            # print('\n')
            # print('!!!not sock', self.sock)
            # traceback.print_stack()
            # print('\n')
        else:
            self.sock = sock
