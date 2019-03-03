from src.communications.messages.request import Request


class NewGame(Request):
    def __init__(self, *args, **kwargs):
        """
        New Game message

        :param args:
        :param kwargs: {message_type_id}
        """
        super().__init__(*args, **kwargs)
