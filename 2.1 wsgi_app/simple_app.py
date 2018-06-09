def application(environ, start_response):
	status = '200 OK'
	response_headers = [('Content-type', 'text/html')]
	start_response(status, response_headers)
	body = '<h1>Hello, {name} !</h1>'.format(name = environ['PATH_INFO'][1:] or 'WSGI')
	for header in environ.items():
		print(header)

	return [body.encode('utf-8')]

if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	app = make_server('127.0.0.1', 8000, application)
	print('Server running at port 8000...')
	app.serve_forever()