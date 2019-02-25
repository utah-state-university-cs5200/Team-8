from src.communications.messages.ack import Ack
from src.communications.messages.addplayer import AddPlayer
from src.communications.messages.assign_id import AssignID
from src.communications.messages.block import Block
from src.communications.messages.call import Call
from src.communications.messages.constants import *
from src.communications.messages.contact import Contact
from src.communications.messages.contact_alert import ContactAlert
from src.communications.messages.create_game_server import CreateGameServer
from src.communications.messages.error import Error
from src.communications.messages.game_list import GameList
from src.communications.messages.game_server_def import GameServerDef
from src.communications.messages.game_state import GameState
from src.communications.messages.get_game_state import GetGameState
from src.communications.messages.hello import Hello
from src.communications.messages.join_game import JoinGame
from src.communications.messages.leave_game import LeaveGame
from src.communications.messages.message_exception import MessageException
from src.communications.messages.new_game import NewGame
from src.communications.messages.refresh_game_list import RefreshGameList
from src.communications.messages.set_secret_word import SetSecretWord
from src.communications.messages.submit_guess import SubmitGuess
from src.communications.messages.terminate_game import TerminateGame
from src.communications.messages.update_clients import UpdateClients


class MessageFactory:
    MESSAGE_TYPE_ID_MAP = {
        MESSAGE_ID_ACK: Ack,
        MESSAGE_ID_ADD_PLAYER: AddPlayer,
        MESSAGE_ID_ASSIGN_ID: AssignID,
        MESSAGE_ID_BLOCK: Block,
        MESSAGE_ID_CALL: Call,
        MESSAGE_ID_CONTACT: Contact,
        MESSAGE_ID_CONTACT_ALERT: ContactAlert,
        MESSAGE_ID_CREATE_GAME_SERVER: CreateGameServer,
        MESSAGE_ID_ERROR: Error,
        MESSAGE_ID_GAME_LIST: GameList,
        MESSAGE_ID_GAME_SERVER_DEF: GameServerDef,
        MESSAGE_ID_GAME_STATE: GameState,
        MESSAGE_ID_GET_GAME_STATE: GetGameState,
        MESSAGE_ID_HELLO: Hello,
        MESSAGE_ID_JOIN_GAME: JoinGame,
        MESSAGE_ID_LEAVE_GAME: LeaveGame,
        MESSAGE_ID_NEW_GAME: NewGame,
        MESSAGE_ID_REFRESH_GAME_LIST: RefreshGameList,
        MESSAGE_ID_SET_SECRET_WORD: SetSecretWord,
        MESSAGE_ID_SUBMIT_GUESS: SubmitGuess,
        MESSAGE_ID_TERMINATE_GAME: TerminateGame,
        MESSAGE_ID_UPDATE_CLIENTS: UpdateClients
    }

    @staticmethod
    def build(*args, **kwargs):
        """
        Creates and returns a message object according to the input parameters
        :param args: Arguments for message creation, starting with message_id
        :param kwargs:
        :return: Message object
        :raises MessageException: if message cannot be built properly
        """
        if len(args) < 1:
            raise MessageException("Error: MessageFactory not enough arguments for message creation")
        message = MessageFactory.MESSAGE_TYPE_ID_MAP[kwargs["message_type_id"]](*args, **kwargs)
        return message
