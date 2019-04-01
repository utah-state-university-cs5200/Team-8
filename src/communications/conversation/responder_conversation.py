from src.communications.conversation.conversation import Conversation, PossibleState
from src.communications.conversation.envelope import Envelope


class ResponderConversation(Conversation):
    """
    Parent class must be specialized

    :note: Specializations must implement _execute_details()
    """
    def __init__(self, com_system, incoming_envelop, *args, **kwargs):
        super().__init__(com_system, *args, **kwargs)
        self.incoming_envelop = incoming_envelop

        if self.incoming_envelop and self._is_envelope_valid(self.incoming_envelop):
            self.conversation_id = self.incoming_envelop.message.conversation_id
            self.remote_endpoint = self.incoming_envelop.address
        else:
            self._possible_state = PossibleState.FAILED
