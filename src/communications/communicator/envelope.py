

class Envelope:
    """Package a message with destination address"""

    def __init__(self, message, address):
        self.message = message
        self.address = address
