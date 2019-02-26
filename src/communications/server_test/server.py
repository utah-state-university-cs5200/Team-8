import uuid
import queue
from threading import Thread


class Server(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.alive = True
        self.ID = self._initID()
        self.taskQueue = queue.Queue()
        self.sendQueue = queue.Queue()
        self.message = None
        self.type = "Server"

    def _initID(self):
        return uuid.uuid1()

    def enqueueTask(self, task):
        self.taskQueue.put(task)

    def printMsg(self):
        print(self.message.__dict__)

    def run(self):
        while self.alive:
            if not self.taskQueue.empty():
                print("Message in Queue.")
                self.message = self.taskQueue.get()
                self.printMsg()

