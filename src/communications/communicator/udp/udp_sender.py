from src.communications.communicator.sender import Sender
from src.communications.encode_decode.encode import encode


class UDPSender(Sender):
    def _sendMessage(self, message):
        self.socket.send(encode(message))
