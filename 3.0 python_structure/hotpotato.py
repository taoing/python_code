#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2017-07-01 16:10:02

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

#"烫手山芋"模型
def hotpotato(namelist, num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotpotato(['bill','susan','jane','michel','david','bird'],7))