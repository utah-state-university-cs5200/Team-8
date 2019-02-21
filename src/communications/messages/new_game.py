from src.communications.messages.request import Request


class NewGame(Request):
    def __init__(self, *args, **kwargs):
        """
        New Game message

        :param args: [message_type_id]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
