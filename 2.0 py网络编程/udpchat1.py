import socket
from threading import Thread
from time import ctime

udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.bind(('127.0.0.1',8100))
destip = '127.0.0.1'
destport = 8101

#接收数据
def recvdata():
    while True:
        recvinfo = udpsocket.recvfrom(1024)
        data,addr = recvinfo
        print('>>>:{0} from {1} : {2}'.format(ctime(),str(addr),data.decode('utf-8')))

#发送数据
def senddata():
    while True:
        sendinfo = input('<<<:')
        udpsocket.sendto(sendinfo.encode('utf-8'),(destip,destport))

def main():
    tr = Thread(target = recvdata)
    ts = Thread(target = senddata)
    tr.start()
    ts.start()
    tr.join()
    ts.join()

if __name__ == '__main__':
    main()