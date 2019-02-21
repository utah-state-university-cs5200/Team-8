from src.communications.messages.reply import Reply


class Error(Reply):
    def __init__(self, *args, **kwargs):
        """
        Error message

        :param args: [message_type_id, request_id, status, error_string]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.error_string = args[3]
