from multiprocessing import Pool
import time
import os
import random

def worker(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f s.' % (name, (end-start)))

if __name__ == '__main__':
    print('Parent process %s...' % os.getpid())
    # 创建进程数最大为4的进程池
    pool = Pool(4)
    for i in range(1,11):
        pool.apply_async(worker, args=(i,))
    print('Waiting for all subprocesses done...')
    # 关闭进程池，不能再添加新进程
    pool.close()
    # 让主进程等待所有子进程执行完再向下执行
    pool.join()
    print('All process done.')