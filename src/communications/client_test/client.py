import uuid
import queue
from threading import Thread


class Client:
    def __init__(self):
        self.alive = True
        self.ID = self._initID()
        self.taskQueue = queue.Queue()
        self.sendQueue = queue.Queue()
        self.type = Client

    def _initID(self):
        return uuid.uuid1()

    def enqueueTask(self, task):
        self.taskQueue.put(task)

