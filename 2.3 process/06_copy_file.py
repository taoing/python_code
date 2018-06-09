#coding=utf-8

from multiprocessing import Manager, Pool
import time
import os
import random

# copy file
def copy_file(file_name, old_folder_name, new_folder_name):
    print('Start copy: %s...' % file_name)
    read_file = open('./' + old_folder_name +'/' + file_name, 'rb')
    write_file = open('./' + new_folder_name + '/' + file_name, 'wb')
    # 读取文件内容写入到新文件中，即是copy
    write_file.write(read_file.read())
    read_file.close()
    write_file.close()

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
    for file_name in file_list:
        pool.apply_async(copy_file, args = (file_name, old_folder_name, new_folder_name))
    # 主进程等待所有进程结束
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()