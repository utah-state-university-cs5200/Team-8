import unittest
from message import Message

class ReversibleEncodingTest(unittest.TestCase):
    def test_from_decoding_has_same_payload(self):
        local_message = Message(1,[4,'sounds like lickin\'', 'chicken'])
        recieved_message = Message.from_decoding(local_message.encode())
        self.assertEqual(
            local_message.payload,
            recieved_message.payload
            )

if __name__=='__main__':
    unittest.main()
