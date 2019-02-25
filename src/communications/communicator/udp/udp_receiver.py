from src.communications.communicator.receiver import Receiver
from src.communications.encode_decode.decode import decode


class UDPReceiver(Receiver):
    def _receiveMessage(self):
        buffer = self.socket.recv(1024)
        return decode(buffer)
