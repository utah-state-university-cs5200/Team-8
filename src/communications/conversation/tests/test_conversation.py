import time
import unittest

from src.communications.conversation.envelope import Envelope
from src.communications.conversation.conversation_dictionary import ConversationDictionary
from src.communications.conversation.tests.constants import *
from src.communications.conversation.tests.conversation_factory import ConversationFactory
from src.communications.messages.constants import MESSAGE_ID_HELLO
from src.communications.messages.message_factory import MessageFactory


class TestConversation(unittest.TestCase):
    def setUp(self):
        self.client_conversation_factory = ConversationFactory()

    def tearDown(self):
        pass

    def testConversationFactory(self):
        conversation_id = 1111
        timeout = 1
        max_retry = 5

        remote_endpoint = ('172.0.0.10', 6000)
        hello_initiator_conversation = self.client_conversation_factory.build(conversation_type_id=HELLO_INITIATOR_CONVERSATION,
                                                                              conversation_id=conversation_id,
                                                                              remote_endpoint=remote_endpoint,
                                                                              player_alias="my alias",
                                                                              message_id=1,
                                                                              sender_id=2,
                                                                              timeout=timeout,
                                                                              max_retry=max_retry)

        hello_initiator_conversation.start()
        time.sleep(1)
        # Fake an incoming message from the dispatcher
        message = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO,
                                       conversation_id=0,
                                       message_id=1,
                                       sender_id=2,
                                       player_alias="my alias")
        hello_initiator_conversation.process(Envelope(message=message, address=('192.0.0.1', 4444)))

        self.assertEqual(hello_initiator_conversation.conversation_id, conversation_id)
        self.assertEqual(hello_initiator_conversation.remote_endpoint, remote_endpoint)
        self.assertEqual(hello_initiator_conversation.timeout, timeout)
        self.assertEqual(hello_initiator_conversation.max_retry, max_retry)

        hello_initiator_conversation.cleanup()

    def testConversationDictionary(self):
        class TestConv:
            def __init__(self, conversation_id):
                self.alive = True
                self.conversation_id = conversation_id

            def is_alive(self):
                return self.alive

        conversation_dict = ConversationDictionary()

        conv1 = TestConv(1)
        conv2 = TestConv(2)
        conv3 = TestConv(3)
        conv4 = TestConv(4)
        conv5 = TestConv(5)
        conv6 = TestConv(6)

        conversation_dict.add(conv1)
        conversation_dict.add(conv2)
        conversation_dict.add(conv3)
        conversation_dict.add(conv4)
        conversation_dict.add(conv5)
        conversation_dict.add(conv6)

        self.assertEqual(conversation_dict.get(1), conv1)
        self.assertEqual(conversation_dict.get(2), conv2)
        self.assertEqual(conversation_dict.get(3), conv3)
        self.assertEqual(conversation_dict.get(4), conv4)
        self.assertEqual(conversation_dict.get(5), conv5)
        self.assertEqual(conversation_dict.get(6), conv6)
        self.assertEqual(conversation_dict.get(7), None)

        conv2.alive = False
        conv4.alive = False
        conv6.alive = False

        time.sleep(2)

        self.assertEqual(conversation_dict.get(1), conv1)
        self.assertEqual(conversation_dict.get(2), None)
        self.assertEqual(conversation_dict.get(3), conv3)
        self.assertEqual(conversation_dict.get(4), None)
        self.assertEqual(conversation_dict.get(5), conv5)
        self.assertEqual(conversation_dict.get(6), None)
        self.assertEqual(conversation_dict.get(7), None)

        conversation_dict.cleanup()

    def testConversationWithDictionary(self):
        conversation_id = 6666
        timeout = 1

        conversation_dict = ConversationDictionary()

        remote_endpoint = ('172.0.0.10', 6001)
        hello_initiator_conversation = self.client_conversation_factory.build(
            conversation_type_id=HELLO_INITIATOR_CONVERSATION,
            conversation_id=conversation_id,
            remote_endpoint=remote_endpoint,
            player_alias="my alias",
            timeout=timeout)
        hello_initiator_conversation.start()

        conversation_dict.add(hello_initiator_conversation)

        self.assertEqual(conversation_dict.get(hello_initiator_conversation.conversation_id), hello_initiator_conversation)

        time.sleep(1)
        # Fake an incoming message from the dispatcher
        message = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO,
                                       conversation_id=0,
                                       message_id=1,
                                       sender_id=2,
                                       player_alias="my alias")
        hello_initiator_conversation.process(Envelope(message=message, address=('192.0.0.1', 4445)))

        time.sleep(5)

        self.assertEqual(conversation_dict.get(hello_initiator_conversation.conversation_id), None)

        conversation_dict.cleanup()
