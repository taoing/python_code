# -*- coding: utf-8 -*-

# 图的实现

import sys

class Vertex(object):
    '''顶点'''
    def __init__(self, key):
        self.id = key
        self.connectedto = {}
        self.color = 'white'
        self.pred = None
        self.dist = sys.maxsize
        self.disc = 0
        self.fin = 0

    def add_neighbor(self, nbr, weight=0):
        self.connectedto[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedto:' + str([x.id for x in connectedto])

    def get_connections(self):
        return self.connectedto.keys()

    def getid(self):
        return self.id

    def get_weight(self, nbr):
        return self.connectedto[nbr]

    def setcolor(self, color):
        self.color = color

    def setpred(self, pred):
        self.pred = pred

    def setdistance(self, d):
        self.dist = d

    def setdiscovery(self, t):
        self.disc = t

    def setfinish(self, t):
        self.fin = t

    def getcolor(self):
        return self.color

    def getpred(self):
        return self.pred

    def getdistance(self):
        return self.dist

    def getdiscovery(self):
        return self.disc

    def getfinish(self):
        return self.fin

class Graph(object):
    '''图, 顶点的列表'''
    def __init__(self):
        self.vertlist = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        newvertex = Vertex(key)
        self.vertlist[key] = newvertex
        return newvertex

    def get_vertex(self, n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertlist

    def addedge(self, f, t, cost=0):
        if f not in self.vertlist:
            nv = self.add_vertex(f)
        if t not in self.vertlist:
            nv = self.add_vertex(t)
        self.vertlist[f].add_neighbor(self.vertlist[t], cost)
    def get_vertices(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())


g = Graph()
for i in range(6):
    g.add_vertex(i)

print(g.vertlist)
g.addedge(0,1,5)
g.addedge(0,5,2)
g.addedge(1,2,4)
g.addedge(2,3,9)
g.addedge(3,4,7)
g.addedge(3,5,3)
g.addedge(4,0,1)
g.addedge(5,4,8)
g.addedge(5,2,1)

for v in g:
    for w in v.get_connections():
        print('({}, {})'.format(v.getid(), w.getid()))