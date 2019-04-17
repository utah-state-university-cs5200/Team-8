import time
import unittest

from src.server.conversations.constants import *
from src.server.conversations.conversation_factory import ConversationFactory

from src.communications.messages.constants import *
from src.communications.messages.message_factory import MessageFactory
from src.communications.conversation.envelope import Envelope
from src.communications.conversation.conversation import PossibleState


class TestServerConversations(unittest.TestCase):
    def setUp(self):
        self.client_conversation_factory = ConversationFactory()

    def tearDown(self):
        pass

    def testServerConversationFactory(self):
        conversation_id = 1111

        remote_endpoint = ('172.0.0.10', 5000)
        conv_1 = self.client_conversation_factory.build(conversation_type_id=BLOCK_CONTACT_INITIATOR_CONVERSATION,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=remote_endpoint,
                                                        message_id=1,
                                                        sender_id=2,
                                                        clue_id=10)

        self.assertEqual(conv_1.first_envelope.message.message_type_id, MESSAGE_ID_CONTACT_ALERT)
        self.assertEqual(conv_1.first_envelope.message.message_id, 1)
        self.assertEqual(conv_1.first_envelope.message.sender_id, 2)
        self.assertEqual(conv_1.first_envelope.message.clue_id, 10)

        # Test Declare Contact Responder Conversation
        remote_endpoint = ('172.0.0.10', 5001)
        message = MessageFactory.build(message_type_id=MESSAGE_ID_CONTACT,
                                       conversation_id=2,
                                       message_id=4,
                                       sender_id=5,
                                       guess='<something unique>',
                                       clue_id=5,)
        envelope = Envelope(message=message, address=remote_endpoint)

        conv_2 = self.client_conversation_factory.build(conversation_type_id=DECLARE_CONTACT_RESPONDER_CONVERSATION,
                                                        incoming_envelope=envelope)

        self.assertEqual(conv_2.conversation_id, 2)
        self.assertEqual(conv_2.remote_endpoint, remote_endpoint)

        # Test Join Game Responder Conversation
        remote_endpoint = ('172.0.0.10', 5002)
        message = MessageFactory.build(message_type_id=MESSAGE_ID_ADD_PLAYER,
                                       conversation_id=2,
                                       message_id=4,
                                       sender_id=5,
                                       player_alias='I am the Walrus',
                                       player_id=9)
        envelope = Envelope(message=message, address=remote_endpoint)

        conv_2 = self.client_conversation_factory.build(conversation_type_id=JOIN_GAME_RESPONDER_CONVERSATION,
                                                        incoming_envelope=envelope)

        self.assertEqual(conv_2.conversation_id, 2)
        self.assertEqual(conv_2.remote_endpoint, remote_endpoint)

        # Test New Game Responder Conversation
        remote_endpoint = ('172.0.0.10', 5003)
        message = MessageFactory.build(message_type_id=MESSAGE_ID_CREATE_GAME_SERVER,
                                       conversation_id=2,
                                       message_id=4,
                                       sender_id=5)
        envelope = Envelope(message=message, address=remote_endpoint)

        conv_2 = self.client_conversation_factory.build(conversation_type_id=NEW_GAME_RESPONDER_CONVERSATION,
                                                        incoming_envelope=envelope)

        self.assertEqual(conv_2.conversation_id, 2)
        self.assertEqual(conv_2.remote_endpoint, remote_endpoint)

        # Test Set Secret Word Responder Conversation
        remote_endpoint = ('172.0.0.10', 5004)
        message = MessageFactory.build(message_type_id=MESSAGE_ID_SET_SECRET_WORD,
                                       conversation_id=2,
                                       message_id=4,
                                       sender_id=5,
                                       player_id=9,
                                       secret_word='This is a secret')
        envelope = Envelope(message=message, address=remote_endpoint)

        conv_2 = self.client_conversation_factory.build(conversation_type_id=SET_SECRET_WORD_RESPONDER_CONVERSATION,
                                                        incoming_envelope=envelope)

        self.assertEqual(conv_2.conversation_id, 2)
        self.assertEqual(conv_2.remote_endpoint, remote_endpoint)

        # Test Submit Guess Responder Conversation
        remote_endpoint = ('172.0.0.10', 5005)
        message = MessageFactory.build(message_type_id=MESSAGE_ID_SUBMIT_GUESS,
                                       conversation_id=2,
                                       message_id=4,
                                       sender_id=5,
                                       player_id=10,
                                       word='hello',
                                       clue='just another clue')
        envelope = Envelope(message=message, address=remote_endpoint)

        conv_2 = self.client_conversation_factory.build(conversation_type_id=SUBMIT_GUESS_RESPONDER_CONVERSATION,
                                                        incoming_envelope=envelope)

        self.assertEqual(conv_2.conversation_id, 2)
        self.assertEqual(conv_2.remote_endpoint, remote_endpoint)

    def testBlockContactInitiatorConversation(self):
        remote_endpoint = ('172.0.0.10', 5000)
        conv = self.client_conversation_factory.build(conversation_type_id=BLOCK_CONTACT_INITIATOR_CONVERSATION,
                                                      conversation_id=1111,
                                                      remote_endpoint=remote_endpoint,
                                                      message_id=1,
                                                      sender_id=2,
                                                      clue_id=10)
        conv.start()
        time.sleep(.1)

        # TODO: Finish testing by faking incoming messages

        conv.cleanup()
        time.sleep(1)

        self.assertEqual(conv._possible_state, PossibleState.WORKING)

    def testDeclareContactResponderConversation(self):
        remote_endpoint = ('172.0.0.10', 5001)
        message = MessageFactory.build(message_type_id=MESSAGE_ID_CONTACT,
                                       conversation_id=2,
                                       message_id=4,
                                       sender_id=5,
                                       guess='<something unique>',
                                       clue_id=5, )
        envelope = Envelope(message=message, address=remote_endpoint)

        conv = self.client_conversation_factory.build(conversation_type_id=DECLARE_CONTACT_RESPONDER_CONVERSATION,
                                                      incoming_envelope=envelope)
        conv.start()
        time.sleep(.1)

        # TODO: Finish testing by faking incoming messages

        time.sleep(.1)
        conv.cleanup()
        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)

    def testJoinGameResponderConversation(self):
        remote_endpoint = ('172.0.0.10', 5002)
        message = MessageFactory.build(message_type_id=MESSAGE_ID_ADD_PLAYER,
                                       conversation_id=2,
                                       message_id=4,
                                       sender_id=5,
                                       player_alias='I am the Walrus',
                                       player_id=9)
        envelope = Envelope(message=message, address=remote_endpoint)

        conv = self.client_conversation_factory.build(conversation_type_id=JOIN_GAME_RESPONDER_CONVERSATION,
                                                      incoming_envelope=envelope)
        conv.start()
        time.sleep(.1)

        # TODO: Finish testing by faking incoming messages

        time.sleep(.1)
        conv.cleanup()
        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)

    def testNewGameResponderConversation(self):
        remote_endpoint = ('172.0.0.10', 5003)
        message = MessageFactory.build(message_type_id=MESSAGE_ID_CREATE_GAME_SERVER,
                                       conversation_id=2,
                                       message_id=4,
                                       sender_id=5)
        envelope = Envelope(message=message, address=remote_endpoint)

        conv = self.client_conversation_factory.build(conversation_type_id=NEW_GAME_RESPONDER_CONVERSATION,
                                                      incoming_envelope=envelope)
        conv.start()
        time.sleep(.1)

        # TODO: Finish testing by faking incoming messages

        time.sleep(.1)
        conv.cleanup()
        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)

    def testSetSecretWordResponderConversation(self):
        remote_endpoint = ('172.0.0.10', 5004)
        message = MessageFactory.build(message_type_id=MESSAGE_ID_SET_SECRET_WORD,
                                       conversation_id=2,
                                       message_id=4,
                                       sender_id=5,
                                       player_id=9,
                                       secret_word='This is a secret')
        envelope = Envelope(message=message, address=remote_endpoint)

        conv = self.client_conversation_factory.build(conversation_type_id=SET_SECRET_WORD_RESPONDER_CONVERSATION,
                                                      incoming_envelope=envelope)
        conv.start()
        time.sleep(.1)

        # TODO: Finish testing by faking incoming messages

        time.sleep(.1)
        conv.cleanup()
        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)

    def testSubmitGuessResponderConversation(self):
        remote_endpoint = ('172.0.0.10', 5005)
        message = MessageFactory.build(message_type_id=MESSAGE_ID_SUBMIT_GUESS,
                                       conversation_id=2,
                                       message_id=4,
                                       sender_id=5,
                                       player_id=10,
                                       word='hello',
                                       clue='just another clue')
        envelope = Envelope(message=message, address=remote_endpoint)

        conv = self.client_conversation_factory.build(conversation_type_id=SUBMIT_GUESS_RESPONDER_CONVERSATION,
                                                      incoming_envelope=envelope)
        conv.start()
        time.sleep(.2)

        # TODO: Finish testing by faking incoming messages

        time.sleep(.1)
        conv.cleanup()
        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)

