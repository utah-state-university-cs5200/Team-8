import unittest
import hypothesis

from src.communications.messages.constants import MESSAGE_ID_HELLO, MESSAGE_ID_SUBMIT_GUESS, MESSAGE_ID_ASSIGN_ID, \
    MESSAGE_STATUS_SUCCESS
from src.communications.messages.message_exception import MessageException
from src.communications.messages.message_factory import MessageFactory

from src.communications.messages import constants

class TestMessageFactory(unittest.TestCase):
    def testBuildMessageSuccessful(self):
        """
        Test that a valid message is built as expected

        :return:
        """
        m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias")
        self.assertEqual(m1.getAttributes()["message_type_id"], MESSAGE_ID_HELLO)
        self.assertEqual(m1.getAttributes()["player_alias"], "Test Alias")

        m2 = MessageFactory.build(message_type_id=MESSAGE_ID_SUBMIT_GUESS, player_id=19, word="foo", clue="bar")
        self.assertEqual(m2.getAttributes()["message_type_id"], MESSAGE_ID_SUBMIT_GUESS)
        self.assertEqual(m2.getAttributes()["player_id"], 19)
        self.assertEqual(m2.getAttributes()["word"], "foo")
        self.assertEqual(m2.getAttributes()["clue"], "bar")

        m3 = MessageFactory.build(message_type_id=MESSAGE_ID_ASSIGN_ID, request_id=4, message_status=MESSAGE_STATUS_SUCCESS, player_id=8)
        self.assertEqual(m3.getAttributes()["message_type_id"], MESSAGE_ID_ASSIGN_ID)
        self.assertEqual(m3.getAttributes()["request_id"], 4)
        self.assertEqual(m3.getAttributes()["message_status"], MESSAGE_STATUS_SUCCESS)
        self.assertEqual(m3.getAttributes()["player_id"], 8)

    def testBuildMessageUnsuccessful(self):
        """
        Test that an invalid message raises an exception and is not built, as expected

        :return:
        """
        self.assertRaises(MessageException, MessageFactory.build)

        self.assertRaises(MessageException, MessageFactory.build, message_type_id=MESSAGE_ID_HELLO)

        self.assertRaises(MessageException, MessageFactory.build, message_type_id=MESSAGE_ID_SUBMIT_GUESS, player_id=9, clue="bar")

    def testReversibilityOfEncoding(self):
        vals = [item for item in dir(constants) if not item.startswith("__")]
        for term in vals:
            if 'SUCCESS' in term:
                continue
            id_val = getattr(constants, term)
            message = MessageFactory.MESSAGE_TYPE_ID_MAP[id_val]
            print(message)
            print(dir(message))
        self.assertEqual(0,1)

if __name__ == "__main__":
    unittest.main()
