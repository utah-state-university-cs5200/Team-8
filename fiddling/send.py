import encoding_approaches
import socket
from time import sleep

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message_queue = [
    (1,1,'bean noises', 'fart'),
    (2,3,1, 'fart noises')
]
for message in message_queue:
    udp_socket.sendto(
        encoding_approaches.jencoder(message),
        ('127.0.0.1', 12001)
        )
    sleep(.5)
