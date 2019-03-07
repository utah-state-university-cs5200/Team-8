from src.communications.communicator.sender import Sender


class TCPSender(Sender):
    def _sendData(self, buf, address):
        self.sock.connect(address)
        self.sock.sendall(buf)
