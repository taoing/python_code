class Application(object):
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        path = self.environ['PATH_INFO']
        if path == '/':
            return self.GET_index()
        elif path == '/wsgi':
            return self.GET_wsgi()
        else:
            return self.notfound()

    def GET_index(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        self.start_response(status, response_headers)
        yield '<h1>Hello, World!</h1>'.encode('utf-8')

    def GET_wsgi(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        self.start_response(status, response_headers)
        yield '<h1>Hello, WSGI!</h1>'.encode('utf-8')

    def notfound(self):
        status = '404 NOT FOUND'
        response_headers = [('Content-type', 'text/html')]
        self.start_response(status, response_headers)
        yield '<h1>NOT FOUND</h1>'.encode('utf-8')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    app = make_server('127.0.0.1', 8000, Application)
    print('Server running at port 8000...')
    sa = app.socket.getsockname()
    print('http://{0}:{1}/'.format(*sa))

    app.serve_forever()