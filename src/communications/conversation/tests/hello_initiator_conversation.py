from src.communications.conversation.initiator_conversation import InitiatorConversation
from src.communications.messages.constants import MESSAGE_ID_HELLO
from src.communications.messages.message_factory import MessageFactory
from src.communications.messages.message_exception import MessageException


# Concrete implementation of InitiatorConversation
class HelloConversation(InitiatorConversation):
    def __init__(self, conversation_id, remote_endpoint, *args, **kwargs):
        super().__init__(conversation_id, remote_endpoint, *args, **kwargs)
        self._valid_incoming_message_types = {MESSAGE_ID_HELLO}

    def _create_first_message(self, kwargs):
        try:
            return MessageFactory.build(message_type_id=MESSAGE_ID_HELLO,
                                        conversation_id=self.conversation_id,
                                        message_id=kwargs['message_id'],
                                        sender_id=kwargs['sender_id'],
                                        player_alias=kwargs['player_alias'])
        except KeyError or MessageException:
            return None

    def _process_valid_response(self, envelope):
        # Do stuff after the initial UDP Request Reply returns a valid envelope
        # Ex: do some processing, then send back another message via either udp or tcp
        # Idea: add other messaging protocols to the base conversation class
        self._alive = False
