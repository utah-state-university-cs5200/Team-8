from src.communications.messages.request import Request


class Call(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
