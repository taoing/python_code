# -*- coding: utf-8 -*-

# 查找树

class TreeNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent

    def has_leftchild(self):
        return self.leftchild

    def has_rightchild(self):
        return self.rightchild

    def is_leftchild(self):
        return self.parent and self.parent.leftchild == self

    def is_rightchild(self):
        return self.parent and self.parent.rightchild == self

    def isroot(self):
        return not self.parent

    def isleaf(self):
        return not(self.leftchild or self.rightchild)

    def has_anychildren(self):
        return self.leftchild or self.rightchild

    def has_bothchildren(self):
        return self.leftchild and self.rightchild

    def replace_nodedata(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftchild = lc
        self.rightchild = rc
        if self.has_leftchild():
            self.leftchild.parent = self
        if self.has_rightchild():
            self.rightchild.parent = self


    def spliceout(self):
        if self.isleaf():
            if self.is_leftchild():
                self.parent.leftchild = None
            else:
                self.parent.rightchild = None
        elif self.has_anychildren():
            if self.has_leftchild():
                if self.is_leftchild():
                    self.parent.leftchild = self.leftchild
                else:
                    self.parent.rightchild = self.leftchild
                self.leftchild.parent = self.parent
            else:
                if self.is_leftchild():
                    self.parent.leftchild = self.rightchild
                else:
                    self.parent.rightchild = self.rightchild
                self.rightchild.parent.self.parent

    def find_successor(self):
        succ = None
        if self.has_rightchild():
            succ = self.rightchild.findmin()
        else:
            if self.parent:
                if self.is_leftchild():
                    succ = self.parent
                else:
                    self.parent.rightchild = None
                    succ = self.parent.find_successor()
                    self.parent.rightchild = self

        return succ

    def findmin(self):
        current = self
        while current.has_leftchild():
            current = current.leftchild
        return current



class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentnode):
        if key < currentnode.key:
            if currentnode.has_leftchild():
                self._put(key, val, currentnode.leftchild)
            else:
                currentnode.leftchild = TreeNode(key, val, parent=currentnode)

        # 相等情况, 更新值更好, 可修改
        elif key == currentnode.key:
            currentnode.payload = val

        else:
            if currentnode.has_rightchild():
                self._put(key, val, currentnode.rightchild)
            else:
                currentnode.rightchild = TreeNode(key, val, parent=currentnode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None

    def _get(self, key, currentnode):
        if not currentnode:
            return None
        elif currentnode.key == key:
            return currentnode
        elif key < currentnode.key:
            return self._get(key, currentnode.leftchild)
        else:
            return self._get(key, currentnode.rightchild)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)


    def remove(self, currentnode):
        if currentnode.is_leaf():
            if currentnode == currentnode.parent.leftchild:
                currentnode.parent.leftchild = None
            else:
                currentnode.parent.rightchild = None
        elif currentnode.has_bothchildren():
            succ = currentnode.find_successor()
            succ.spliceout()
            currentnode.key = succ.key
            currentnode.payload = succ.payload
        else:
            if currentnode.has_leftchild():
                if currentnode.is_leftchild():
                    currentnode.leftchild.parent = currentnode.parent
                    currentnode.parent.leftchild = currentnode.leftchild
                elif currentnode.is_rightchild():
                    currentnode.leftchild.parent = currentnode.parent
                    currentnode.parent.rightchild = currentnode.leftchild
                else:
                    currentnode.replace_nodedata(currentnode.leftchild.key, currentnode.leftchild.payload, currentnode.leftchild.leftchild, currentnode.leftchild.rightchild)
            else:
                if currentnode.is_leftchild():
                    currentnode.rightleft.parent = currentnode.parent
                    currentnode.parent.leftchild = currentnode.rightchild
                elif currentnode.is_rightchild:
                    currentnode.rightchild.parent = currentnode.parent
                    currentnode.parent.rightchild = currentnode.rightchild
                else:
                    currentnode.replace_nodedata(currentnode.rightchild.key, currentnode.rightchild.payload, currentnode.rightchild.leftchild, currentnode.rightchild.rightchild)

    def __getitem__(self, key):
        return self.get(key)


mytree = BinarySearchTree()
mytree[3] = 'red'
mytree[4] = 'blue'
mytree[6] = 'yellow'
mytree[2] = 'at'

print(mytree[6])
print(mytree[2])