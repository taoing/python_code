#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2017-07-01 14:47:13

#中缀表达式转后缀表达式

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

def infixTopostfix(infixexpr):
    prec = {'*':3,'/':3,'+':2,'-':2,'(':1}
    opstack = Stack()
    postfixlist = []
    tokenlist = infixexpr.split()

    for token in tokenlist:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixlist.append(token)

        elif token == '(':
            opstack.push(token)

        elif token == ')':
            toptoken=opstack.pop()
            while toptoken != '(':
                postfixlist.append(toptoken)
                toptoken = opstack.pop()

        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                postfixlist.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfixlist.append(opstack.pop())
    
    return ' '.join(postfixlist)

print(infixTopostfix('A * B + C * D'))
print(infixTopostfix('( A + B ) * C - ( D - E ) * ( F + G )'))


#后缀表达式求值

def postfixeval(postfixexpr):
    operandstack = Stack()
    tokenlist = postfixexpr.split()

    for token in tokenlist:
        if token in '0123456789':
            operandstack.push(int(token))

        else:
            operand2 = operandstack.pop()
            operand1 = operandstack.pop()
            result = domath(token, operand1, operand2)
            operandstack.push(result)

    return operandstack.pop()

def domath(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

print(postfixeval('7 8 + 3 2 + /'))