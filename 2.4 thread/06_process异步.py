from multiprocessing import Pool
import os
import time

def test():
    print('subprocess %s is running, parrent process is %s' % (os.getpid(), os.getppid()))
    time.sleep(1)
    print('subprocess ended and return something.')
    return 'my pid %s' % os.getpid()

# 回调函数,其参数为函数test运行后的返回值
# test函数所在子进程执行完之后,父进程立即开始执行回调函数
def test2callback(args):
    print('in callback function, process %s is running...' % os.getpid())
    print('my args is %s' % args)

def main():
    print('parrent process %s is running...' % os.getpid())
    pool = Pool(4)
    pool.apply_async(func = test, callback = test2callback)

    for i in range(10):
        print('%s in (%s)' % (i, os.getpid()))
        time.sleep(0.5)

if __name__ == '__main__':
    main()