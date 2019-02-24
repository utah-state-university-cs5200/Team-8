

class Communicator:
    """
    Parent communicator class to be specialized
    """
    def __init__(self, *args, **kwargs):
        self.client = kwargs['client']
        self.socket = None
        self.sender = None
        self.receiver = None

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
