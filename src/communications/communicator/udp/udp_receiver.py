from src.communications.communicator.receiver import Receiver


class UDPReceiver(Receiver):
    def _receiveMessage(self):
        buffer = self.sock.recv(1024)
        return decode(buffer)
