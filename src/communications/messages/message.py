

class Message:
    def __init__(self, *args, **kwargs):
        """
        Parent message class for both request and reply messages

        :param args: [message_type_id]
        :param kwargs:
        """
        self.id = args[0]

    def getAttributes(self):
        return vars(self)
