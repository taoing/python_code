# -*- coding: utf-8 -*-

from queue import Queue
from graph import Graph, Vertex

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

def bsf(g, start):
    start.setdistance(0)
    start.setpred(None)
    vertqueue = Queue()
    vertqueue.enqueue(start)
    while vertqueue.size() > 0:
        current_vert = vertqueue.dequeue()
        for nbr in current_vert.get_connections()
        if nbr.getcolor() == 'white':
            nbr.setcolor('gray')
            nbr.setdistance(current_vert.getdistance()+1)
            nbr.setpred(current_vert)
            vertqueue.enqueue(nbr)
        current_vert.setcolor('black')

def traverse(y):
    '''任何顶点开始, 沿前导链都可以回到根, 打印前导链'''
    x = y
    while x.getpred():
        print(x.getid())
        x = x.getpred()
    print(x.getid())

traverse(g.get_vertex('sage'))