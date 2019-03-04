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
        self.sock = kwargs['sock']

    def run(self):
        while self.communicator.isActive():
            try:
                message = self._receiveMessage()
                self.communicator.enqueueTask(message)
            except socket.error as e:
                print(e)
                time.sleep(SLEEP_TIME)
            except DecodeError:
                # TODO: may want to log whenever this happens
                pass
        self.communicator.cleanup()

    def _receiveMessage(self):
        """
        Create a message from the incoming bytes from the socket, if any

        :return: Message object
        :raises socket.error: If no data is on the socket
        :raises DecodeError: If message could not be decoded
        """
        raise NotImplementedError
