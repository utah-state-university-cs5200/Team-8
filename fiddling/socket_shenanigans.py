import socket

t1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
t2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('127.0.0.1', 1700)
t1.bind(address)
t2.connect(address)
t2.sendto('bits'.encode(), address)
