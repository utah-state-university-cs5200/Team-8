import socket

from src.communications.communicator.communicator import Communicator
from src.communications.communicator.sender import UDPSender
from src.communications.communicator.udp.udp_receiver import UDPReceiver


class UDPCommunicator(Communicator):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sender = UDPSender(communicator=self, socket=self.socket)
        self.receiver = UDPReceiver(communicator=self, socket=self.socket)
        self.sender.run()
        self.receiver.run()
