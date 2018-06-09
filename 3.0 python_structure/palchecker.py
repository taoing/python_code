#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2017-07-01 16:10:02

class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


#回文检查

def palchecker(astring):
    chardeque = Deque()
    for ch in astring:
        chardeque.addRear(ch)

    stillequal = True
    while chardeque.size() > 1 and stillequal:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillequal = False

    return stillequal

print(palchecker('asdfghjkl'))
print(palchecker('asdfdsa'))
print(palchecker('asddsa'))