from src.communications.messages.request import Request


class ContactAlert(Request):
    def __init__(self, *args, **kwargs):
        """
        Contact Alert message

        :param args: [message_type_id, clue_id]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.clue_id = args[1]
