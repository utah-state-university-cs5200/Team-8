from src.communications.conversation.conversation import PossibleState
from src.communications.conversation.initiator_conversation import InitiatorConversation
from src.communications.messages.constants import MESSAGE_ID_NEW_GAME, MESSAGE_ID_GAME_SERVER_DEF, MESSAGE_ID_GET_GAME_STATE, MESSAGE_ID_GAME_STATE
from src.communications.messages.message_factory import MessageFactory
from src.communications.messages.message_exception import MessageException


# Concrete implementation of InitiatorConversation
class NewGameInitiatorConversation(InitiatorConversation):
    def __init__(self, com_system, conversation_id, remote_endpoint, *args, **kwargs):
        super().__init__(com_system, conversation_id, remote_endpoint, *args, **kwargs)

    def _create_first_message(self, kwargs):
        try:
            return MessageFactory.build(message_type_id=MESSAGE_ID_NEW_GAME)
        except KeyError or MessageException:
            return None

    def _process_valid_response(self, envelope):
        # 1) Validate lobby responded with GameServerDef
        if envelope and envelope.message.message_type_id == MESSAGE_ID_GAME_SERVER_DEF:
            # TODO: process the GameServerDef message
            pass
        else:
            self._possible_state = PossibleState.FAILED

        # 2) Request GetGameState from game server
        # TODO: The endpoint for this message should be the game server not lobby (the endpoint of the conversation)
        game_state_message = MessageFactory.build(message_type_id=MESSAGE_ID_GET_GAME_STATE)
        envelope = self._do_reliable_request(game_state_message)

        # 3) Process game state
        if envelope and envelope.message.message_type_id == MESSAGE_ID_GAME_STATE:
            # TODO: process the GameState message
            pass
        else:
            self._possible_state = PossibleState.FAILED

        self._possible_state = PossibleState.SUCCEEDED
