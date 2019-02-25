import socket

from src.communications.communicator.communicator import Communicator
from src.communications.communicator.tcp.tcp_sender import TCPSender
from src.communications.communicator.tcp.tcp_receiver import TCPReceiver


class TCPCommunicator(Communicator):
    def __init__(self, client, address=None):
        super().__init__(client, address)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(self.address)
        self.sender = TCPSender(communicator=self, socket=self.socket)
        self.receiver = TCPReceiver(communicator=self, socket=self.socket)
        self.sender.run()
        self.receiver.run()
