from src.communications.messages.message import Message


class Reply(Message):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request_id = args[1]
        self.status = args[2]
