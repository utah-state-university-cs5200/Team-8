import socket
import time
from threading import Thread

# TODO: temporary, clean this up later
SLEEP_TIME = 50

# TODO: implement decode(message) method
# TODO: implement DecodeError if message cannot be decoded succesfuly


class UDPReceiver(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.communicator = kwargs['communicator']
        self.socket = kwargs['socket']

    def run(self):
        while self.communicator.isActive():
            try:
                buf = self.socket.recv(1024)
                if len(buf) > 0:
                    message = self._decodeBuffer(buf)
                    self.communicator.enqueueTask(message)
            except socket.error:
                time.sleep(SLEEP_TIME)
            except DecodeError:
                pass

    def _decodeBuffer(self, buf):
        """
        Create a message by decoding the incoming buffer

        :param buf: bytestring containing encoded message
        :return: A message object
        :raises DecodeError: If a message cannot be created from the buffer
        """
        return decode(buf)
