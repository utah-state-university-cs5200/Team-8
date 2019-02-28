from src.communications.messages.request import Request


class AddPlayer(Request):
    type_key = Request.freshTypeDict()

    def __init__(self, *args, **kwargs):
        """
        Add Player message

        :param args:
        :param kwargs: {message_type_id, player_alias, player_id}
        """
        super().__init__(*args, **kwargs)
        self.player_alias = kwargs["player_alias"]
        self.player_id = kwargs["player_id"]
