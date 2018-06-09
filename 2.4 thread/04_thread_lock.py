import threading
import time

# for循环次数，最后balance不等于0的机会越大
balance = 0
def change_it(n):
    global balance
    # 上锁，只有获取锁后才能继续执行，在获取到锁之前，阻塞等待
    lock.acquire()
    balance = balance + n
    balance = balance - n
    # 释放锁
    lock.release()

def run_thread(n):
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(1000000):
        change_it(n)

lock = threading.Lock()
t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)