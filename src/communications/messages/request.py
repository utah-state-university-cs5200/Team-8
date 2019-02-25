from src.communications.messages.message import Message


class Request(Message):
    def __init__(self, *args, **kwargs):
        """
        Parent class for request-style messages

        :param args:
        :param kwargs: {message_type_id}
        """
        super().__init__(*args, **kwargs)
