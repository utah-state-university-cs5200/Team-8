from src.communications.communicator.sender import Sender


class TCPSender(Sender):
    def _sendMessage(self, message):
        self.sock.sendall(encode(message))
