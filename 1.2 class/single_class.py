# -*- coding: utf-8 -*-

# 单例模式

class A(object):
    def __init__(self):
        print('init')

    def __new__(cls, *args, **kwargs):
        print('new %s' % cls.__name__)
        return object.__new__(cls, *args, **kwargs)

a = A()

print('*'*20)
class SingleA(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

single_a = SingleA()
single_a.value = 2
single_b = SingleA()

print(single_b.value)
print(single_a == single_b)
print(single_a)
print(single_b)

print('*'*20)
class SingleB(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'value'):
            self.value = 1

c = SingleB()
print(c.value)

c.value =2
d = SingleB()
print(d.value)
print(c == d)
print(c)
print(d)