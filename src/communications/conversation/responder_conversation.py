from src.communications.conversation.conversation import Conversation, PossibleState
from src.communications.conversation.envelope import Envelope


class ResponderConversation(Conversation):
    """
    Parent class must be specialized

    :note: Specializations must implement _execute_details()
    """
    def __init__(self, incoming_envelope, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.incoming_envelope = incoming_envelope

        if self.incoming_envelope and self._is_envelope_valid(self.incoming_envelope):
            self.conversation_id = self.incoming_envelope.message.conversation_id
            self.remote_endpoint = self.incoming_envelope.address
        else:
            self._possible_state = PossibleState.FAILED
