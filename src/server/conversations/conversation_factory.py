from src.communications.conversation.conversation_factory import ConversationFactory
from src.server.conversations.constants import *
from src.server.conversations.block_contact_initiator_conversation import BlockContactInitiatorConversation
from src.server.conversations.declare_contact_responder_conversation import DeclareContactResponderConversation
from src.server.conversations.join_game_responder_conversation import JoinGameResponderConversation
from src.server.conversations.new_game_responder_conversation import NewGameResponderConversation
from src.server.conversations.set_secret_word_responder_conversation import SetSecretWordResponderConversation
from src.server.conversations.submit_guess_responder_conversation import SubmitGuessResponderConversation


class ConversationFactory(ConversationFactory):
    def __init__(self):
        self.CONVERSATION_TYPE_ID_MAP = {
            BLOCK_CONTACT_INITIATOR_CONVERSATION: BlockContactInitiatorConversation,
            DECLARE_CONTACT_RESPONDER_CONVERSATION: DeclareContactResponderConversation,
            JOIN_GAME_RESPONDER_CONVERSATION: JoinGameResponderConversation,
            NEW_GAME_RESPONDER_CONVERSATION: NewGameResponderConversation,
            SET_SECRET_WORD_RESPONDER_CONVERSATION: SetSecretWordResponderConversation,
            SUBMIT_GUESS_RESPONDER_CONVERSATION: SubmitGuessResponderConversation
        }