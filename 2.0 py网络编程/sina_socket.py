#tcp socket

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
print('target IP:',socket.gethostbyname('www.sina.com.cn'))
s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
buf = []
while True:
	d = s.recv(1024)
	if d:
		buf.append(d)
	else:
		break
data = b''.join(buf)
header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html','wb') as f:
	f.write(html)
print('html is saved!')