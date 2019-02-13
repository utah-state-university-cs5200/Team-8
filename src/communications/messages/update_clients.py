from src.communications.messages.request import Request


class UpdateClients(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
