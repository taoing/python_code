import socket
from threading import Thread
import time

def tcplink(server_socket, addr):
    print('Accept new connection from %s:%s' % addr)
    server_socket.send(b'Welcome!')
    while True:
        data = server_socket.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        server_socket.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    server_socket.close()
    print('Connection from %s:%s closed!' % addr)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8113))
s.listen(5)
print('Waiting for connection...')
while True:
    server_socket, addr = s.accept()
    print('server_socket: %s' % server_socket)
    t = Thread(target = tcplink, args = (server_socket, addr))
    t.start()