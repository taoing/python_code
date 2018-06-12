# -*- coding: utf-8 -*-

# 快速排序

def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)
def quick_sort_helper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quick_sort_helper(alist, first, splitpoint-1)
        quick_sort_helper(alist, splitpoint+1, last)
def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] > pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

# alist = [35,21,56,27,11,47,98,85,57]
# quick_sort(alist)
# print(alist)

import random
import time
random_list = random.sample(range(3000000), 1000000)
blist = random_list[:]
print('list的长度:', len(blist))
start = time.time()
quick_sort(blist)
end = time.time()
print('quick sort complete, use time: {}'.format(end-start))