"""
锁示例
"""
from threading import Thread, Event, Lock

# msg = None
# e = Event()
#
# def hello():
#     print("拜见山头")
#     global msg
#     msg = "天王盖地虎"
#     lock.release()  # 解除阻塞
#
#
# lock = Lock()
# lock.acquire()
# t = Thread(target=hello)
# t.start()
#
# lock.acquire()  # 验证前阻塞一下
# # 主进程去验证
# if msg == "天王盖地虎":
#     print("宝塔镇河妖")
# else:
#     print("杀了他")

a = b = 1


def fun():
    while True:
        lock.acquire()
        if a != b:
            print(f"a={a},b={b}")
        lock.release()


lock = Lock()
t = Thread(target=fun)
t.start()
while True:
    lock.acquire()
    a += 1
    b += 1
    lock.release()

# 问,没有锁a,b会打印出来吗？答：会
# 把对共享资源的操作用锁包起来
# 两个锁住的代码部分，同一时刻只能有一个部分的代码在执行
