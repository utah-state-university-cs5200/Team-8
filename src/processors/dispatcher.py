from src.communications.messages.encoder_decoder import decode


MESSAGE_CONVERSATION_TYPE_ID_MAP = {
    
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

