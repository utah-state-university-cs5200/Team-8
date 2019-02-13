from src.communications.messages.request import Request


class RefreshGameList(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
