import time
import queue

from enum import Enum
from threading import Thread

from src.communications.communicator.udp.udp_communicator import UDPCommunicator
from src.communications.conversation.envelope import Envelope


DEFAULT_TIMEOUT = 30
DEFAULT_MAX_RETRY = 3



class PossibleState(Enum):
    NotInitialized = 1
    Working = 2
    Failed = 3
    Succeeded = 4


# Abstract class
#   you need to implement the following methods
#       _execute_details
class Conversation(Thread):
    def __init__(self, conversation_id, remote_endpoint, *args, **kwargs):
        super().__init__()
        self._alive = True
        self._incoming_messages = queue.Queue()
        self._possible_state = PossibleState

        self.conversation_id = conversation_id
        self.remote_endpoint = remote_endpoint
        self.timeout = None
        self.max_retry = None

        self._initComSystem()
        self._initWorker(kwargs)
        self._init_timeout(kwargs)
        self._init_max_retry(kwargs)

    def run(self):
        self._execute_details()
        self.cleanup()

    def process(self, envelope):
        if self._is_envelope_valid(envelope):
            self._incoming_messages.put(envelope)
        else:
            print('Invalid incoming envelope')

    def is_alive(self):
        return self._alive

    def _execute_details(self):
        raise NotImplementedError

    def _is_envelope_valid(self, envelope):
        if envelope and type(Envelope()) == type(envelope):
            # has_message = communications.messages in str(type(envelope.message).__bases__[0])
            # has_address = len(envelope.address) ==2
            # if has_message and has_address:
            if envelope.message and envelope.address :
                return True
        return False

    def _do_reliable_request(self, outgoing_envelope):
        incoming_envelope = None

        remaining_sends = self.max_retry
        while remaining_sends > 0 and not incoming_envelope:
            remaining_sends -= 1

            self.com_system.sendMessage(outgoing_envelope)

            if self._incoming_messages.empty():
                time.sleep(self.timeout)

            try:
                incoming_envelope = self._incoming_messages.get(block=False)
            except queue.Empty:
                incoming_envelope = None

            if not incoming_envelope or not self._is_envelope_valid(incoming_envelope):
                incoming_envelope = None

        return incoming_envelope

    def _initComSystem(self):
        self.com_system = None
        self.com_system = UDPCommunicator(address=self.remote_endpoint, dispatcher=self)

    def _initWorker(self, kwargs):
        try:
            self.worker = kwargs['worker']
        except KeyError:
            self.worker = None

    def _init_max_retry(self, kwargs):
        try:
            self.max_retry = kwargs['max_retry']
        except KeyError:
            self.max_retry = DEFAULT_MAX_RETRY

    def _init_timeout(self, kwargs):
        try:
            self.timeout = kwargs['timeout']
        except KeyError:
            self.timeout = DEFAULT_TIMEOUT

    def cleanup(self):
        self._alive = False
        self.com_system.cleanup()
