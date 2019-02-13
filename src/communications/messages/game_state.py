from src.communications.messages.reply import Reply


class GameState(Reply):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
