import time
import queue

from enum import Enum
from threading import Thread

from src.communications.communicator.udp.udp_communicator import UDPCommunicator
from src.communications.conversation.envelope import Envelope

DEFAULT_TIMEOUT = 30
DEFAULT_MAX_RETRY = 3


class PossibleState(Enum):
    NOT_INITIALIZED = 1
    WORKING = 2
    FAILED = 3
    SUCCEEDED = 4


class Conversation(Thread):
    """
    Parent Conversation class to be specialized

    :note: Specializations must implement _execute_details()
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self._alive = True
        self._incoming_messages = queue.Queue()
        self._valid_incoming_message_types = set()
        self._possible_state = PossibleState.NOT_INITIALIZED

        self.conversation_id = None
        self.remote_endpoint = None
        self.timeout = None
        self.max_retry = None

        self._initComSystem()
        self._initWorker(kwargs)
        self._init_timeout(kwargs)
        self._init_max_retry(kwargs)

    def run(self):
        self._initComSystem()
        self._possible_state = PossibleState.WORKING
        self._execute_details()
        self.cleanup()

    def _execute_details(self):
        raise NotImplementedError

    def process(self, envelope):
        """
        Add incoming envelope to internal message queue

        :param envelope:
        :return:
        """
        if self._is_envelope_valid(envelope):
            self._incoming_messages.put(envelope)
        else:
            print('Invalid incoming envelope')

    def _do_reliable_request(self, outgoing_envelope):
        """
        Implements the Reliable Request (RR) messaging protocol.
        Will retry as many times as specified in self.max_retry.
        Waits self.timeout seconds between retries.

        :param outgoing_envelope:
        :return: first incoming envelope found on the message queue
        """
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
            elif incoming_envelope.message.message_type_id not in self._valid_incoming_message_types:
                # Not a message type this conversation is expecting
                incoming_envelope = None

        return incoming_envelope

    def _wait_for_response(self):
        """
        Waits for first message on message queue.s
        Will retry as many times as specified in self.max_retry.
        Waits self.timeout seconds between retries.

        :return incoming_envelope: first incoming envelope found on the message queue
        """
        incoming_envelope = None

        remaining_sends = self.max_retry
        while remaining_sends > 0 and not incoming_envelope:
            remaining_sends -= 1

            if self._incoming_messages.empty():
                time.sleep(self.timeout)

            try:
                incoming_envelope = self._incoming_messages.get(block=False)
            except queue.Empty:
                incoming_envelope = None

            if not incoming_envelope or not self._is_envelope_valid(incoming_envelope):
                incoming_envelope = None
            elif incoming_envelope.message.message_type_id not in self._valid_incoming_message_types:
                incoming_envelope = None

        return incoming_envelope

    @staticmethod
    def _is_envelope_valid(envelope):
        """
        :param envelope: Envelope
        :return: Bool
        """
        if envelope and type(Envelope()) == type(envelope):
            if envelope.message and envelope.address:
                return True
        return False

    def is_alive(self):
        if self._alive and not self._possible_state == PossibleState.FAILED:
            return True
        else:
            return False

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

    def _initComSystem(self):
        self.com_system = None
        self.com_system = UDPCommunicator(address=self.remote_endpoint, dispatcher=self)

    def cleanup(self):
        self._alive = False

        if self.com_system:
            self.com_system.cleanup()
