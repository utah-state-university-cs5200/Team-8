from src.communications.messages.request import Request


class JoinGame(Request):
    def __init__(self, *args, **kwargs):
        """
        Join Game message

        :param args:
        :param kwargs: {message_type_id, game_id, player_id, player_alias}
        """
        super().__init__(*args, **kwargs)
        self.game_id = kwargs["game_id"]
        self.player_id = kwargs["player_id"]
        self.player_alias = kwargs["player_alias"]
