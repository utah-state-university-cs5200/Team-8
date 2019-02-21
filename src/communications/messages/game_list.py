from src.communications.messages.reply import Reply


class GameList(Reply):
    def __init__(self, *args, **kwargs):
        """
        Game List message

        :param args: [message_type_id, request_id, status, game_list]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.game_list = args[3]
