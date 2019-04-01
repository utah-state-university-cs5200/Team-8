from src.communications.conversation.conversation_factory import ConversationFactory
from src.client.conversations.constants import *
from src.client.conversations.connect_to_lobby_initiator_conversation import ConnectToLobbyInitiatorConversation
from src.client.conversations.declare_contact_initiator_conversation import DeclareContactInitiatorConversation
from src.client.conversations.join_game_initiator_conversation import JoinGameInitiatorConversation
from src.client.conversations.new_game_initiator_conversation import NewGameInitiatorConversation
from src.client.conversations.set_secret_word_initiator_conversation import SetSecretWordInitiatorConversation
from src.client.conversations.submit_guess_initiator_conversation import SubmitGuessInitiatorConversation
from src.client.conversations.block_contact_responder_conversation import BlockContactResponderConversation


class ConversationFactory(ConversationFactory):
    def __init__(self):
        self.CONVERSATION_TYPE_ID_MAP = {
            CONNECT_TO_LOBBY_INITIATOR_CONVERSATION: ConnectToLobbyInitiatorConversation,
            DECLARE_CONTACT_INITIATOR_CONVERSATION: DeclareContactInitiatorConversation,
            JOIN_GAME_INITIATOR_CONVERSATION: JoinGameInitiatorConversation,
            NEW_GAME_INITIATOR_CONVERSATION: NewGameInitiatorConversation,
            SET_SECRET_WORD_INITIATOR_CONVERSATION: SetSecretWordInitiatorConversation,
            SUBMIT_GUESS_INITIATOR_CONVERSATION: SubmitGuessInitiatorConversation,
            BLOCK_CONTACT_RESPONDER_CONVERSATION: BlockContactResponderConversation
        }