from src.communications.messages.reply import Reply


class Error(Reply):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_string = args[3]
