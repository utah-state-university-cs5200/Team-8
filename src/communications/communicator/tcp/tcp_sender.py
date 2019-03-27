from src.communications.communicator.sender import Sender


class TCPSender(Sender):
    def _sendData(self, buf):
        self.sock.sendall(buf)
