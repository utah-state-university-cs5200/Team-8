from src.communications.messages.reply import Reply


class Ack(Reply):
    def __init__(self, *args, **kwargs):
        """
        Acknowledge message

        :param args: [message_type_id, request_id, status]
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
