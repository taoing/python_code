from multiprocessing import Process, Queue
import time
import os
import random

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get()
        print('Get %s from queue' % value)

if __name__ == '__main__':
    print('Parent process %s...' % os.getpid())
    # 创建进程数最大为4的进程池
    q = Queue(3)
    pw = Process(target = write, args = (q,))
    pr = Process(target = read, args = (q,))
    pw.start()
    pr.start()
    pw.join()
    # pr是死循环，强制终止
    pr.terminate()
    print('All process done.')