from src.communications.messages.reply import Reply


class GameServerDef(Reply):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        game_id = args[3]
