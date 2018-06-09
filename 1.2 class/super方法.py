# -*- coding: utf-8 -*-

# super方法

class Base(object):
    def __init__(self, *args, **kwargs):
        print('enter Base')
        print('leave Base')

class A(Base):
    def __init__(self, *args, **kwargs):
        print('enter A')
        super(A, self).__init__(*args, **kwargs)
        print('leave A')

class B(Base):
    def __init__(self, *args, **kwargs):
        print('enter B')
        super(B, self).__init__(*args, **kwargs)
        print('leave B')

class C(A, B):
    def __init__(self, *args, **kwargs):
        print('enter C')
        super().__init__(*args, **kwargs) #super()中的参数恪已省略
        print('leave C')

c = C()
print('C的方法解析顺序列表:', C.mro())