# -*- coding: utf-8 -*-

# 二叉树 节点

class BinaryTree(object):
    def __init__(self, root_obj):
        self.key = root_obj
        self.leftchild = None
        self.rightchild = None

    def insert_left(self, new_node):
        if self.leftchild == None:
            self.leftchild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insert_right(self, new_node):
        if self.rightchild == None:
            self.rightchild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.rightchild = self.rightchild
            self.rightchild = t

    def get_rightchild(self):
        return self.rightchild

    def get_leftchild(self):
        return self.leftchild

    def get_rootval(self):
        return self.key

    def set_rootval(self, obj):
        self.key = obj

r = BinaryTree('a')
print(r.get_leftchild())
print(r.get_rightchild())
r.insert_left('b')
print(r.get_leftchild())
r.insert_right('c')
print(r.get_rightchild())