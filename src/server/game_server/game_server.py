from queue import Queue
from threading import Thread

from src.communications.communicator.tcp.tcp_communicator import TCPCommunicator
from src.communications.communicator.udp.udp_communicator import UDPCommunicator


class GameServer(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.alive = True
        self.tcp_communicator = TCPCommunicator(self)
        self.udp_communicator = UDPCommunicator(self)
        self.tcp_comm_pool = {}
        self.udp_comm_pool = {}
        self.task_queue = Queue()

    def enqueueTask(self, task):
        self.task_queue.put(task)

    def addTCPConnection(self, process_id, address, sock):
        communicator = TCPCommunicator(self, address, sock)
        self.tcp_comm_pool[process_id] = communicator

    def addUDPConnection(self, process_id, address, sock):
        communicator = UDPCommunicator(self, address, sock)
        self.udp_comm_pool[process_id] = communicator
