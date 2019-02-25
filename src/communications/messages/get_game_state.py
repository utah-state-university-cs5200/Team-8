from src.communications.messages.request import Request


class GetGameState(Request):
    def __init__(self, *args, **kwargs):
        """
        Get Game State message

        :param args:
        :param kwargs: {message_type_id}
        """
        super().__init__(*args, **kwargs)
