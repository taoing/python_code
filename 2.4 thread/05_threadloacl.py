import threading

global_local = threading.local()

def process_student():
    std = global_local.student
    print('%s in %s' % (std, threading.current_thread().name))

def process_thread(name):
    global_local.student = name
    process_student()

t1 = threading.Thread(target = process_thread, args = ('xiaoming',), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('xiaohua',), name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()