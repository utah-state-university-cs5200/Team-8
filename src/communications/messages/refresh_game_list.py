from src.communications.messages.request import Request


class RefreshGameList(Request):
    type_key = Request.freshTypeDict()
    def __init__(self, *args, **kwargs):
        """
        Refresh Game List message

        :param args:
        :param kwargs: {message_type_id}
        """
        super().__init__(*args, **kwargs)
