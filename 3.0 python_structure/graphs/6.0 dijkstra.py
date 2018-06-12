# -*- coding: utf-8 -*-

from priorityqueue import PriorityQueue
from graph import Graph, Vertex

def dijkstra(agraph, start):
    pq = PriorityQueue()
    start.setdistance(0)
    pq.buildheap([(v.getdistance(), v) for v in agraph])
    while not pq.isEmpty():
        currentvert = pq.delmin()
        for nextvert in currentvert.get_connections():
            newdist = currentvert.getdistance() + currentvert.get_weight(nextvert)
            if newdist < nextvert.getdistance():
                nextvert.setdistance(newdist)
                nextvert.setpred(currentvert)
                pq.decreasekey(newvert, newdist)