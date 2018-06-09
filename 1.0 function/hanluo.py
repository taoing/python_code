#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-26 20:24:29
# @Author  : mx (${email})
# @Link    : ${link}
# @Version : $Id$

import os
def move(n,a,b,c):
	if n==1:
	    print('move:',a,'--->',c)
	    return
	move(n-1,a,c,b)
	print('move:',a,'--->',c)#第n个盘子从A到C
	move(n-1,b,a,c)#剩余n-1个盘子从b到C
move(1,'A','B','C')
print('\n')
move(2,'A','B','C')
print('\n')
move(3,'A','B','C')
print('\n')
move(4,'A','B','C')
print('\n')
move(5,'A','B','C')
print('\n')
