from src.communications.conversation.conversation import PossibleState
from src.communications.conversation.initiator_conversation import InitiatorConversation
from src.communications.messages.constants import MESSAGE_ID_HELLO, MESSAGE_ID_ASSIGN_ID, MESSAGE_ID_GAME_LIST, MESSAGE_ID_REFRESH_GAME_LIST
from src.communications.messages.message_factory import MessageFactory
from src.communications.messages.message_exception import MessageException


# Concrete implementation of InitiatorConversation
from src.processors.worker import JOB_CLIENT_ASSIGN_ID


class ConnectToLobbyInitiatorConversation(InitiatorConversation):
    def __init__(self, conversation_id, remote_endpoint, *args, **kwargs):
        super().__init__(conversation_id, remote_endpoint, *args, **kwargs)
        self._valid_incoming_message_types = {MESSAGE_ID_ASSIGN_ID, MESSAGE_ID_GAME_LIST}

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
        # 1) Validate game server responded with AssignID
        if envelope and envelope.message.message_type_id == MESSAGE_ID_ASSIGN_ID:
            if self.worker:
                job = self.createJob(JOB_CLIENT_ASSIGN_ID, envelope.message.player_id)
                self.worker.process(job)
        else:
            self._possible_state = PossibleState.FAILED

        envelope = self._wait_for_response()
        if envelope and envelope.message.message_type_id == MESSAGE_ID_GAME_LIST:
            # TODO: process the GameList message
            pass
        else:
            self._possible_state = PossibleState.FAILED

        while self.is_alive():
            refresh_game_list_message = MessageFactory.build(message_type_id=MESSAGE_ID_REFRESH_GAME_LIST,
                                                             conversation_id=self.conversation_id,
                                                             message_id=1,
                                                             sender_id=1)
            envelope = self._do_reliable_request(refresh_game_list_message)

            if envelope and envelope.message.message_type_id == MESSAGE_ID_GAME_LIST:
                # TODO: process the GameList message
                pass
            # else:
            #     self._possible_state = PossibleState.FAILED

        self._possible_state = PossibleState.SUCCEEDED
