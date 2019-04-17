import time
import unittest

from src.client.conversations.constants import *
from src.client.conversations.conversation_factory import ConversationFactory

from src.communications.messages.constants import *
from src.communications.messages.message_factory import MessageFactory
from src.communications.conversation.envelope import Envelope
from src.communications.conversation.conversation import PossibleState


class TestClientConversations(unittest.TestCase):
    def setUp(self):
        self.client_conversation_factory = ConversationFactory()

    def tearDown(self):
        pass

    def testClientConversationFactory(self):
        conversation_id = 1111

        remote_endpoint = ('172.0.0.10', 5000)
        conv_1 = self.client_conversation_factory.build(conversation_type_id=CONNECT_TO_LOBBY_INITIATOR_CONVERSATION,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=remote_endpoint,
                                                        message_id=1,
                                                        sender_id=2,
                                                        player_alias='The Best Player Ever')

        self.assertEqual(conv_1.first_envelope.message.message_type_id, MESSAGE_ID_HELLO)
        self.assertEqual(conv_1.first_envelope.message.message_id, 1)
        self.assertEqual(conv_1.first_envelope.message.sender_id, 2)
        self.assertEqual(conv_1.first_envelope.message.player_alias, 'The Best Player Ever')

        remote_endpoint = ('172.0.0.10', 5001)
        conv_2 = self.client_conversation_factory.build(conversation_type_id=DECLARE_CONTACT_INITIATOR_CONVERSATION,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=remote_endpoint,
                                                        message_id=1,
                                                        sender_id=2,
                                                        clue_id=10,
                                                        guess='This is a guess')

        self.assertEqual(conv_2.first_envelope.message.message_type_id, MESSAGE_ID_CONTACT)
        self.assertEqual(conv_2.first_envelope.message.message_id, 1)
        self.assertEqual(conv_2.first_envelope.message.sender_id, 2)
        self.assertEqual(conv_2.first_envelope.message.clue_id, 10)
        self.assertEqual(conv_2.first_envelope.message.guess, 'This is a guess')

        remote_endpoint = ('172.0.0.10', 5002)
        conv_3 = self.client_conversation_factory.build(conversation_type_id=JOIN_GAME_INITIATOR_CONVERSATION,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=remote_endpoint,
                                                        message_id=1,
                                                        sender_id=2,
                                                        game_id=20,
                                                        player_id=999,
                                                        player_alias='The Best Player Ever')

        self.assertEqual(conv_3.first_envelope.message.message_type_id, MESSAGE_ID_JOIN_GAME)
        self.assertEqual(conv_3.first_envelope.message.message_id, 1)
        self.assertEqual(conv_3.first_envelope.message.sender_id, 2)
        self.assertEqual(conv_3.first_envelope.message.game_id, 20)
        self.assertEqual(conv_3.first_envelope.message.player_id, 999)
        self.assertEqual(conv_3.first_envelope.message.player_alias, 'The Best Player Ever')

        remote_endpoint = ('172.0.0.10', 5003)
        conv_4 = self.client_conversation_factory.build(conversation_type_id=NEW_GAME_INITIATOR_CONVERSATION,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=remote_endpoint,
                                                        message_id=1,
                                                        sender_id=2)

        self.assertEqual(conv_4.first_envelope.message.message_type_id, MESSAGE_ID_NEW_GAME)
        self.assertEqual(conv_4.first_envelope.message.message_id, 1)
        self.assertEqual(conv_4.first_envelope.message.sender_id, 2)

        remote_endpoint = ('172.0.0.10', 5004)
        conv_5 = self.client_conversation_factory.build(conversation_type_id=SET_SECRET_WORD_INITIATOR_CONVERSATION,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=remote_endpoint,
                                                        message_id=1,
                                                        sender_id=2,
                                                        player_id=999,
                                                        secret_word='Word')

        self.assertEqual(conv_5.first_envelope.message.message_type_id, MESSAGE_ID_SET_SECRET_WORD)
        self.assertEqual(conv_5.first_envelope.message.message_id, 1)
        self.assertEqual(conv_5.first_envelope.message.sender_id, 2)
        self.assertEqual(conv_5.first_envelope.message.player_id, 999)
        self.assertEqual(conv_5.first_envelope.message.secret_word, 'Word')

        remote_endpoint = ('172.0.0.10', 5005)
        conv_6 = self.client_conversation_factory.build(conversation_type_id=SUBMIT_GUESS_INITIATOR_CONVERSATION,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=remote_endpoint,
                                                        message_id=1,
                                                        sender_id=2,
                                                        player_id=999,
                                                        word='Word',
                                                        clue='Clue')

        self.assertEqual(conv_6.first_envelope.message.message_type_id, MESSAGE_ID_SUBMIT_GUESS)
        self.assertEqual(conv_6.first_envelope.message.message_id, 1)
        self.assertEqual(conv_6.first_envelope.message.sender_id, 2)
        self.assertEqual(conv_6.first_envelope.message.player_id, 999)
        self.assertEqual(conv_6.first_envelope.message.word, 'Word')
        self.assertEqual(conv_6.first_envelope.message.clue, 'Clue')

    def testConnectToLobbyInitiatorConversation(self):
        remote_endpoint = ('172.0.0.10', 5006)
        conv = self.client_conversation_factory.build(conversation_type_id=CONNECT_TO_LOBBY_INITIATOR_CONVERSATION,
                                                      conversation_id=111,
                                                      remote_endpoint=remote_endpoint,
                                                      message_id=1,
                                                      sender_id=2,
                                                      player_alias='The Best Player Ever',
                                                      timeout=.1,
                                                      max_retry=3)

        conv.start()
        time.sleep(.1)
        # Fake an incoming message from the dispatcher
        message = MessageFactory.build(message_type_id=MESSAGE_ID_ASSIGN_ID,
                                       conversation_id=0,
                                       message_id=2,
                                       sender_id=2,
                                       request_id=0,
                                       message_status=1,
                                       player_id=2)
        conv.process(Envelope(message=message, address=('192.0.0.1', 4444)))

        time.sleep(.1)
        # Fake an incoming message from the dispatcher
        message = MessageFactory.build(message_type_id=MESSAGE_ID_GAME_LIST,
                                       conversation_id=0,
                                       message_id=2,
                                       sender_id=2,
                                       request_id=0,
                                       message_status=1,
                                       game_list='a game')
        conv.process(Envelope(message=message, address=('192.0.0.1', 4444)))

        conv.cleanup()
        time.sleep(1)

        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)

    def testDeclareContactInitiatorConversation(self):
        remote_endpoint = ('172.0.0.10', 5007)
        conv = self.client_conversation_factory.build(conversation_type_id=DECLARE_CONTACT_INITIATOR_CONVERSATION,
                                                      conversation_id=111,
                                                      remote_endpoint=remote_endpoint,
                                                      message_id=1,
                                                      sender_id=2,
                                                      clue_id=3,
                                                      guess='A Guess',
                                                      timeout=.1,
                                                      max_retry=3)

        conv.start()

        time.sleep(.1)
        # Fake an incoming message from the dispatcher
        message = MessageFactory.build(message_type_id=MESSAGE_ID_CONTACT_ALERT,
                                       conversation_id=0,
                                       message_id=2,
                                       sender_id=2,
                                       request_id=0,
                                       clue_id=1)
        conv.process(Envelope(message=message, address=('192.0.0.1', 4444)))

        time.sleep(.1)
        conv.cleanup()
        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)

    def testJoinGameInitiatorConversation(self):
        remote_endpoint = ('172.0.0.10', 5008)
        conv = self.client_conversation_factory.build(conversation_type_id=JOIN_GAME_INITIATOR_CONVERSATION,
                                                      conversation_id=111,
                                                      remote_endpoint=remote_endpoint,
                                                      message_id=1,
                                                      sender_id=2,
                                                      game_id=2,
                                                      player_id=3,
                                                      player_alias='An Alias',
                                                      timeout=.1,
                                                      max_retry=3)

        conv.start()

        time.sleep(.1)
        # Fake an incoming message from the dispatcher
        message = MessageFactory.build(message_type_id=MESSAGE_ID_GAME_SERVER_DEF,
                                       conversation_id=0,
                                       message_id=2,
                                       sender_id=2,
                                       request_id=0,
                                       message_status=0,
                                       game_id=1)
        conv.process(Envelope(message=message, address=('192.0.0.1', 4444)))

        time.sleep(.1)
        # Fake an incoming message from the dispatcher
        message = MessageFactory.build(message_type_id=MESSAGE_ID_GAME_STATE,
                                       conversation_id=0,
                                       message_id=2,
                                       sender_id=2,
                                       request_id=0,
                                       message_status=0)
        conv.process(Envelope(message=message, address=('192.0.0.1', 4444)))

        time.sleep(.1)
        conv.cleanup()
        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)

    def testNewGameInitiatorConversation(self):
        remote_endpoint = ('172.0.0.10', 5009)
        conv = self.client_conversation_factory.build(conversation_type_id=NEW_GAME_INITIATOR_CONVERSATION,
                                                      conversation_id=111,
                                                      remote_endpoint=remote_endpoint,
                                                      message_id=1,
                                                      sender_id=2,
                                                      timeout=.1,
                                                      max_retry=3)

        conv.start()

        time.sleep(.1)
        # Fake an incoming message from the dispatcher
        message = MessageFactory.build(message_type_id=MESSAGE_ID_GAME_SERVER_DEF,
                                       conversation_id=0,
                                       message_id=2,
                                       sender_id=2,
                                       request_id=0,
                                       message_status=0,
                                       game_id=1)
        conv.process(Envelope(message=message, address=('192.0.0.1', 4444)))

        time.sleep(.1)
        # Fake an incoming message from the dispatcher
        message = MessageFactory.build(message_type_id=MESSAGE_ID_GAME_STATE,
                                       conversation_id=0,
                                       message_id=2,
                                       sender_id=2,
                                       request_id=0,
                                       message_status=0)
        conv.process(Envelope(message=message, address=('192.0.0.1', 4444)))

        time.sleep(.1)
        conv.cleanup()
        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)

    def testSetSecretWordInitiatorConversation(self):
        remote_endpoint = ('172.0.0.10', 5010)
        conv = self.client_conversation_factory.build(conversation_type_id=SET_SECRET_WORD_INITIATOR_CONVERSATION,
                                                      conversation_id=111,
                                                      remote_endpoint=remote_endpoint,
                                                      message_id=1,
                                                      sender_id=2,
                                                      player_id=1,
                                                      secret_word='It\'s a secret',
                                                      timeout=.1,
                                                      max_retry=3)

        conv.start()

        time.sleep(.1)
        # Fake an incoming message from the dispatcher
        message = MessageFactory.build(message_type_id=MESSAGE_ID_ACK,
                                       conversation_id=0,
                                       message_id=2,
                                       sender_id=2,
                                       request_id=0,
                                       message_status=0)
        conv.process(Envelope(message=message, address=('192.0.0.1', 4444)))

        time.sleep(.1)
        conv.cleanup()
        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)

    def testSubmitGuessInitiatorConversation(self):
        remote_endpoint = ('172.0.0.10', 5011)
        conv = self.client_conversation_factory.build(conversation_type_id=SUBMIT_GUESS_INITIATOR_CONVERSATION,
                                                      conversation_id=111,
                                                      remote_endpoint=remote_endpoint,
                                                      message_id=1,
                                                      sender_id=2,
                                                      word='A word',
                                                      clue='A clue',
                                                      timeout=.1,
                                                      max_retry=3)

        conv.start()

        time.sleep(.2)
        # Fake an incoming message from the dispatcher
        message = MessageFactory.build(message_type_id=MESSAGE_ID_ACK,
                                       conversation_id=0,
                                       message_id=2,
                                       sender_id=2,
                                       request_id=0,
                                       message_status=0)
        conv.process(Envelope(message=message, address=('192.0.0.1', 4444)))

        time.sleep(.1)
        conv.cleanup()
        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)

    def testBlockContactResponderConversation(self):
        message = MessageFactory.build(message_type_id=MESSAGE_ID_CONTACT_ALERT,
                                       conversation_id=0,
                                       message_id=1,
                                       sender_id=2,
                                       clue_id=1)
        message.conversation_id = 1
        envelope = Envelope(message=message, address=('172.0.0.10', 5012))

        conv = self.client_conversation_factory.build(conversation_type_id=BLOCK_CONTACT_RESPONDER_CONVERSATION,
                                                      incoming_envelope=envelope,
                                                      timeout=.1,
                                                      max_retry=3)

        conv.start()

        time.sleep(.1)
        conv.cleanup()
        self.assertEqual(conv._possible_state, PossibleState.SUCCEEDED)