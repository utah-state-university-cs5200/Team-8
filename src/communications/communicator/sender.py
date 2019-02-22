import logging
import time
from queue import Queue, Empty
from threading import Thread


class Sender(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.client = kwargs['client']
        self.socket = kwargs['socket']
        self.message_queue = Queue()

    def run(self):
        while self.client.alive:
            try:
                message = self.message_queue.get(block=False)
                self._sendMessage(message)
            except Empty:
                time.sleep(SLEEP_TIME)

    def setSocket(self, socket):
        self.socket = socket

    def enqueueMessage(self, message):
        logging.debug("Sender enqueueing message with id: {}".format(message.id))
        self.message_queue.put(message)

    def _sendMessage(self, message):
        logging.info("Sender sending bytes: {}".format(message.encode()))
        self.socket.send(message.encode())
