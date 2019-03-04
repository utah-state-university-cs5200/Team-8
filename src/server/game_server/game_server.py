from queue import Queue
from threading import Thread

from src.communications.communicator.constants import DEFAULT_GAME_SERVER_ADDRESS
from src.communications.communicator.tcp.tcp_listener import TCPListener
from src.communications.communicator.udp.udp_listener import UDPListener


class GameServer(Thread):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.alive = True
        self._initAddress(kwargs)
        self.tcp_listener = TCPListener(address=self.address, client=self)
        self.udp_listener = UDPListener(address=self.address, client=self)
        self.tcp_comm_pool = {}
        self.udp_comm_pool = {}
        self.task_queue = Queue()
        
    def _initAddress(self, kwargs):
        self.address = DEFAULT_GAME_SERVER_ADDRESS
        try:
            self.address = kwargs['address']
        except KeyError:
            pass

    def enqueueTask(self, task):
        self.task_queue.put(task)

    def addTCPConnection(self, process_id, tcp_communicator):
        self.tcp_comm_pool[process_id] = tcp_communicator

    def addUDPConnection(self, process_id, udp_communicator):
        self.udp_comm_pool[process_id] = udp_communicator

    def getNextProcessID(self):
        return 1 # TODO: return a new unique process id for connecting processes
