from src.communications.messages.request import Request


class RefreshGameList(Request):
    def __init__(self, *args, **kwargs):
        """
        Refresh Game List message

        :param args:
        :param kwargs: {message_type_id}
        """
        super().__init__(*args, **kwargs)
