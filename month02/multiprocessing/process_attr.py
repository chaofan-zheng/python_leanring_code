"""
进程模块使用，基础示例
"""
# 不能选带横线的
from multiprocessing import Process
from time import sleep

a = 1


# 进程执行函数
def fun():
    print("开始运行第一个进程")
    print(p.is_alive())
    sleep(2)
    print("第一个进程结束")
    # print(p.is_alive())


# 实例化进程对象
p = Process(target=fun, name="Aid",daemon=True)

p.start()
print("第二个进程开始运行")
sleep(1)
print("第二个进程结束")
print(p.name)
print(p.pid)
print(p.is_alive())

