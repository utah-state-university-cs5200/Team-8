from src.communications.messages.reply import Reply


class AssignID(Reply):
    def __init__(self, *args, **kwargs):
        """
        Assign ID message

        :param args:
        :param kwargs: {message_type_id, request_id, message_status, player_id}
        """
        super().__init__(*args, **kwargs)
        self.player_id = kwargs["player_id"]
