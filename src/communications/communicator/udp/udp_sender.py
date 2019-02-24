from src.communications.communicator.sender import Sender


class UDPSender(Sender):
    def _sendMessage(self, message):
        self.socket.send(encode(message))