from src.client.client import Client
from src.contact.player import Player
from src.communications.conversation.constants import *


class PlayerClient(Client):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.player = Player()
        # TODO:

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
        submit_word_conversation = self.conversation_factory.build(
            conversation_type_id=KEEPER_WORD_SUBMIT,
            conversation_id=self.getNextConversationID(),
            remote_endpoint=self.serverUDPAddress,
            player_id=self.player.id,
            new_word=word
        )
        submit_word_conversation.start()
        self.conversation_dict.add(submit_word_conversation)

    def keeper_block(self, contact_id):
        """Secret keeper blocks on a contact"""
        keeper_block_conversation = self.conversation_factory.build(
            conversation_type_id=KEEPER_BLOCK,
            conversation_id=self.getNextConversationID(),
            remote_endpoint=self.serverUDPAddress,
            player_id=self.player.id,
            contact_id=contact_id
        )
        keeper_block_conversation.start()
        self.conversation_dict.add(keeper_block_conversation)

    def keeper_call(self, contact_id):
        """Secret keeper calls on a contact"""
        keeper_call_conversation = self.conversation_factory.build(
            conversation_type_id=KEEPER_CALL,
            conversation_id=self.getNextConversationID(),
            remote_endpoint=self.serverUDPAddress,
            player_id=self.player.id,
            contact_id=contact_id
        )
        keeper_call_conversation.start()
        self.conversation_dict.add(keeper_call_conversation)

    def give_clue(self, clue):
        """A player submits a clue for the word"""
        give_clue_conversation = self.conversation_factory.build(
            conversation_type_id=GIVE_CLUE,
            conversation_id=self.getNextConversationID(),
            remote_endpoint=self.serverUDPAddress,
            player_id=self.player.id,
            new_clue=clue
        )
        give_clue_conversation.start()
        self.conversation_dict.add(give_clue_conversation)

    def initiate_contact(self, clue_id, guess_word):
        """A player initiates contact on a clue"""
        initiate_contact_conversation = self.conversation_factory.build(
            conversation_type_id=GIVE_CLUE,
            conversation_id=self.getNextConversationID(),
            remote_endpoint=self.serverUDPAddress,
            player_id=self.player.id,
            clue_id=clue_id,
            guess_word=guess_word
        )
        initiate_contact_conversation.start()
        self.conversation_dict.add(initiate_contact_conversation)

    def update_client(self):
        """Updates all data/fields on the client"""
        pass
