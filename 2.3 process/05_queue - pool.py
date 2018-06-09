from multiprocessing import Manager, Pool
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
        if not q.empty():
            value = q.get()
            print('Get %s from queue' % value)
            time.sleep(1)
        else:
            break

if __name__ == '__main__':
    print('Parent process %s...' % os.getpid())
    # 创建进程数最大为4的进程池
    q = Manager().Queue(3)
    pool = Pool(4)
    pool.apply_async(write, args = (q,))
    pool.apply_async(read, args = (q,))
    pool.close()
    pool.join()
    print('All process done.')