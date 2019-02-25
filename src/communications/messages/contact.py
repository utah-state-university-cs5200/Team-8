from src.communications.messages.request import Request


class Contact(Request):
    def __init__(self, *args, **kwargs):
        """
        Contact message

        :param args:
        :param kwargs: {message_type_id, player_id, clue_id, guess}
        """
        super().__init__(*args, **kwargs)
        self.player_id = kwargs["player_id"]
        self.clue_id = kwargs["clue_id"]
        self.guess = kwargs["guess"]
