from src.communications.communicator.receiver import Receiver
from src.communications.encode_decode.decode import decode


class UDPReceiver(Receiver):
    def _receiveMessage(self):
        buffer = self.socket.recvfrom(4096)
        return decode(buffer[0]), buffer[1]
