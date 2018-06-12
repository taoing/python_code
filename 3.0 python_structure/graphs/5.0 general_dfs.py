# -*- coding: utf-8 -*-

from graph import Graph

class DFSGraph(Graph):
    def __init__(self):
        super(DFSGraph, self).__init__()
        self.time = 0

    def dfs(self):
        for avertex in self:
            avertex.setcolor('white')
            avertex.setpred(-1)
        for avertex in self:
            if avertex.getcolor() == 'white':
                self.dfsvisit(avertex)

    def dfsvisit(self, startvertex):
        startvertex.setcolor('gray')
        self.time = self.time + 1
        startvertex.setdiscovery(self.time)
        for nextvertex in startvertex.get_connections():
            if nextvertex.getcolor() == 'white':
                nextvertex.setpred(startvertex)
                self.dfsvisit(nextvertex)
        startvertex.setcolor('black')
        self.time = self.time + 1
        startvertex.setfinish(self.time)