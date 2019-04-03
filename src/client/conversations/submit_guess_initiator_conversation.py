from src.communications.conversation.conversation import PossibleState
from src.communications.conversation.initiator_conversation import InitiatorConversation
from src.communications.messages.constants import MESSAGE_ID_SUBMIT_GUESS, MESSAGE_ID_ACK
from src.communications.messages.message_factory import MessageFactory
from src.communications.messages.message_exception import MessageException


# Concrete implementation of InitiatorConversation
class SubmitGuessInitiatorConversation(InitiatorConversation):
    def __init__(self, conversation_id, remote_endpoint, *args, **kwargs):
        super().__init__(conversation_id, remote_endpoint, *args, **kwargs)
        self._valid_incoming_message_types = {MESSAGE_ID_ACK}

    def _create_first_message(self, kwargs):
        try:
            return MessageFactory.build(message_type_id=MESSAGE_ID_SUBMIT_GUESS,
                                        message_id=kwargs['message_id'],
                                        sender_id=kwargs['sender_id'],
                                        player_id=kwargs['player_id'],
                                        word=kwargs['word'],
                                        clue=kwargs['clue'])
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
