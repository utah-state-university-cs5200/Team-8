from copy import copy

class Message:
    type_key = {'message_type_id': int}
    type_key['message_id'] = int
    type_key['sender_id'] = int
    def __init__(self, *args, **kwargs):
        """
        Parent message class for both request and reply messages

        :param args:
        :param kwargs: {message_type_id}
        """
        self.message_type_id = kwargs["message_type_id"]
        self.message_id = kwargs["message_id"]
        self.sender_id = kwargs["sender_id"]

    def getAttributes(self):
        return vars(self)

    def unique_message_id(self):
        return (self.message_type_id, self.sender_id, self.message_id)

    @classmethod
    def freshTypeDict(self):
        return copy(self.type_key)
