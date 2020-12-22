"""
在之前pool的练习中，
在拷贝过程中不断显示拷贝的百分比
"""
"""
拷贝一个目录，假设目录下有若干普通文件，需要编写程序，将该目录拷贝一份。注意拷贝过程中需要多份文件同时拷贝
os.mkdir("文件夹名") # 创建文件夹
os.listdir("/home/tarena/FTP") # 获取文件夹里面文件的列表
"""

from multiprocessing import *
import os

filename_list = os.listdir("../day12")
os.mkdir("FTP")

q = Queue()


def get_totalsize():
    totalsize = 0
    for filename in filename_list:
        totalsize += os.path.getsize(f"../day12/{filename}")
    return totalsize


total_size = get_totalsize()


def copy_file(old_file_name):
    old_file = open(f"../day12/{old_file_name}", "rb")
    new_file = open(f"FTP/{old_file_name}", "wb")
    while True:
        content = old_file.read(64)
        if not content:
            break
        else:
            size = new_file.write(content)
            q.put(size)
    old_file.close()
    new_file.close()


pool = Pool()

for filename in filename_list:
    pool.apply_async(copy_file, args=(filename,))  # 必须要是元组

copied_size = 0
while copied_size<total_size:
    copied_size += q.get()
    percentage = copied_size/total_size
    print("复制百分比",percentage)


pool.close()
pool.join()
