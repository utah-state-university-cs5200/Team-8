from src.communications.messages.request import Request


class SubmitGuess(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player_id = args[1]
        self.word = args[2]
        self.clue = args[3]
