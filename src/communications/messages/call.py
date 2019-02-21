from src.communications.messages.request import Request


class Call(Request):
    def __init__(self, *args, **kwargs):
        """
        Call message

        :param args: [message_type_id]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
