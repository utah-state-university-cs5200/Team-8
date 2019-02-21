from src.communications.messages.request import Request


class Hello(Request):
    def __init__(self, *args, **kwargs):
        """
        Hello message

        :param args: [message_type_id, player_alias]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.player_alias = args[1]
