#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date : 2017-04-08 14:32:21

class Student(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value <0 or value>100:
			raise ValueError('score must between 0~100!')
		self._score=value

s=Student()
s.score=88
print(s.score)


class Student(object):
	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self,value):
		self._birth=value

	@property
	def age(self):
		return 2017-self.birth

s=Student()
s.birth=1998
print(s.birth)
print(s.age)
