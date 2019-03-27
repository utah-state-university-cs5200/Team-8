
class Dispatcher:
    def __init__(self, conversation_dict, conversation_factory):
        self.conversation_dict = conversation_dict
        self.conversation_factory = conversation_factory

    def processEnvelope(self, envelope):
        print("Received envelope from {} containing {}".format(envelope.address, envelope.message)) # TODO: process an envelope