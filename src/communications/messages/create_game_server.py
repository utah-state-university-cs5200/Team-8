from src.communications.messages.request import Request


class CreateGameServer(Request):
    type_key = Request.freshTypeDict()
    def __init__(self, *args, **kwargs):
        """
        Create Game Server message

        :param args:
        :param kwargs: {message_type_id}
        """
        super().__init__(*args, **kwargs)
