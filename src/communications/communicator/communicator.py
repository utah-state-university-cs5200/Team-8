from src.communications.communicator.constants import DEFAULT_SERVER_ADDRESS
from src.communications.conversation.envelope import Envelope


class Communicator:
    """
    Parent communicator class to be specialized
    """
    def __init__(self, dispatcher, address=None, sock=None):
        """
        Constructor

        :param dispatcher: Process that processes messages
        :param address: IP address for socket
        :param sock: Socket object if you want to pass in an existing socket
        """
        self.alive = True
        self.dispatcher = dispatcher
        self._initAddress(address)
        self._initSocket(sock)
        self.sender = None
        self.receiver = None

    def _initAddress(self, address):
        if address is None:
            self.address = DEFAULT_SERVER_ADDRESS
        else:
            self.address = address

    def _initSocket(self, sock):
        self.sock = sock

    def isActive(self):
        """
        Check if communicator is active

        :return: True if communicator is alive, false otherwise
        """
        return self.alive

    def sendMessage(self, message):
        """
        Forward a message to the sender's message queue

        :param message: Message to be sent over the socket
        :return:
        """
        self.sender.enqueueMessage(message)

    def sendEnvelope(self, envelope):
        """
        Send an envelope through the sender if it matches the address of this communicator

        :param envelope: envelope containing message and address
        """
        if envelope.address == self.address:
            self.sendMessage(envelope.message)
        else:
            pass # TODO: may want to log this - sending an envelope through the wrong communicator

    def enqueueTask(self, task):
        """
        Forward a task to the dispatcher as an envelope

        :param task: Task/message to be processed by the dispatcher
        :return:
        """
        envelope = Envelope(message=task, address=self.address)
        self.dispatcher.process(envelope)

    def cleanup(self):
        """
        Cleanup resources such as sockets when communicator is done

        :return:
        """
        self.alive = False
        self.sock.close()
