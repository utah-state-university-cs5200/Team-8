from threading import Thread


class Server(Thread):
    """
    Parent server class to be specialized.

    Receives connections and creates new sockets for those connections
    :note: Specializations must implement _initSocket, _createCommunicator and _addConnection methods
    """
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.client = kwargs['client']
        self.address = kwargs['address']
        self._initSocket()

    def _initSocket(self):
        raise NotImplementedError

    def run(self):
        while self.client.alive:
            conn, addr = self.sock.accept()
            process_id = self.client.getNextProcessID()
            communicator = self._createCommunicator(conn, addr)
            self._addConnection(process_id, communicator)
        self.cleanup()

    def cleanup(self):
        self.sock.close()

    def _createCommunicator(self, conn, addr):
        raise NotImplementedError

    def _addConnection(self, process_id, communicator):
        raise NotImplementedError
