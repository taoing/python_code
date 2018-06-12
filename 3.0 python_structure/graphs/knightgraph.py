# -*- coding: utf-8 -*-

# 骑士旅图

from graph import Graph, Vertex

def knight_graph(bdsize):
    '''构建骑士旅图, bdsize为板的大小, bdsize*bdsize'''
    ktgraph = Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeid = pos_to_nodeid(row, col, bdsize)
            new_positions = gen_legal_moves(row, column, bdsize)
            for e in new_positions:
                nid = pos_to_nodeid(e[0], e[1], bdsize)
                ktgraph.addedge(nodeid, nid)

    return ktgraph

def pos_to_nodeid(row, column, bdsize):
    '''根据板上坐标位置计算出对应的节点id'''
    return row*bdsize + column

def gen_legal_moves(x, y, bdsize):
    '''计算所有的合法移动'''
    new_moves = [] #列表存储所有的合法移动
    # 所有可能移动的相对坐标, 骑士'跳日'移动
    moveoffsets = [(-1,-2), (-1,2), (-2,-1), (-2,-1), (1,-2), (1,2), (2,-1), (2,1)]
    for i in moveoffsets:
        # 由相对移动计算移动后的实际坐标
        newx = x + i[0]
        newy = y + i[1]
        if legal_coord(newx, bdsize) and legal_coord(newy, bdsize):
            new_moves.append((newx, newy))
    return new_moves

def legal_coord(x, bdsize):
    '''判断是否是合法坐标'''
    if x >= 0 and x < bdsize:
        return True
    else:
        return False


# 骑士之旅
'''参数:
n:搜索树中的当前深度
path:到此为止访问的顶点的列表
u:图中我们希望探索的顶点
limit:路径中的节点数
'''

def knight_tour(n, path, u, limit):
    '''实现骑士之旅'''
    u.setcolor('gray')
    path.append(u)
    if n < limit:
        nbrlist = list(u.get_connections())
        i = 0
        done = False
        while i < len(nbrlist) and not done:
            if nbrlist[i].getcolor() == 'white':
                done = knight_tour(n+1, path, nbrlist[i], limit)
            i =i + 1
        if not done:
            path.pop()
            u.setcolor('white')
    else:
        done = True
    return done

# 使用orderby_avail代替get_connections
def orderby_avail(n):
    '''优先选择可移动数少的下一个顶点'''
    reslist = []
    for v in n.get_connections():
        if v.getcolor() == 'white':
            c = 0
            for w in v.get_connections():
                if w.getcolor() == 'white':
                    c = c + 1
            reslist.append((c, v))
    reslist.sort(key=lambda x: x[0])
    return [y[1] for y in reslist]