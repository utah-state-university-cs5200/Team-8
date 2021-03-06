from src.communications.communicator.sender import Sender


class UDPSender(Sender):
    def _sendData(self, buf):
        self.sock.sendto(buf, self.communicator.address)
