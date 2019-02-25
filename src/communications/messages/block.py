from src.communications.messages.request import Request


class Block(Request):
    def __init__(self, *args, **kwargs):
        """
        Block message

        :param args:
        :param kwargs: {message_type_id, word}
        """
        super().__init__(*args, **kwargs)
        self.word = kwargs["word"]
