import socket
import time

from src.communications.communicator.constants import SOCKET_TIMEOUT, THREAD_SLEEP_TIME
from src.communications.communicator.listener import Listener
from src.communications.conversation.envelope import Envelope


class UDPListener(Listener):
    def run(self):
        self.sock.bind(self.address)
        while self.alive:
            try:
                message, address = self.sock.recvfrom(1024)
                envelope = Envelope(message=message, address=address)
                self.dispatchEnvelope(envelope)
            except socket.timeout:
                time.sleep(THREAD_SLEEP_TIME)

    def _initSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(SOCKET_TIMEOUT)
