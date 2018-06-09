#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date : 2017-04-08 13:33:27

#decorator
def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)

	return wrapper

@log
def now():
	print('2017-04-08')

#now=log(now)
now()

#return decorator
def log2(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)

		return wrapper

	return decorator

@log2('execute')
def now2():
	print('2017-04-08')

#now2=log2('execute')(now2)
now2()
print(now2.__name__)