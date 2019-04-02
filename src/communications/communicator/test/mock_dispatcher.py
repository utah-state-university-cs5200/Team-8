class MockDispatcher:
    def __init__(self):
        self.received = []

    def process(self, envelope):
        self.received.append(envelope)
