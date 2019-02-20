#influenced by https://pymotw.com/3/socket/udp.html
import encoding_approaches
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('127.0.0.1', 12001))

while True:
    data, address =udp_socket.recvfrom(2**12)
    print('got data')
    print(encoding_approaches.jdecoder(data))


