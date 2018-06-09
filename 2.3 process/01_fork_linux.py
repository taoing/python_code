# 多次fork
import os

pid = os.fork()
if pid == 0:
    print('---1---')
else:
    print('---2---')
    pid2 = os.fork()
    if pid2 == 0:
        print('---21---')
    else:
        print('---22---')

# 3次fork
import os
os.fork()
os.fork()
os.fork()

print('---executing---')