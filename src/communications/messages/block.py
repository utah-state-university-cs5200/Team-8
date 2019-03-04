from src.communications.messages.request import Request


class Block(Request):
    type_key = Request.freshTypeDict()
    type_key['word'] = str
    type_key['clue_id'] = int
    def __init__(self, *args, **kwargs):
        """
        Block message

        :param args:
        :param kwargs: {message_type_id, word}
        """
        super().__init__(*args, **kwargs)
        self.word = kwargs["word"]
        self.clue_id = kwargs["clue_id"]
