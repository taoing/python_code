import socket
from multiprocessing import Process
import re

class HTTPServer(object):
    def __init__(self, application):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.app = application
    def bind(self, port):
        self.server_socket.bind(('', port))
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
        ('Server', 'MyWebServer 1.0')
        ]
        server_headers = headers + server_headers
        # 构造响应首部行
        response_headers = 'HTTP/1.1 ' + status + '\r\n'
        for header in server_headers:
            response_headers = response_headers + '%s:%s' % header + '\r\n'
        self.response_headers = response_headers

    def handle_request(self, conn_socket):
        '''处理客户端请求'''
        env = {}
        request_data = conn_socket.recv(2048).decode('utf-8')
        print('request from client:')
        print(request_data)
        '''解析请求返回响应'''
        # 请求行
        reuqestmethodline = request_data.split('\r\n')[0]
        # 请求方法
        requestmethod = reuqestmethodline.split(' ', 1)[0]
        # 请求资源
        requestpath = re.match(r'\w+\s+(/[^\s]*)',reuqestmethodline).group(1)# [^\s]匹配非空字符
        env['Method'] = requestmethod
        env['PATH_INFO'] = requestpath
        # 返回响应体
        response_body = self.app(env, self.start_response)
        response = self.response_headers + '\r\n' + response_body
        print('response from server:')
        print(response)
        conn_socket.send(response.encode('utf-8'))
        conn_socket.close()