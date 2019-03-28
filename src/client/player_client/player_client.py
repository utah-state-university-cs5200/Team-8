from src.client.client import Client
from src.contact.player import Player


class PlayerClient(Client):
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.player = Player()

    def hello(self):
        hello_conversation = self.conversation_factory.build(
            conversation_type_id=HELLO_INITIATOR_CONVERSATION,
            conversation_id=self.getNextConversationID(),
            remote_endpoint=self.serverUDPAddress,
            player_alias=self.player.alias,
            timeout=timeout)
        hello_conversation.start()
        self.conversation_dict.add(hello_conversation)
