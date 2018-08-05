# -*- coding: utf-8 -*-

# 二分查找

def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first+last) // 2
        if alist[midpoint] == item:
            found = True;
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

testlist = [0, 1, 2, 8, 13, 19, 32, 42]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))

# 递归
def binary_search_r(alist, item):
    if len(alist) == 0:
        return False

    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search_r(alist[:midpoint], item)
            else:
                return binary_search_r(alist[midpoint+1:], item)

testlist = [0, 1, 2, 8, 13, 19, 32, 42]
print(binary_search_r(testlist, 3))
print(binary_search_r(testlist, 13))

# 递归改进
def binary_search_r_helper(alist, start, end, item):
    if start > end:
        return False
    else:
        midpoint = (start+end) // 2
        if item == alist[midpoint]:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search_r_helper(alist, start, midpoint-1, item)
            else:
                return binary_search_r_helper(alist, midpoint+1, end, item)

def binary_search_r2(alist, item):
    if len(alist) == 0:
        return False
    else:
        return binary_search_r_helper(alist, 0, len(alist)-1, item)

testlist = [0, 1, 2, 8, 13, 19, 32, 42]
print(binary_search_r2(testlist, 3))
print(binary_search_r2(testlist, 13))
print(binary_search_r2(testlist, 0))
print(binary_search_r2(testlist, 42))