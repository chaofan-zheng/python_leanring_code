"""
拷贝一个目录，假设目录下有若干普通文件，需要编写程序，将该目录拷贝一份。注意拷贝过程中需要多份文件同时拷贝
os.mkdir("文件夹名") # 创建文件夹
os.listdir("/home/tarena/FTP") # 获取文件夹里面文件的列表
"""
from multiprocessing import *
import os

filename_list = os.listdir("../day12")
os.mkdir("FTP")


def copy_file(old_file_name):
    old_file = open(f"../day12/{old_file_name}", "rb")
    new_file = open(f"FTP/{old_file_name}", "wb")
    while True:
        content = old_file.read(64)
        if not content:
            break
        else:
            new_file.write(content)
    old_file.close()
    new_file.close()


pool = Pool()

for filename in filename_list:
    pool.apply_async(copy_file, args=(filename,))  # 必须要是元组

pool.close()
pool.join()
