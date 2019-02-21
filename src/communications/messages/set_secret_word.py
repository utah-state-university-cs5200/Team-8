from src.communications.messages.request import Request


class SetSecretWord(Request):
    def __init__(self, *args, **kwargs):
        """
        Set Secret Word message

        :param args: [message_type_id, player_id, secret_word]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.player_id = args[1]
        self.secret_word = args[2]
