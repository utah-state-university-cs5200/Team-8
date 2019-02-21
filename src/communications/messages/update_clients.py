from src.communications.messages.request import Request


class UpdateClients(Request):
    def __init__(self, *args, **kwargs):
        """
        Update Clients message

        :param args: [message_type_id, request_id, status]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
