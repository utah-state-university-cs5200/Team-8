from src.communications.messages.request import Request


class Contact(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player_id = args[1]
        self.clue_id = args[2]
        self.guess = args[3]
