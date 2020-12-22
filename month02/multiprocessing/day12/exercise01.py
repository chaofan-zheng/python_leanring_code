"""
练习1：大文件拆分
编写程序完成
将一个文件平均拆分为两个部分,分别为
上半部分和下半部分，要求拆分过程同步执行
"""
from multiprocessing import Process
import os

filename = "./timg.jfif"
size = os.path.getsize(filename)

# 如果在父进程打开，子进程直接使用
# 那么父子进程公用一个文件偏移量
# fr = open(filename, 'rb')

# 复制文件上半部分
def top():
    fr = open(filename,'rb')
    fw = open("top.jpg",'wb')
    n = size // 2 # 要拷贝n个字节
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制文件下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open("bot.jpg", 'wb')
    fr.seek(size // 2)  # 从中间开始
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

# 创建进程完成
p = Process(target=top)
p.start()

bot() # 父进程负责下半部分

p.join()