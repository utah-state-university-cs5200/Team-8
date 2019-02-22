from src.communications.communicator.communicator import Communicator


class TCPCommunicator(Communicator):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.socket = None
        self.sender = None
        self.receiver = None
