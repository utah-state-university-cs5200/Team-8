class MockDispatcher:
    def __init__(self):
        self.received = []

    def processEnvelope(self, envelope):
        self.received.append(envelope)
