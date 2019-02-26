from src.communications.messages.reply import Reply


class GameList(Reply):
    def __init__(self, *args, **kwargs):
        """
        Game List message

        :param args:
        :param kwargs: {message_type_id, request_id, message_status, game_list}
        """
        super().__init__(*args, **kwargs)
        self.game_list = kwargs["game_list"]
