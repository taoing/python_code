import time

def application(env, start_response):
	status = '200 OK'
	headers = [('Content-Type', 'text/html')]
	start_response(status, headers)
	return time.ctime()