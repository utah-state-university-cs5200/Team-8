from src.communications.conversation.conversation_exception import ConversationException


class ConversationFactory:
    def __init__(self):
        self.CONVERSATION_TYPE_ID_MAP = {}

    def build(self, *args, **kwargs):
        try:
            conversation = self.CONVERSATION_TYPE_ID_MAP[kwargs["conversation_type_id"]](*args, **kwargs)
        except KeyError:
            raise ConversationException("Error: ConversationFactory missing a required argument for conversation creation")
        return conversation
