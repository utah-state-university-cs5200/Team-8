from src.communications.conversation.conversation import Conversation
from src.communications.conversation.envelope import Envelope


# Abstract class
#   you need to implement the following methods
#       _execute_details
#       _create_first_message
class InitiatorConversation(Conversation):
    def __init__(self, conversation_id, remote_endpoint, *args, **kwargs):
        super().__init__(conversation_id, remote_endpoint, *args, **kwargs)
        self.first_envelop = None

        first_message = self._create_first_message(kwargs)
        self.first_envelop = Envelope(message=first_message, address=self.remote_endpoint)

    def _execute_details(self):
        envelope = self._do_reliable_request(self.first_envelop)

        if not envelope:
            print('no response :(')
        else:
            self._process_valid_response(envelope)

    def _create_first_message(self):
        raise NotImplementedError

    def _process_valid_response(self, envelope):
        raise NotImplementedError
