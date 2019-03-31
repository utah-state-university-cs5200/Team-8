import socket
import time

from src.communications.communicator.constants import SOCKET_TIMEOUT, THREAD_SLEEP_TIME
from src.communications.communicator.listener import Listener
from src.communications.conversation.envelope import Envelope


class TCPListener(Listener):
    def run(self):
        self.sock.bind(self.address)
        self.sock.listen(5)
        while self.alive:
            try:
                conn, addr = self.sock.accept()
                while self.alive:
                    data = conn.recv(1024)
                    if data:
                        envelope = Envelope(message=data, address=addr)
                        self.dispatchEnvelope(envelope)
                    else:
                        break
                conn.close()
            except socket.timeout:
                time.sleep(THREAD_SLEEP_TIME)
            except ConnectionAbortedError:
                pass

    def _initSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(SOCKET_TIMEOUT)
