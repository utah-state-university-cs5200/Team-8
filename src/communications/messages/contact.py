from src.communications.messages.request import Request


class Contact(Request):
    type_key = Request.freshTypeDict()
    type_key['clue_id'] = int
    type_key['guess'] = str

    def __init__(self, *args, **kwargs):
        """
        Contact message

        :param args:
        :param kwargs: {message_type_id, player_id, clue_id, guess}
        """
        super().__init__(*args, **kwargs)
        self.clue_id = kwargs["clue_id"]
        self.guess = kwargs["guess"]

    def player_id(self):
        return self.sender_id
