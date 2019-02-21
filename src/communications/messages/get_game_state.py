from src.communications.messages.request import Request


class GetGameState(Request):
    def __init__(self, *args, **kwargs):
        """
        Get Game State message

        :param args: [message_type_id]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
