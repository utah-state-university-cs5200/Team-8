import socket

from src.communications.communicator.listener import Listener
from src.communications.conversation.envelope import Envelope


class UDPListener(Listener):
    def run(self):
        self.sock.bind(self.address)
        while self.alive:
            message, address = self.sock.recvfrom(1024)
            envelope = Envelope(message=message, address=address)
            self.dispatchEnvelope(envelope)
        self.cleanup()

    def _initSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
