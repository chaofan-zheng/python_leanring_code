"""
* 粘包问题
编写程序完成，将一个文件平均拆分为两个部分，分别为上半部分和下半部分，要求拆分过程同步执行
os.path.getsize()
不建议一次性的读写
难点：上半部分怎么复制到一半停止
"""
import os
from multiprocessing import Process

file_name = "dict.txt"
file_size = os.path.getsize(file_name)
a = file_size // 2
# file = open(file_name, "rb")  # 只有父进程会运行这个代码，但是内存里也会有这个file 但是两个文件公用一个偏移量所以不能这么写


def top():
    file = open(file_name, "rb")
    target_file = open("file02", "wb")
    while True:
        position = target_file.tell()
        if a - position <= 64:
            data = file.read(a - position)
        else:
            data = file.read(64)
        if not data:
            break
        target_file.write(data)
    file.close()
    target_file.close()


def bottom():
    file = open(file_name, "rb")
    target_file01 = open("file01", "wb")
    file.seek(a)
    while True:
        data = file.read(64)
        if not data:
            break
        target_file01.write(data)
    file.close()
    target_file01.close()


p = Process(target=bottom)
p.start()
top()
p.join()
