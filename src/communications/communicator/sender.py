import time
from queue import Queue, Empty
from threading import Thread

from src.communications.communicator.constants import THREAD_SLEEP_TIME
from src.communications.messages.encoder_decoder import EncodeError, encoding


class Sender(Thread):
    """
    Parent sender class to be specialized

    :note: Specializations must implement _sendMessage()
    """
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.communicator = kwargs['communicator']
        self.sock = kwargs['sock']
        self.message_queue = Queue()

    def run(self):
        while self.communicator.isActive():
            try:
                message = self.message_queue.get(block=False)
                buf = encoding(message)
                self._sendData(buf)
            except Empty:
                time.sleep(THREAD_SLEEP_TIME)
            except EncodeError:
                pass # TODO: may want to log this
        self.communicator.cleanup()

    def enqueueMessage(self, message):
        self.message_queue.put(message)

    def _sendData(self, buf):
        """
        Send bytes through the socket

        :param buf: bytesstring to be sent
        :return:
        """
        raise NotImplementedError