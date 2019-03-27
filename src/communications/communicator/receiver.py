import socket
import time
from threading import Thread

from src.communications.communicator.constants import THREAD_SLEEP_TIME
from src.communications.messages.encoder_decoder import decoding, DecodeError


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
                buf = self._receiveData()
                message = decoding(buf)
                self.communicator.enqueueTask(message)
            except socket.error:
                time.sleep(THREAD_SLEEP_TIME)
            except DecodeError:
                # TODO: may want to log whenever this happens
                pass

    def _receiveData(self):
        """
        Return bytes from the socket, if any

        :return: bytes from socket
        :raises socket.error: If no data is on the socket
        :raises DecodeError: If message could not be decoded
        """
        raise NotImplementedError
