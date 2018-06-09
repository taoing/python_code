# python web框架

import time

class Application(object):
    # 框架的核心部分
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get('PATH_INFO', '/')
        if path.startswith('/static'):
            file_path = '.' + path
            print('request file:', file_path)
            try:
                file = open(file_path, 'rb')
            except IOError:
                status = '404 Not Found'
                headers = []
                start_response(status, headers)
                response_body = 'The file not found!'
                return response_body
            else:
                status = '200 OK'
                headers = []
                start_response(status, headers)
                response_body = file.read().decode('utf-8')
                file.close()
                return response_body
        for url, handler in self.urls:
            if path == url:
                response_body = handler(env, start_response)
                return response_body
        # 请求路径不存在，返回404响应码
        status = '404 Not Found'
        headers = [('Content-Type', 'text/html')]
        start_response(status, headers)
        response_body = 'The file not found!'
        return response_body

def ctime(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    return time.ctime()

def hello(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    return 'Hello, World!'

urls = [
    ('/', hello),
    ('/ctime', ctime),
    ('/hello', hello)
    ]
app = Application(urls)