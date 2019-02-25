from src.communications.messages.request import Request


class TerminateGame(Request):
    def __init__(self, *args, **kwargs):
        """
        Terminate Game message

        :param args:
        :param kwargs: {message_type_id, game_id}
        """
        super().__init__(*args, **kwargs)
        self.game_id = kwargs["game_id"]
