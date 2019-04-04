from src.communications.messages.encoder_decoder import decode


class Dispatcher:
    def __init__(self, conversation_dict, conversation_factory):
        self.conversation_dict = conversation_dict
        self.conversation_factory = conversation_factory

    def process(self, envelope):
        conversation = self.conversation_dict.get(envelope.message.conversation_id)
        if conversation is None:
            message = decode(envelope.message)
            # TODO: need to determine the conversation_type_id and pass that in
            conversation = self.conversation_factory.build(remote_endpoint=envelope.address, **message.getAttributes())

        conversation.process(envelope)
