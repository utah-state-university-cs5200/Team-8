from threading import Thread


class Listener(Thread):
    """
    Parent listener class to be specialized.

    Receives connections and creates new sockets for those connections
    :note: Specializations must implement _initSocket, _createCommunicator and _addConnection methods
    """
    def __init__(self, dispatcher, address, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.dispatcher = dispatcher
        self.address = address
        self._initSocket()

    def _initSocket(self):
        raise NotImplementedError

    def run(self):
        self.sock.bind(self.address)
        self.sock.listen()
        while self.dispatcher.alive:
            conn, addr = self.sock.accept()
            process_id = self.dispatcher.getNextProcessID()
            communicator = self._createCommunicator(conn, addr)
            self._addConnection(process_id, communicator)
        self.cleanup()

    def cleanup(self):
        self.sock.close()

    def _createCommunicator(self, conn, addr):
        raise NotImplementedError

    def _addConnection(self, process_id, communicator):
        raise NotImplementedError
