from network_io import NetworkIO
from message import Message
from time import sleep

interface = NetworkIO(('127.0.0.1', 12002))

message_queue = [
    [1,1,'bean noises', 'fart'],
    [2,3,1, 'fart noises']
]
destination = ('127.0.0.1', 12001)
for message in message_queue:
    interface.outbox.append(
        Message(1,message,destination=destination)
        )

while not len(interface.outbox)==0:
    print('sent')
    interface.transmit()
    sleep(.5)
