from src.communications.conversation.conversation import PossibleState
from src.communications.conversation.initiator_conversation import InitiatorConversation
from src.communications.messages.constants import MESSAGE_ID_CONTACT_ALERT, MESSAGE_ID_BLOCK, MESSAGE_ID_CALL
from src.communications.messages.message_factory import MessageFactory
from src.communications.messages.message_exception import MessageException


# Concrete implementation of InitiatorConversation
class BlockContactInitiatorConversation(InitiatorConversation):
    def __init__(self, conversation_id, remote_endpoint, *args, **kwargs):
        super().__init__(conversation_id, remote_endpoint, *args, **kwargs)
        self._valid_incoming_message_types = {MESSAGE_ID_BLOCK, MESSAGE_ID_CALL}

    def _create_first_message(self, kwargs):
        try:
            return MessageFactory.build(message_type_id=MESSAGE_ID_CONTACT_ALERT,
                                        message_id=kwargs['message_id'],
                                        sender_id=kwargs['sender_id'],
                                        clue_id=kwargs['clue_id'])
        except KeyError or MessageException:
            return None

    def _process_valid_response(self, envelope):
        if envelope and envelope.message.message_type_id == MESSAGE_ID_BLOCK:
            # TODO: process the ContactAlert message
            pass
        else:
            self._possible_state = PossibleState.FAILED

        # TODO: Add other parts of this protocol. See documentation

        self._possible_state = PossibleState.SUCCEEDED
