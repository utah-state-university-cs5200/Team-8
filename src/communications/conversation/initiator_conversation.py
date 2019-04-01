from src.communications.conversation.conversation import Conversation
from src.communications.conversation.envelope import Envelope


class InitiatorConversation(Conversation):
    """
    Parent class must be specialized

    :note: Specializations must implement _create_first_message() and _process_valid_response()
    """
    def __init__(self, com_system, conversation_id, remote_endpoint, *args, **kwargs):
        super().__init__(com_system, *args, **kwargs)
        self.first_envelop = None
        self.conversation_id = conversation_id
        self.remote_endpoint = remote_endpoint

        first_message = self._create_first_message(kwargs)
        self.first_envelope = Envelope(message=first_message, address=self.remote_endpoint)

    def _execute_details(self):
        envelope = self._do_reliable_request(self.first_envelope)

        if not envelope:
            print('no response :(')
        else:
            self._process_valid_response(envelope)

    def _create_first_message(self, kwargs):
        raise NotImplementedError

    def _process_valid_response(self, envelope):
        raise NotImplementedError
