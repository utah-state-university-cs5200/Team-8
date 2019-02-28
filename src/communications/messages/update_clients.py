from src.communications.messages.request import Request

#hoo boy this is going to get fleshed out
class UpdateClients(Request):
    type_key = Request.freshTypeDict()
    def __init__(self, *args, **kwargs):
        """
        Update Clients message

        :param args:
        :param kwargs: {message_type_id, request_id, message_status}
        """
        super().__init__(*args, **kwargs)
