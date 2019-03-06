from src.communications.messages.reply import Reply


class Error(Reply):
    type_key = Reply.freshTypeDict()
    type_key['error_string'] = str
    def __init__(self, *args, **kwargs):
        """
        Error message

        :param args:
        :param kwargs: {message_type_id, request_id, message_status, error_string}
        """
        super().__init__(*args, **kwargs)
        self.error_string = kwargs["error_string"]
