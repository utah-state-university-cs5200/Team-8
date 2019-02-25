from src.communications.messages.message import Message


class Reply(Message):
    def __init__(self, *args, **kwargs):
        """
        Parent class for reply-style messages

        :param args:
        :param kwargs: {message_type_id, request_id, message_status}
        """
        super().__init__(*args, **kwargs)
        self.request_id = kwargs["request_id"]
        self.message_status = kwargs["message_status"]
