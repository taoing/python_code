import socket
from multiprocessing import Process
import re
import sys

root_path = './static'
wsgipy = './wsgipy'
env = {}

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
    def start_response(self, status, headers):
        server_headers = [
        ('Server', 'Myserver 1.0')
        ]
        server_headers = headers + server_headers
        response_headers = 'HTTP/1.1 ' + status + '\r\n'
        for header in server_headers:
            response_headers = response_headers + '%s:%s' % header + '\r\n'
        self.response_headers = response_headers

    def handle_request(self, conn_socket):
        '''处理客户端请求'''
        request_data = conn_socket.recv(2048).decode('utf-8')
        print('request data:')
        print(request_data)
        '''解析请求返回响应'''
        # 请求行
        reuqestmethodline = request_data.split('\r\n')[0]
        # 请求方法
        requestmethod = reuqestmethodline.split(' ', 1)[0]
        # 请求资源
        requestpath = re.match(r'\w+\s+(/[a-zA-Z0-9\_\.]*)',reuqestmethodline).group(1)
        env['Method'] = requestmethod
        env['PATH_INFO'] = requestpath

        if requestmethod == 'GET':
            if requestpath.endswith('.py'):
                try:
                    app = __import__(requestpath[1:-3])
                except ImportError:
                    self.response_headers = 'HTTP/1.1 404 Not Found' + '\r\n'
                    response_body = 'The file not found!'
                else:
                    response_body = app.application(env, self.start_response)
                response = self.response_headers + '\r\n' + response_body
                print('response:')
                print(response)
                conn_socket.send(response.encode('utf-8'))
                conn_socket.close()
            else:
                if requestpath == '/':
                    getfilename = '/index.html'
                else:
                    getfilename = requestpath
                getfile = root_path + getfilename
                print('request file >>> %s' % getfile)
                # 读取文件系统中的资源，构造响应
                try:
                    fp = open(getfile, 'r', encoding = 'utf-8')
                # 如果请求资源不存在，返回404响应
                except IOError:
                    response_body = '<h1>The file not found!</h1>'
                    response_header = 'HTTP/1.1 404 Not Found' + '\r\n' + 'Content-Type: text/html' + '\r\n\r\n'
                else:
                    response_body = fp.read()
                    fp.close()
                    response_header = 'HTTP/1.1 200 OK' + '\r\n' + 'Content-Type: text/html' + '\r\n\r\n'
                finally:
                    response = response_header + response_body
                    print('response:')
                    print(response)
                    conn_socket.send(response.encode('utf-8'))
                    conn_socket.close()

def main():
    http_server = HTTPServer('', 8000)
    http_server.start()

if __name__ == '__main__':
    sys.path.insert(1, wsgipy)
    main()