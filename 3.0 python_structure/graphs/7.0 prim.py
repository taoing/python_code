# -*- coding: utf-8 -*-

import sys
from priorityqueue import PriorityQueue
from graph import Vertex, Graph

def prim(g, start):
    pq = PriorityQueue()
    for v in g:
        v.setPred(None)
        v.setdistance(sys.maxsize)
    start.setdistance(0)
    pq = buildheap([(v.getdistance(), v) for v in g])
    while not pq.isEmpty():
        currentvert = pq.delmin()
        for nextvert in currentvert.get_connections():
            newcost = currentvert.get_weight(nextvert)
            if nextvert in pq and newcost < nextvert.getdistance():
                nextvert.setpred(currentvert)
                nextvert.setdistance(newcost)
                pq.decreasekey(nextvert, newcost)