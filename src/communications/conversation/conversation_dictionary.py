import time

from threading import Thread

GARBAGE_COLLECTION_SLEEP = 1


class ConversationDictionary:
    def __init__(self):
        self._conversation_dict = {}
        self._garbage_collector_thread_alive = True
        self._garbage_collector_thread = Thread(target=self._garbage_collector, args=())
        self._garbage_collector_thread.start()

    def get(self, key):
        try:
            return self._conversation_dict[key]
        except KeyError:
            return None

    def add(self, conversation):
        if conversation.conversation_id:
            self._conversation_dict[conversation.conversation_id] = conversation
            return True
        return False

    def remove(self, key):
        try:
            del self._conversation_dict[key]
            return True
        except KeyError:
            return False

    def cleanup(self):
        self._garbage_collector_thread_alive = False

    def _garbage_collector(self):
        while self._garbage_collector_thread_alive:
            time.sleep(GARBAGE_COLLECTION_SLEEP)
            for key in list(self._conversation_dict.keys()):
                if not self._conversation_dict[key].is_alive():
                    self.remove(key)
