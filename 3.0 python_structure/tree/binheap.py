# -*- coding: utf-8 -*-

# 二叉堆

class BinHeap(object):
    def __init__(self):
        self.heaplist = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i//2 >0:
            if self.heaplist[i] < self.heaplist[i//2]:
                tmp = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heaplist.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while (i*2) <= self.current_size:
            mc = self.minchild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def minchild(self, i):
        if i*2+1 > self.current_size:
            return i*2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delmin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.current_size]
        self.current_size = self.current_size - 1
        self.heaplist.pop()
        self.perc_down(1)
        return retval

    def buildheap(self, alist):
        i = len(alist)//2
        self.current_size = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1

    def buildheap_append(self, alist):
        while len(alist) > 0:
            self.insert(alist.pop())

bh = BinHeap()
bh.buildheap([9,5,6,2,3])
bh2 = BinHeap()
bh2.buildheap_append([3,2,6,5,9])

print(bh.heaplist)
print(bh2.heaplist)

print(bh.delmin())
print(bh.delmin())
print(bh.delmin())
print(bh.delmin())
print(bh.delmin())

print(bh2.delmin())
print(bh2.delmin())
print(bh2.delmin())
print(bh2.delmin())
print(bh2.delmin())