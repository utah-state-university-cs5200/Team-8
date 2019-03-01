from copy import copy
from src.communications.messages.encoder_decoder import encoding

class Message:
    type_key = {'message_type_id': int}
    def __init__(self, *args, **kwargs):
        """
        Parent message class for both request and reply messages

        :param args:
        :param kwargs: {message_type_id}
        """
        self.message_type_id = kwargs["message_type_id"]

    def getAttributes(self):
        return vars(self)

    @classmethod
    def freshTypeDict(self):
        return copy(self.type_key)

    def encode(self):
        print('trying to encode')
        return encoding(vars(self))
