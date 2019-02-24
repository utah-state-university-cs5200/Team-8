import time
from queue import Queue, Empty
from threading import Thread


# TODO: temporary, clean this up later
SLEEP_TIME = 50

# TODO: implement encode(message) method

class UDPSender(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.communicator = kwargs['communicator']
        self.socket = kwargs['socket']
        self.message_queue = Queue()

    def run(self):
        while self.communicator.isActive():
            try:
                message = self.message_queue.get(block=False)
                self._sendMessage(message)
            except Empty:
                time.sleep(SLEEP_TIME)

    def enqueueMessage(self, message):
        self.message_queue.put(message)

    def _sendMessage(self, message):
        self.socket.send(encode(message))
