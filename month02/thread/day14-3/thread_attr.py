"""
线程属性信息设置
"""
from threading import Thread
from time import sleep

# 线程执行函数
def music():
    for i in range(3):
        sleep(2)
        print("播放:黄河大合唱")

# 实例化线程对象
t = Thread(target=music)

# 在start前设置
t.setDaemon(True)

t.start()

t.setName("tarena")
print(t.getName())
print(t.is_alive())  # 生命周期




