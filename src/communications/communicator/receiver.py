import socket
import time
from threading import Thread

# TODO: temporary, clean this up later
SLEEP_TIME = 50

# TODO: implement decode(message) method
# TODO: implement DecodeError if message cannot be decoded successfully


class Receiver(Thread):
    """
    Parent receiver class to be specialized

    :note: Specializations must implement _receiveMessage()
    """
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.communicator = kwargs['communicator']
        self.socket = kwargs['socket']

    def run(self):
        while self.communicator.isActive():
            try:
                envelope, addr = self._receiveMessage()
                self.communicator.returnaddr = addr
                print(addr)
                self.communicator.enqueueTask(envelope)
            except socket.error:
                pass # time.sleep(SLEEP_TIME)   # doesn't continue loop when ran?
            #except DecodeError:
                # TODO: may want to log whenever this happens
               # pass

    def _receiveMessage(self):
        """
        Create a message from the incoming bytes from the socket, if any

        :return: Message object
        :raises socket.error: If no data is on the socket
        :raises DecodeError: If message could not be decoded
        """
        raise NotImplementedError
