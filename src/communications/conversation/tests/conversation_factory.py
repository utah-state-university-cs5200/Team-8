from src.communications.conversation.tests.constants import *
from src.communications.conversation.conversation_factory import ConversationFactory
from src.communications.conversation.tests.hello_initiator_conversation import HelloConversation


class ConversationFactory(ConversationFactory):
    def __init__(self):
        self.CONVERSATION_TYPE_ID_MAP = {
                HELLO_INITIATOR_CONVERSATION : HelloConversation
            }