import socket
import time
from threading import Thread

from src.communications.communicator.constants import THREAD_SLEEP_TIME


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
                buf = self._receiveMessage()
                message = decode(buf)
                self.communicator.enqueueTask(message)
            except socket.error:
                time.sleep(THREAD_SLEEP_TIME)
            except DecodeError:
                # TODO: may want to log whenever this happens
                pass
        self.communicator.cleanup()

    def _receiveMessage(self):
        """
        Create a message from the incoming bytes from the socket, if any

        :return: bytes from socket
        :raises socket.error: If no data is on the socket
        :raises DecodeError: If message could not be decoded
        """
        raise NotImplementedError
