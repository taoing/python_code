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


#模型：打印机队列

class Printer(object):
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startnext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getpages() * 60/self.pagerate

import random

class Task(object):
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getstamp(self):
        return self.timestamp

    def getpages(self):
        return self.pages

    def waittime(self,currenttime):
        return currenttime - self.timestamp

def simulation(numseconds, pagesperminute):
    labprinter = Printer(pagesperminute)
    printQueue = Queue()
    waitingtimes = []

    for currentsecond in range(numseconds):
        if newPrintTask():
            task = Task(currentsecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waittime(currentsecond))
            labprinter.startnext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print('Average wait %6.2f secs %3d tasks remaining.' % (averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

print('pagesperminute:5')
for i in range(10):
    simulation(3600,5)

print('pagesperminute:10')
for i in range(10):
    simulation(3600,10)