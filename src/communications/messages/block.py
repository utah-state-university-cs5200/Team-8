from src.communications.messages.request import Request


class Block(Request):
    def __init__(self, *args, **kwargs):
        """
        Block message

        :param args: [message_type_id, word]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.word = args[1]
