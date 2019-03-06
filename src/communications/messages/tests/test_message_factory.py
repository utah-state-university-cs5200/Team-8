import unittest
import hypothesis

from src.communications.messages.constants import MESSAGE_ID_HELLO, MESSAGE_ID_SUBMIT_GUESS, MESSAGE_ID_ASSIGN_ID, \
    MESSAGE_STATUS_SUCCESS
from src.communications.messages.message_exception import MessageException
from src.communications.messages.message_factory import MessageFactory

from src.communications.messages import constants

class TestMessageFactory(unittest.TestCase):
    @hypothesis.strategies.composite
    def arbitrary_message_dict(draw):
        output = {}
        return output
        #maybe just use fixed dictionary strategy?
    def testBuildMessageSuccessful(self):
        """
        Test that a valid message is built as expected

        :return:
        """
        id_vals = {'message_id':2, 'conv_id':(2, 1)}
        m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias", **id_vals)
        self.assertEqual(m1.getAttributes()["message_type_id"], MESSAGE_ID_HELLO)
        self.assertEqual(m1.getAttributes()["player_alias"], "Test Alias")

        m2 = MessageFactory.build(message_type_id=MESSAGE_ID_SUBMIT_GUESS, player_id=19, word="foo", clue="bar", **id_vals)
        self.assertEqual(m2.getAttributes()["message_type_id"], MESSAGE_ID_SUBMIT_GUESS)
        self.assertEqual(m2.getAttributes()["player_id"], 19)
        self.assertEqual(m2.getAttributes()["word"], "foo")
        self.assertEqual(m2.getAttributes()["clue"], "bar")

        m3 = MessageFactory.build(message_type_id=MESSAGE_ID_ASSIGN_ID, request_id=4, message_status=MESSAGE_STATUS_SUCCESS, player_id=8, **id_vals)
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


    @hypothesis.given(hypothesis.strategies.data())
    @hypothesis.settings(deadline=None)
    def testReversibilityOfEncoding(self, data):
        st_int = hypothesis.strategies.integers()
        strat_map = {
            int:st_int,
            str:hypothesis.strategies.characters(),
            (int, int):hypothesis.strategies.tuples(st_int, st_int),
            }
        vals = [item for item in dir(constants) if not item.startswith("__")]
        for term in vals:
            if 'SUCCESS' in term:
                continue
            id_val = getattr(constants, term)
            message_class = MessageFactory.MESSAGE_TYPE_ID_MAP[id_val]
            types = message_class.freshTypeDict()
            for argument in types.keys():
                types[argument] = strat_map[types[argument]]
            prop = data.draw(
                hypothesis.strategies.fixed_dictionaries(types)
                )
            prop['message_type_id'] = id_val
            # print(prop)
            message_instance = MessageFactory.build(**prop)
            byte_string = message_instance.encode()
            result_message = MessageFactory.fromByteString(byte_string)
            byte_string2 = result_message.encode()
            self.assertEqual(byte_string, byte_string2)

if __name__ == "__main__":
    unittest.main()
