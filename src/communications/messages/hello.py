from src.communications.messages.request import Request


class Hello(Request):
    type_key = Request.freshTypeDict()
    type_key['player_alias'] = str
    def __init__(self, *args, **kwargs):
        """
        Hello message

        :param args:
        :param kwargs: {message_type_id, player_alias}
        """
        super().__init__(*args, **kwargs)
        self.player_alias = kwargs["player_alias"]
