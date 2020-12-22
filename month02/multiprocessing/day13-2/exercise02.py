"""
练习2： 拷贝一个目录
假设目录下有若干普通文件,需要编写程序
将该目录拷贝一份，注意拷贝过程中需要
多文件同时拷贝（使用进程池完成）

os.mkdir("FTP")
os.listdir("/home/tarena/FTP")
"""
from multiprocessing import Pool,Queue
import os

q = Queue() # 生成消息队列

# 进程池事件 将文件从原文件夹拷贝到新文件夹
def copy(filename, old, new):
    fr = open(old + '/' + filename, 'rb')
    fw = open(new + '/' + filename, 'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data)
        q.put(n) # 将已经拷贝的大小给父进程
    fr.close()
    fw.close()

# 获取文件夹大小
def total_size(dir):
    res = 0
    for file in os.listdir(dir):
        res += os.path.getsize(dir+'/'+file)
    return res

# 创建进程池，调用函数作为进程池执行事件
def main(old_folder):
    # 创建新文件夹
    new_folder = old_folder.split("/")[-1]
    os.mkdir(new_folder)

    # 获取文件里列表
    file_list = os.listdir(old_folder)

    size = total_size(old_folder)

    # 创建进程池
    pool = Pool()
    # 循环添加事件
    for file in file_list:
        pool.apply_async(copy, args=(file, old_folder, new_folder))

    pool.close()

    # 求拷贝的百分比
    copy_size = 0
    while copy_size < size:
        copy_size += q.get()  # 累加
        print("已拷贝%.2f%%" % (copy_size/size*100))

    pool.join()


if __name__ == '__main__':
    main("/home/tarena/FTP")
