from src.communications.messages.request import Request


class SetSecretWord(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player_id = args[1]
        self.secret_word = args[2]
