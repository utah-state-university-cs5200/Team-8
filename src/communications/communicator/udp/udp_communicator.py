import socket

from src.communications.communicator.communicator import Communicator
from src.communications.communicator.udp.udp_sender import UDPSender
from src.communications.communicator.udp.udp_receiver import UDPReceiver


class UDPCommunicator(Communicator):
    def __init__(self, client, address=None):
        super().__init__(client, address)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # only can bind socket once...
        if client.type == "Server":
            self.socket.bind(self.address)

        self.sender = UDPSender(communicator=self, socket=self.socket)
        self.receiver = UDPReceiver(communicator=self, socket=self.socket)
        print("Start sender")
        self.sender.start()
        print("start receiver")
        self.receiver.start()

