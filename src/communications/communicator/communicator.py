from src.communications.communicator.constants import DEFAULT_SERVER_ADDRESS


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

    def _initAddress(self, address):
        if address is None:
            return DEFAULT_SERVER_ADDRESS
        else:
            return address

    def isActive(self):
        """
        Check if communicator is active

        :return: True if client is alive, false otherwise
        """
        return self.client.alive

    def sendMessage(self, message):
        """
        Forward a message to the sender's message queue

        :param message: Message to be sent over the socket
        :return:
        """
        self.sender.enqueueMessage(message)

    def enqueueTask(self, task):
        """
        Forward a task to the client's task queue

        :param task: Task/message to be processed by the client
        :return:
        """
        self.client.enqueueTask(task)

    def cleanup(self):
        """
        Cleanup resources such as sockets when communicator is done

        :return:
        """
        self.socket.close()
