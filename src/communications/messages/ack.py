from src.communications.messages.reply import Reply


class Ack(Reply):
    type_key = Reply.freshTypeDict()
    def __init__(self, *args, **kwargs):
        """
        Acknowledge message

        :param args:
        :param kwargs: {message_type_id, request_id, status}
        """
        super().__init__(*args, **kwargs)
