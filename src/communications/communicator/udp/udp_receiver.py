from src.communications.communicator.receiver import Receiver


class UDPReceiver(Receiver):
    def _receiveData(self):
        return self.sock.recv(1024)
