class Application(object):
    def __init__(self, environ, start_response):
        self.path = environ['PATH_INFO']
        self.start_response = start_response

    def __iter__(self):
        if self.path == '/':
            status = '200 OK'
            response_headers = [('Content-type', 'text/html')]
            self.start_response(status, response_headers)
            yield '<h1>Hello, world!</h1>'.encode('utf-8')

        elif self.path == '/wsgi':
            status = '200 OK'
            response_headers = [('Content-type', 'text/html')]
            self.start_response(status, response_headers)
            yield '<h1>Hello, WSGI!</h1>'.encode('utf-8')

        else:
            status = '404 NOT FOUND'
            response_headers = [('Content-type', 'text/html')]
            self.start_response(status, response_headers)
            yield '<h1>404 NOT FOUND</h1>'.encode('utf-8')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    app = make_server('127.0.0.1', 8000, Application)
    print('Server running at port 8000...')
    sa = app.socket.getsockname()
    print('http://{0}:{1}/'.format(*sa))

    app.serve_forever()