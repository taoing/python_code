# -*- coding: utf-8 -*-

# 字梯图

class Vertex(object):
    '''顶点'''
    def __init__(self, key):
        self.id = key
        self.connectedto = {}

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

def buildgraph(wordfile):
    d = {}
    g = Graph()
    wfile = open(wordfile, 'r').readlines()
    # 创建只有一个字母不同的单词桶
    for line in wfile:
        word = line[:-1] #去掉单词末尾的换行符
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # 在同一个桶中为每一个单词添加顶点和边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addedge(word1, word2)

    return g