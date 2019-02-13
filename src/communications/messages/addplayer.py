from src.communications.messages.request import Request


class AddPlayer(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player_alias = args[1]
        self.player_id = args[2]
