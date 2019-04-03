from threading import Thread


class Worker(Thread):
    def __init__(self, master):
        self.master = master
