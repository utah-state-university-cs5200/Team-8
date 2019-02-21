from src.communications.messages.reply import Reply


class GameServerDef(Reply):
    def __init__(self, *args, **kwargs):
        """
        Game Server Definition message

        :param args: [message_type_id, request_id, status, game_id]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.game_id = args[3]
