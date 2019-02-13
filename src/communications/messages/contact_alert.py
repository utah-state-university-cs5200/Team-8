from src.communications.messages.request import Request


class ContactAlert(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clue_id = args[1]
