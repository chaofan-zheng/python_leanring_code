"""
线程基础示例 1
"""
import threading
from time import sleep
import os

a = 1

# 线程执行函数
def music():
    global a
    print("a = ",a)
    a = 10000
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放:黄河大合唱")

# 实例化线程对象
t = threading.Thread(target=music)

# 启动线程
t.start()

for i in range(4):
    sleep(1)
    print(os.getpid(),"播放：葫芦娃")

# 阻塞等待线程结束
t.join()
print("a:",a) # ?
