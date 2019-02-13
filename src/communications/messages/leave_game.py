from src.communications.messages.request import Request


class LeaveGame(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player_id = args[1]
