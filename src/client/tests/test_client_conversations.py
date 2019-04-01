import time
import unittest

from unittest.mock import Mock

from src.client.conversations.constants import *
from src.client.conversations.conversation_factory import ConversationFactory

from src.communications.messages.constants import *
from src.communications.communicator.udp.udp_communicator import UDPCommunicator


class TestClientConversations(unittest.TestCase):
    def setUp(self):
        self.remote_endpoint = ('172.0.0.10', 9999)

        self.mock_client = Mock()
        self.mock_client.alive = True
        self.mock_client.enqueueTask = lambda message: message

        self.client_conversation_factory = ConversationFactory()
        self.client_udp_communicator = UDPCommunicator(dispatcher=self.mock_client)

    def tearDown(self):
        self.client_udp_communicator.cleanup()

    def testClientConversationFactory(self):
        conversation_id = 1111

        conv_1 = self.client_conversation_factory.build(conversation_type_id=CONNECT_TO_LOBBY_INITIATOR_CONVERSATION,
                                                        com_system=self.client_udp_communicator,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=self.remote_endpoint,
                                                        message_id=1,
                                                        sender_id=2,
                                                        player_alias='The Best Player Ever')

        self.assertEqual(conv_1.first_envelope.message.message_type_id, MESSAGE_ID_HELLO)
        self.assertEqual(conv_1.first_envelope.message.message_id, 1)
        self.assertEqual(conv_1.first_envelope.message.sender_id, 2)
        self.assertEqual(conv_1.first_envelope.message.player_alias, 'The Best Player Ever')

        conv_2 = self.client_conversation_factory.build(conversation_type_id=DECLARE_CONTACT_INITIATOR_CONVERSATION,
                                                        com_system=self.client_udp_communicator,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=self.remote_endpoint,
                                                        message_id=1,
                                                        sender_id=2,
                                                        clue_id=10,
                                                        guess='This is a guess')

        self.assertEqual(conv_2.first_envelope.message.message_type_id, MESSAGE_ID_CONTACT)
        self.assertEqual(conv_2.first_envelope.message.message_id, 1)
        self.assertEqual(conv_2.first_envelope.message.sender_id, 2)
        self.assertEqual(conv_2.first_envelope.message.clue_id, 10)
        self.assertEqual(conv_2.first_envelope.message.guess, 'This is a guess')

        conv_3 = self.client_conversation_factory.build(conversation_type_id=JOIN_GAME_INITIATOR_CONVERSATION,
                                                        com_system=self.client_udp_communicator,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=self.remote_endpoint,
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

        conv_4 = self.client_conversation_factory.build(conversation_type_id=NEW_GAME_INITIATOR_CONVERSATION,
                                                        com_system=self.client_udp_communicator,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=self.remote_endpoint,
                                                        message_id=1,
                                                        sender_id=2)

        self.assertEqual(conv_4.first_envelope.message.message_type_id, MESSAGE_ID_NEW_GAME)
        self.assertEqual(conv_4.first_envelope.message.message_id, 1)
        self.assertEqual(conv_4.first_envelope.message.sender_id, 2)

        conv_5 = self.client_conversation_factory.build(conversation_type_id=SET_SECRET_WORD_INITIATOR_CONVERSATION,
                                                        com_system=self.client_udp_communicator,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=self.remote_endpoint,
                                                        message_id=1,
                                                        sender_id=2,
                                                        player_id=999,
                                                        secret_word='Word')

        self.assertEqual(conv_5.first_envelope.message.message_type_id, MESSAGE_ID_SET_SECRET_WORD)
        self.assertEqual(conv_5.first_envelope.message.message_id, 1)
        self.assertEqual(conv_5.first_envelope.message.sender_id, 2)
        self.assertEqual(conv_5.first_envelope.message.player_id, 999)
        self.assertEqual(conv_5.first_envelope.message.secret_word, 'Word')

        conv_6 = self.client_conversation_factory.build(conversation_type_id=SUBMIT_GUESS_INITIATOR_CONVERSATION,
                                                        com_system=self.client_udp_communicator,
                                                        conversation_id=conversation_id,
                                                        remote_endpoint=self.remote_endpoint,
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
        pass

    def testDeclareContactInitiatorConversation(self):
        pass

    def testJoinGameInitiatorConversation(self):
        pass

    def testNewGameInitiatorConversation(self):
        pass

    def testSetSecretWordInitiatorConversation(self):
        pass

    def testSubmitGuessInitiatorConversation(self):
        pass
