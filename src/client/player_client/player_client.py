from src.client.client import Client
from src.contact.player import Player
from src.communications.conversation.constants import *


class PlayerClient(Client):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.player = Player()

    def hello(self):
        hello_conversation = self.conversation_factory.build(
            conversation_type_id=HELLO_INITIATOR_CONVERSATION,
            conversation_id=self.getNextConversationID(),
            remote_endpoint=self.serverUDPAddress,
            player_alias=self.player.alias
            )
        hello_conversation.start()
        self.conversation_dict.add(hello_conversation)

    def keeper_submit_word(self, word):
        """Secret keeper submits a new word"""
        pass

    def keeper_block(self):
        """Secret keeper blocks on a contact"""
        pass

    def keeper_call(self):
        """Secret keeper calls on a contact"""
        pass

    def give_clue(self, clue):
        """A player submits a clue for the word"""
        pass

    def initiate_contact(self):
        """A player initiates contact on a clue"""
        pass

    def update_client(self):
        """Updates all data/fields on the client"""
        pass
