from src.communications.messages.request import Request


class JoinGame(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_id = args[1]
        self.player_id = args[2]
        self.player_alias = args[3]
