from src.communications.conversation.conversation import PossibleState
from src.communications.conversation.initiator_conversation import InitiatorConversation
from src.communications.messages.constants import MESSAGE_ID_SET_SECRET_WORD, MESSAGE_ID_ACK
from src.communications.messages.message_factory import MessageFactory
from src.communications.messages.message_exception import MessageException


# Concrete implementation of InitiatorConversation
class SetSecretWordInitiatorConversation(InitiatorConversation):
    def __init__(self, com_system, conversation_id, remote_endpoint, *args, **kwargs):
        super().__init__(com_system, conversation_id, remote_endpoint, *args, **kwargs)

    def _create_first_message(self, kwargs):
        try:
            return MessageFactory.build(message_type_id=MESSAGE_ID_SET_SECRET_WORD,
                                        message_id=kwargs['message_id'],
                                        sender_id=kwargs['sender_id'],
                                        player_id=kwargs['player_id'],
                                        secret_word=kwargs['secret_word'])
        except KeyError or MessageException:
            return None

    def _process_valid_response(self, envelope):
        # 1) Validate game server responded with Ack
        if envelope and envelope.message.message_type_id == MESSAGE_ID_ACK:
            # TODO: process the Ack message
            pass
        else:
            self._possible_state = PossibleState.FAILED

        self._possible_state = PossibleState.SUCCEEDED
