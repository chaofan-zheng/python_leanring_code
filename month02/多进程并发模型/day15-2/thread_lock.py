"""
线程同步互斥锁
"""
from threading import Thread, Lock

lock = Lock() # 锁对象

a = b = 1


def fun():
    while True:
        lock.acquire() # 上锁
        if a != b:
            print("a = %d,b = %d" % (a, b))
        lock.release() # 解锁

t = Thread(target=fun)
t.start()

while True:
    with lock:  # 上锁
        a += 1
        b += 1
                # 自动解锁

t.join()