from src.communications.messages.reply import Reply


class GameList(Reply):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_list = args[3]
