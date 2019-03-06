from src.communications.messages.request import Request

#submitting a clue-guess pair for others to contact with
class SubmitGuess(Request):
    type_key = Request.freshTypeDict()
    type_key['player_id'] = int
    type_key['word'] = str
    type_key['clue'] = str

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
