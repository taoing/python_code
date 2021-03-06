import socket
from multiprocessing import Process
import re

root_path = './static/'

class HTTPServer(object):
    def __init__(self, ip, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
    def start(self):
        self.server_socket.listen(128)
        print('HTTP server is running...')

        while True:
            conn_socket, client_addr = self.server_socket.accept()
            print('connection from %s : %s' % client_addr)
            # 创建新进程处理客户端连接
            p = Process(target = self.handle_request, args = (conn_socket,))
            p.start()
            conn_socket.close()
    def handle_request(self, conn_socket):
        '''处理客户端请求'''
        request_data = conn_socket.recv(2048).decode('utf-8')
        print('request data:')
        print(request_data)
        '''解析请求返回响应'''
        # 请求行
        requestmethodline = request_data.split('\r\n')[0]
        # 请求方法
        requestmethod = requestmethodline.split(' ', 1)[0]
        # 请求资源
        requestpath = re.match(r'\w+\s+(/[a-zA-Z0-9\_\.]*)',requestmethodline).group(1)
        if requestmethod == 'GET':
            if requestpath == '/':
                getfilename = 'index.html'
            else:
                getfilename = requestpath[1:]
            getfile = root_path + getfilename
            print('request file >>> %s' % getfile)
            # 读取文件系统中的资源，构造响应
            try:
                fp = open(getfile, 'r', encoding = 'utf-8')
            # 如果请求资源不存在，返回404响应
            except IOError:
                responsebody = '<h1>The file not found!</h1>'
                responseheader = 'HTTP/1.1 404 Not Found' + '\r\n' + 'Content-Type: text/html' + '\r\n\r\n'
            else:
                responsebody = fp.read()
                fp.close()
                responseheader = 'HTTP/1.1 200 OK' + '\r\n' + 'Content-Type: text/html' + '\r\n\r\n'
            finally:
                response = responseheader + responsebody
                print('response:')
                print(response)
                conn_socket.send(response.encode('utf-8'))
                conn_socket.close()

def main():
    http_server = HTTPServer('', 8000)
    http_server.start()

if __name__ == '__main__':
    main()