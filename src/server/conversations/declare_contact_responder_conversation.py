from src.communications.conversation.conversation import PossibleState
from src.communications.conversation.responder_conversation import ResponderConversation
from src.communications.messages.constants import MESSAGE_ID_CONTACT
from src.communications.messages.message_factory import MessageFactory
from src.communications.messages.message_exception import MessageException


# Concrete implementation of InitiatorConversation
class DeclareContactResponderConversation(ResponderConversation):
    def __init__(self, incoming_envelope, *args, **kwargs):
        super().__init__(incoming_envelope, *args, **kwargs)
        self._valid_incoming_message_types = {MESSAGE_ID_CONTACT}

    def _execute_details(self):
        if self.incoming_envelope and self.incoming_envelope.message.message_type_id == MESSAGE_ID_CONTACT:
            # TODO: process the ContactAlert message
            pass
        else:
            self._possible_state = PossibleState.FAILED

        # TODO: Add other parts of this protocol. See documentation

        self._possible_state = PossibleState.SUCCEEDED