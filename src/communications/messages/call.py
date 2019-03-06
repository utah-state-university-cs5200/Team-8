from src.communications.messages.request import Request


class Call(Request):
    type_key = Request.freshTypeDict()
    type_key['clue_id'] = int
    def __init__(self, *args, **kwargs):
        """
        Call message

        :param args:
        :param kwargs: {message_type_id}
        """
        super().__init__(*args, **kwargs)
        self.clue_id = kwargs['clue_id']
