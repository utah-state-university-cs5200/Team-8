from src.communications.messages.request import Request


class SetSecretWord(Request):
    type_key = Request.freshTypeDict()
    type_key['player_id'] = int
    type_key['secret_word'] = str
    def __init__(self, *args, **kwargs):
        """
        Set Secret Word message

        :param args:
        :param kwargs: {message_type_id, player_id, secret_word}
        """
        super().__init__(*args, **kwargs)
        self.player_id = kwargs["player_id"]
        self.secret_word = kwargs["secret_word"]
