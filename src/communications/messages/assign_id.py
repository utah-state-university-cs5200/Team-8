from src.communications.messages.reply import Reply


class AssignID(Reply):
    def __init__(self, *args, **kwargs):
        """
        Assign ID message

        :param args: [message_type_id, request_id, status, player_id]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.player_id = args[3]
