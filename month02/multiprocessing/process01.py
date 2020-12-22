"""
进程模块使用，基础示例
"""
# 不能选带横线的
import multiprocessing
from time import sleep

a = 1


# 进程执行函数
def fun():
    print("开始运行第一个进程")
    sleep(2)
    global a
    print(a)
    a = 100  # 打印子进程a
    print("第一个进程结束")


# 实例化进程对象
p = multiprocessing.Process(target=fun)

# 启动进程 此刻才会产生进程，运行fun函数
p.start()
print("第二个进程开始运行")
sleep(3)
print("第二个进程结束")
# 阻塞等待回收进程
p.join()
print(a)  # 打印父进程的a
