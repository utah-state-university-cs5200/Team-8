from src.communications.messages.request import Request


class UpdateClients(Request):
    def __init__(self, *args, **kwargs):
        """
        Update Clients message

        :param args:
        :param kwargs: {message_type_id, request_id, message_status}
        """
        super().__init__(*args, **kwargs)
