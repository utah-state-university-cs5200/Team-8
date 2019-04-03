from src.communications.conversation.conversation import PossibleState
from src.communications.conversation.initiator_conversation import InitiatorConversation
from src.communications.messages.constants import MESSAGE_ID_CONTACT, MESSAGE_ID_CONTACT_ALERT
from src.communications.messages.message_factory import MessageFactory
from src.communications.messages.message_exception import MessageException


# Concrete implementation of InitiatorConversation
class DeclareContactInitiatorConversation(InitiatorConversation):
    def __init__(self, conversation_id, remote_endpoint, *args, **kwargs):
        super().__init__(conversation_id, remote_endpoint, *args, **kwargs)
        self._valid_incoming_message_types = {MESSAGE_ID_CONTACT_ALERT}

    def _create_first_message(self, kwargs):
        try:
            return MessageFactory.build(message_type_id=MESSAGE_ID_CONTACT,
                                        message_id=kwargs['message_id'],
                                        sender_id=kwargs['sender_id'],
                                        clue_id=kwargs['clue_id'],
                                        guess=kwargs['guess'])
        except KeyError or MessageException:
            return None

    def _process_valid_response(self, envelope):
        # 1) Validate game server responded with AnnounceContact
        if envelope and envelope.message.message_type_id == MESSAGE_ID_CONTACT_ALERT:
            # TODO: process the AnnounceContact message
            pass
        else:
            self._possible_state = PossibleState.FAILED

        # TODO: See the conversation documentation for the remaining requirements

        self._possible_state = PossibleState.SUCCEEDED
