from src.communications.messages.request import Request


class Call(Request):
    def __init__(self, *args, **kwargs):
        """
        Call message

        :param args:
        :param kwargs: {message_type_id}
        """
        super().__init__(*args, **kwargs)
