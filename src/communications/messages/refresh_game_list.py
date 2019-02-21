from src.communications.messages.request import Request


class RefreshGameList(Request):
    def __init__(self, *args, **kwargs):
        """
        Refresh Game List message

        :param args: [message_type_id]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
