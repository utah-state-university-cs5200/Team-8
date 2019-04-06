from src.communications.messages.constants import MESSAGE_ID_JOIN_GAME, MESSAGE_ID_CONTACT, MESSAGE_ID_NEW_GAME, \
    MESSAGE_ID_SET_SECRET_WORD, MESSAGE_ID_HELLO, MESSAGE_ID_SUBMIT_GUESS
from src.client.conversations.constants import JOIN_GAME_INITIATOR_CONVERSATION, \
    CONNECT_TO_LOBBY_INITIATOR_CONVERSATION, DECLARE_CONTACT_INITIATOR_CONVERSATION, NEW_GAME_INITIATOR_CONVERSATION, \
    SET_SECRET_WORD_INITIATOR_CONVERSATION, SUBMIT_GUESS_INITIATOR_CONVERSATION
from src.communications.messages.encoder_decoder import decode


MESSAGE_CONVERSATION_TYPE_ID_MAP = {
    MESSAGE_ID_JOIN_GAME: JOIN_GAME_INITIATOR_CONVERSATION,
    MESSAGE_ID_HELLO: CONNECT_TO_LOBBY_INITIATOR_CONVERSATION,
    MESSAGE_ID_CONTACT: DECLARE_CONTACT_INITIATOR_CONVERSATION,
    MESSAGE_ID_NEW_GAME: NEW_GAME_INITIATOR_CONVERSATION,
    MESSAGE_ID_SET_SECRET_WORD: SET_SECRET_WORD_INITIATOR_CONVERSATION,
    MESSAGE_ID_SUBMIT_GUESS: SUBMIT_GUESS_INITIATOR_CONVERSATION,
}


class DispatchException(Exception):
    pass


class Dispatcher:
    def __init__(self, conversation_dict, conversation_factory):
        self.conversation_dict = conversation_dict
        self.conversation_factory = conversation_factory

    def process(self, envelope):
        """
        Pass the envelope to the corresponding conversation, or create a new conversation

        :param envelope:
        :raises: DispatchException if conversation_type_id lookup fails
        """
        conversation = self.conversation_dict.get(envelope.message.conversation_id)
        if conversation is None:
            message = decode(envelope.message)
            conversation_type_id = self._lookupConversationTypeID(message.message_type_id)
            conversation = self.conversation_factory.build(remote_endpoint=envelope.address,
                                                           conversation_type_id=conversation_type_id,
                                                           **message.getAttributes())

        conversation.process(envelope)

    def _lookupConversationTypeID(self, message_type_id):
        try:
            return MESSAGE_CONVERSATION_TYPE_ID_MAP[message_type_id]
        except KeyError:
            raise DispatchException("Error: Could not determine conversation_type_id for message_type {}".format(message_type_id))

