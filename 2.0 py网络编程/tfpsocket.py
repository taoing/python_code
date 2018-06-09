import socket
import sys
import struct

if len(sys.argv) != 3:
    print('-'*30)
    print('tips:')
    print('python xxx.py 192.168.2.100 test.jpg')
    print('-'*30)
    exit()
else:
    ip = sys.argv[1]
    req_file = sys.argv[2]

tftpsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#读取请求
req = struct.pack('!H%dsb5sb' % len(req_file),1,req_file.encode('utf-8'),0,b'octet',0)
server_addr = (ip,69)
tftpsocket.sendto(req,server_addr)
data_num = 0
recvfile = open(req_file,'ab')

while True:
    recvdata,send_addr = tftpsocket.recvfrom(1024)
    data4 = struct.unpack('!HH',recvdata[:4])
    data_code = data4[0]
    current_num = data4[1]
    if data_code == 3:
        data_num = data_num + 1
        #2字节能表示的最大编号为65535
        if data_num == 65536:
            data_num = 0
        #接收数据
        if current_num == data_num:
            recvfile.write(recvdata[4:])
            print('第%d次接收到数据' % current_num)
            ackdata = struct.pack('!HH',4,current_num)
            tftpsocket.sendto(ackdata,send_addr)

        #如果接收到的数据小于516字节，下载完成
        if len(recvdata) < 516:
            recvfile.close()
            print('下载完成！')
            break

    if data_code == 5:
        print('error code:%d' % current_num)
        print('error message:%s' % recvdata[4:].decode('utf-8'))
        break

tftpsocket.close()
