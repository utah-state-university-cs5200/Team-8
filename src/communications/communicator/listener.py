from threading import Thread


class Listener(Thread):
    """
    Parent server listener class to be specialized into UDP and TCP variants.

    Binds to an address, listens for incoming messages, puts those messages into envelopes,
    and sends those envelopes to the dispatcher to be processed

    :note: Specializations must implement _initSocket and run methods
    :note: Dispatcher is expected to have a processEnvelope(envelope) method
    """
    def __init__(self, dispatcher, address, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.alive = True
        self.dispatcher = dispatcher
        self.address = address
        self._initSocket()

    def _initSocket(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def cleanup(self):
        self.alive = False
        self.sock.close()

    def dispatchEnvelope(self, envelope):
        self.dispatcher.processEnvelope(envelope)
