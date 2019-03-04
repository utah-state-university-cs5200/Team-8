from src.communications.messages.reply import Reply


class GameServerDef(Reply):
    type_key = Reply.freshTypeDict()
    type_key['game_id'] = int
    def __init__(self, *args, **kwargs):
        """
        Game Server Definition message

        :param args:
        :param kwargs: {message_type_id, request_id, message_status, game_id}
        """
        super().__init__(*args, **kwargs)
        self.game_id = kwargs["game_id"]
