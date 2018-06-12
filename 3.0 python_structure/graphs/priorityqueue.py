# -*- coding: utf-8 -*-

# 二叉堆优先级队列

class PriorityQueue(object):
    def __init__(self):
        self.heaparray = [(0,0)]
        self.currentsize = 0
        
    def buildheap(self, alist):
        self.currentsize = len(alist)
        self.heaparray = [(0,0)]
        for i in alist:
            self.heaparray.append(i)
        i = len(alist)//2
        while i > 0:
            self.percdown(i)
            i = i - 1
            
    def percdown(self, i):
        while i*2 <= self.currentsize:
            mc = self.minchild(i)
            if self.heaparray[i][0] > self.heaparray[mc][0]:
                tmp = self.heaparray[i]
                self.heaparray[i] = self.heaparray[mc]
                self.heaparray[mc] = tmp
            i = mc
            
    def minchild(self, i):
        if i*2 > self.currentsize:
            return -1
        else:
            if i*2+1 > self.currentsize:
                return i*2
            else:
                return i*2+1
                
    def percup(self, i):
        while i//2 > 0:
            if self.heaparray[i][0] < self.heaparray[i//2][0]:
                tmp = self.heaparray[i//2]
                self.heaparray[i//2] = self.heaparray[i]
                self.heaparray[i] = tmp
            i = i//2
            
    def add(self, k):
        self.heaparray.append(k)
        self.currentsize = self.currentsize + 1
        self.percup(self.currentsize)
        
    def delmin(self):
        retval = self.heaparray[1][1]
        self.heaparray[1] = self.heaparray[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.heaparray.pop()
        self.percdown(1)
        return retval
        
    def isEmpty(self):
        if self.currentsize == 0:
            return True
        else:
            return False
        
    def decreasekey(self, val, amt):
        done = False
        i = 1
        mykey = 0
        while not done and i < self.currentsize:
            if self.heaparray[i][1] == val:
                done = True:
                mykey = i
            else:
                i = i + 1
        if mykey > 0:
            self.heaparray[mykey] = (amt, self.heaparray[mykey][1])
            self.percup(mykey)
            
    def __contains__(self, vtx):
        for pair in self.heaparray:
            if pair[1] = vtx:
                return True
        return False