from src.communications.messages.reply import Reply


class AssignID(Reply):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player_id = args[3]
