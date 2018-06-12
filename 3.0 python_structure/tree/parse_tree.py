# -*- coding: utf-8 -*-

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

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

    def preorder(self):
        '''前序遍历'''
        print(self.get_rootval())
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()

# 分析树 二叉树表示完全括号表达式

def build_parse_tree(fpexp):
    fplist = fpexp.split()
    pstack = Stack()
    etree = BinaryTree('')
    pstack.push(etree)
    current_tree = etree
    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            pstack.push(current_tree)
            current_tree = current_tree.get_leftchild()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_rootval(int(i))
            parent = pstack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_rootval(i)
            current_tree.insert_right('')
            pstack.push(current_tree)
            current_tree = current_tree.get_rightchild()
        elif i == ')':
            current_tree = pstack.pop()
        else:
            raise ValueError

    return etree

pt = build_parse_tree('( ( 10 + 5 ) * 3 )')


# 计算分析树
def evaluate(parse_tree):
    opers = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv
    }

    left_child = parse_tree.get_leftchild()
    right_child = parse_tree.get_rightchild()

    if left_child and right_child:
        fn = opers[parse_tree.get_rootval()]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.get_rootval()

class Operator(object):
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y
    def mul(self, x, y):
        return x * y
    def truediv(self, x, y):
        return x/y

operator = Operator()
print('......')
print(evaluate(pt))
print('......')

# 树的遍历

def preorder(tree):
    '''前序遍历'''
    if tree:
        print(tree.get_rootval())
        preorder(tree.get_leftchild())
        preorder(tree.get_rightchild())

def postorder(tree):
    '''后序遍历'''
    if tree != None:
        postorder(tree.get_leftchild())
        postorder(tree.get_rightchild())
        print(tree.get_rootval())

def postordereval(tree):
    '''后序遍历计算分析树'''
    opers = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv
    }
    if tree:
        res1 = postordereval(tree.get_leftchild())
        res2 = postordereval(tree.get_rightchild())
        if res1 and res2:
            fn = opers[tree.get_rootval()]
            return fn(res1, res2)
        else:
            return tree.get_rootval()

def inorder(tree):
    '''中序遍历, 先访问左树, 其次是根, 然后右树'''
    if tree != None:
        inorder(tree.get_leftchild())
        print(tree.get_rootval())
        inorder(tree.get_rightchild())

def printexp(tree):
    '''中序遍历返回完全括号表达式'''
    sval = ''
    if tree:
        if tree.get_leftchild() and tree.get_rightchild():
            sval = '(' + printexp(tree.get_leftchild())
            sval = sval + str(tree.get_rootval())
            sval = sval + printexp(tree.get_rightchild()) + ')'
        else:
            sval = str(tree.get_rootval())
    return sval

print('前序遍历...')
preorder(pt)
print('后序遍历...')
postorder(pt)
postordereval(pt)
print('中序...')
inorder(pt)
print(printexp(pt))