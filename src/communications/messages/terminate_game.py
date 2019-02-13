from src.communications.messages.request import Request


class TerminateGame(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_id = args[1]
