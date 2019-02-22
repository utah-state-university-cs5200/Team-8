import encoding

class Message():
    generated_messages = 0
    request_or_reply = {
        1:'request',
        2:'reply',
    }
    def __init__(self,type_num, payload,
        message_id=None, destination=None, origin=None
        ):
        self.payload = payload
        self.type_num = type_num
        if message_id:
            self.message_id=message_id
            self.local=False
        else:
            self.message_id = Message.generated_messages
            self.local=True
            Message.generated_messages+=1
        if destination:
            self.destination=destination
        if origin:
            self.origin=origin

    def encode(self):
        details = [self.type_num, self.message_id]+self.payload
        return encoding.encoder(details)

    @classmethod
    def from_decoding(cls, json_str, origin=None):
        details = encoding.decoder(json_str)
        result = cls(details[0], details[2:], message_id=details[1], origin=origin)
        return result
