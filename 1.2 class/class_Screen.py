#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date : 2017-04-08 15:53:08

class Screen(object):
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self,width):
		self._width=width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,height):
		self._height=height

	@property
	def resolution(self):
		self._resolution=self._width*self._height
		return self._resolution

s=Screen()
s.width=1024
s.height=768
print(s.resolution)