#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date : 2017-04-08 14:32:21

class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score

def print_score(self):
	print('%s:%s' % (self.name,self.score))

class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self,score):
		if 0<=score<=100:
			self.__score=score
		else:
			raise ValueError('bad score')

lisa=Student('Lisa',88)
lisa.__name
lisa._Student__name
lisa.__name='NName'
lisa.get_name()
