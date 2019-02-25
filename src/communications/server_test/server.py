import uuid
import queue
from threading import Thread


class Server(Thread):
    def __init__(self):
        self.alive = True
        self.ID = self._initID()
        self.taskQueue = queue.Queue()
        self.message = None

    def _initID(self):
        return uuid.uuid1()

    def enqueueTask(self, task):
        self.taskQueue.put(task)

    def printMsg(self):
        print(self.message.__dict__)

    def run(self):
        while self.alive:
            if not self.taskQueue.empty():
                self.message = self.taskQueue.get()
                self.printMsg()
