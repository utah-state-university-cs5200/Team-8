from src.client.player_client.player_client import PlayerClient
from src.communications.messages.constants import MESSAGE_ID_HELLO
from src.communications.messages.message_factory import MessageFactory

player_client = PlayerClient()


id_vals = {'message_id':2, 'sender_id':1}
m1 = MessageFactory.build(message_type_id=MESSAGE_ID_HELLO, player_alias="Test Alias", **id_vals)

player_client.tcp_communicator.sendMessage(m1)

# player_client.cleanup()
