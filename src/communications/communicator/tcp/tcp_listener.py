import socket

from src.communications.communicator.listener import Listener
from src.communications.conversation.envelope import Envelope


class TCPListener(Listener):
    def run(self):
        self.sock.bind(self.address)
        self.sock.listen(1)
        while self.alive:
            conn, addr = self.sock.accept()
            buf = b''
            try:
                while True:
                    data = conn.recv(16)
                    if data:
                        buf += data
                    else:
                        envelope = Envelope(message=buf, address=addr)
                        self.dispatchEnvelope(envelope)
            except ConnectionAbortedError:
                pass
            finally:
                conn.close()
        self.cleanup()

    def _initSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
