from src.communications.messages.request import Request


class SubmitGuess(Request):
    def __init__(self, *args, **kwargs):
        """
        Submit Guess message

        :param args:
        :param kwargs: {message_type_id, player_id, word, clue}
        """
        super().__init__(*args, **kwargs)
        self.player_id = kwargs["player_id"]
        self.word = kwargs["word"]
        self.clue = kwargs["clue"]
