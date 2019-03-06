from src.communications.messages.request import Request


class LeaveGame(Request):
    type_key = Request.freshTypeDict()
    type_key['player_id'] = int
    def __init__(self, *args, **kwargs):
        """
        Leave Game message

        :param args:
        :param kwargs: {message_type_id, player_id}
        """
        super().__init__(*args, **kwargs)
        self.player_id = kwargs["player_id"]
