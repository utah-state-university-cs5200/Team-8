from src.communications.communicator.envelope import Envelope


class Communicator:
    """
    Parent communicator class to be specialized
    """
    def __init__(self, client, address=None):
        """
        Constructor

        :param client: Client program
        :param address: IP address for socket
        """
        self.client = client
        self.address = self._initAddress(address)
        self.socket = None
        self.sender = None
        self.receiver = None
        self.returnaddr = None

    def _initAddress(self, address):
        if address is None:
            pass # TODO: Make an address automatigically if it isn't provided
        else:
            return address

    def isActive(self):
        """
        Check if communicator is active

        :return: True if client is alive, false otherwise
        """
        return self.client.alive

    def sendMessage(self, message, address):
        """
        Forward a message to the sender's message queue

        :param message: Message to be sent over the socket
        :param address: Address tuple (IP, PORT)
        :return:
        """

        self.sender.enqueueMessage(Envelope(message, address))

    def enqueueTask(self, task):
        """
        Forward a task to the client's task queue

        :param task: Task/message to be processed by the client
        :return:
        """
        self.client.enqueueTask(task)
