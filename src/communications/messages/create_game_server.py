from src.communications.messages.request import Request


class CreateGameServer(Request):
    def __init__(self, *args, **kwargs):
        """
        Create Game Server message

        :param args:
        :param kwargs: {message_type_id}
        """
        super().__init__(*args, **kwargs)
