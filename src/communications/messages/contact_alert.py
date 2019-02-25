from src.communications.messages.request import Request


class ContactAlert(Request):
    def __init__(self, *args, **kwargs):
        """
        Contact Alert message

        :param args:
        :param kwargs: {message_type_id, clue_id}
        """
        super().__init__(*args, **kwargs)
        self.clue_id = kwargs["clue_id"]
