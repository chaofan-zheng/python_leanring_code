"""
进程属性
"""
from multiprocessing import Process
from time import sleep

# 进程执行函数
def fun():
    print("开始运行一个进程喽")
    sleep(2)
    print("终于完成事情结束喽")


# 实例化进程对象
p = Process(target=fun,name="Aid",daemon=True)
p.start()

print(p.name)
print(p.pid)
print(p.is_alive())



