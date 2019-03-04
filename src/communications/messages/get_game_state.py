from src.communications.messages.request import Request

#probably needs player_id?
class GetGameState(Request):
    type_key = Request.freshTypeDict()
    def __init__(self, *args, **kwargs):
        """
        Get Game State message

        :param args:
        :param kwargs: {message_type_id}
        """
        super().__init__(*args, **kwargs)
