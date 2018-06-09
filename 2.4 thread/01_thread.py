import threading
import time

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
th = threading.Thread(target = loop)
th.start()
# th.join()方法让主线程阻塞，等待子线程执行完后再向下执行
th.join()
print('thread %s ended.' % threading.current_thread().name)