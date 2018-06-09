import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(1,4):
            info = 'I am is %s --- %s' % (self.name, i)
            print(info)
            time.sleep(1)

if __name__ == '__main__':
    t = MyThread()
    t.start()
    t.join()