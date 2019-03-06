from src.communications.messages.reply import Reply

#also potentially wonky
class GameState(Reply):
    type_key = Reply.freshTypeDict()
    def __init__(self, *args, **kwargs):
        """
        Game State message

        :param args:
        :param kwargs: {message_type_id, request_id, message_status}
        """
        super().__init__(*args, **kwargs)
