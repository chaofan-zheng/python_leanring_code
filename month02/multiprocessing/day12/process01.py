"""
进程模块使用 基础示例
"""
import multiprocessing
from time import sleep

a = 1

# 进程执行函数
def fun():
    print("开始运行一个进程喽")
    sleep(2)
    global a
    print("a =",a)
    a = 10000
    print("终于完成事情结束喽")


# 实例化进程对象
p = multiprocessing.Process(target=fun)

# 启动进程  此刻产生进程，运行fun函数
p.start()

print("我也要做点事")
sleep(3)
print("我也做完喽。。。")

# 阻塞等待回收进程
p.join()

print("a:",a) # 1

