#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date : 2017-04-08 13:33:27

import functools
#decorator
def log(text='execute'):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s begin call' % text)
			func(*args,**kw)
			print('%s end call' % text)

		return wrapper

	return decorator

@log()
def now():
	print('2017-04-08')

now()
print(now.__name__)