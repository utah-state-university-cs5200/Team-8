from src.communications.communicator.sender import Sender
from src.communications.encode_decode.encode import encode


class UDPSender(Sender):
    def _sendMessage(self, envelope):
        print("Sent: " + str(envelope.message.__dict__))
        self.socket.sendto(encode(envelope), envelope.address)
