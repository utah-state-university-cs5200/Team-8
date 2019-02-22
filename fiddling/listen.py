#influenced by https://pymotw.com/3/socket/udp.html
from network_io import NetworkIO
from message import Message

interface = NetworkIO(('127.0.0.1', 12001))

while True:
    interface.recieve()
    print('got data')
    print(interface.inbox[-1].payload)


