from src.communications.conversation.constants import *
from src.communications.conversation.conversation_exception import ConversationException
from src.communications.conversation.hello_initiator_conversation import HelloConversation


class ConversationFactory:
    def __init__(self):
        self.CONVERSATION_TYPE_ID_MAP = {
                HELLO_INITIATOR_CONVERSATION : HelloConversation
            }

    def build(self, *args, **kwargs):
        try:
            conversation = self.CONVERSATION_TYPE_ID_MAP[kwargs["conversation_type_id"]](*args, **kwargs)
        except KeyError:
            raise ConversationException("Error: ConversationFactory missing a required argument for conversation creation")
        return conversation