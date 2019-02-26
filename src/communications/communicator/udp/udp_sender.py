from src.communications.communicator.sender import Sender
from src.communications.encode_decode.encode import encode


class UDPSender(Sender):
    def _sendMessage(self, message):
        print("Sent: " + str(message.__dict__))
        self.socket.sendto(encode(message), self.communicator.address)
