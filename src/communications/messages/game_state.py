from src.communications.messages.reply import Reply


class GameState(Reply):
    def __init__(self, *args, **kwargs):
        """
        Game State message

        :param args: [message_type_id, request_id, status]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
