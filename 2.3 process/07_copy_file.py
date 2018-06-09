#coding=utf-8

from multiprocessing import Manager, Pool
import time
import os
import random

# copy file
def copy_file(file_name, old_folder_name, new_folder_name, queue):
    read_file = open('./' + old_folder_name +'/' + file_name, 'rb')
    write_file = open('./' + new_folder_name + '/' + file_name, 'wb')
    # 读取文件内容写入到新文件中，即是copy
    write_file.write(read_file.read())
    read_file.close()
    write_file.close()

    queue.put(file_name)

def main():
    # 输入要copy的文件夹名
    old_folder_name = input('请输入copy文件夹:')
    # 复制后文件夹名
    new_folder_name = old_folder_name + '_2'
    # 创建文件夹
    os.mkdir(new_folder_name)
    # 获取copy文件夹中的文件列表
    file_list = os.listdir('./' + old_folder_name)
    # 创建多进程copy文件
    pool = Pool(5)
    queue = Manager().Queue()
    for file_name in file_list:
        pool.apply_async(copy_file, args = (file_name, old_folder_name, new_folder_name, queue))

    num = 0
    file_num = len(file_list)
    while num < file_num:
        queue.get()
        num = num + 1
        copyrate = num/file_num
        print('\rCopy rate: %.2f %%...' % (copyrate*100), end = '')
    print('\r\nCopy end!')

if __name__ == '__main__':
    main()