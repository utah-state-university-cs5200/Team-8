import time
from threading import Thread

from src.communications.communicator.constants import THREAD_SLEEP_TIME
from src.communications.messages.encoder_decoder import EncodeError, encode


class Sender(Thread):
    """
    Parent sender class to be specialized

    :note: Specializations must implement _sendMessage()
    """
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.communicator = kwargs['communicator']
        self.sock = kwargs['sock']
        self.message_queue = []

    def run(self):
        while self.communicator.isActive():
            try:
                if len(self.message_queue) == 0:
                    time.sleep(THREAD_SLEEP_TIME)
                else:
                    message = self.message_queue.pop(0)
                    buf = encode(message)
                    self._sendData(buf)
            except EncodeError:
                pass # TODO: may want to log this

    def enqueueMessage(self, message):
        self.message_queue.append(message)

    def _sendData(self, buf):
        """
        Send bytes through the socket

        :param buf: bytesstring to be sent
        :return:
        """
        raise NotImplementedError