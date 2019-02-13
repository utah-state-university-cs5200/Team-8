from src.communications.messages.message import Message


class Request(Message):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
