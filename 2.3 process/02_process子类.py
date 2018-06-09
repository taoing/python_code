from multiprocessing import Process
import time

class MyProcess(Process):
    #重写run()方法
    def run(self):
        while True:
            print('start()方法里会调用run()方法')
            time.sleep(1)

if __name__ == '__main__':
    p1 = MyProcess()
    p1.start()

    while True:
        print('---main---')
        time.sleep(1)