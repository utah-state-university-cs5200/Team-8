from src.communications.messages.request import Request


class Block(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word = args[1]
