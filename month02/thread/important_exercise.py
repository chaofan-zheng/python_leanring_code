"""
使用两个线程，
一个打印1-52 这52个数字
一个打印a-z这些字母
两个线程一起执行，要求打印出来的顺序为
12A34B...5152Z
多为面试题的笔试题
"""

from threading import Lock, Thread
import time

lock01 = Lock()
lock02 = Lock()


def print_int():
    for i in range(1, 52, 2):
        lock01.acquire()
        print(i)
        print(i + 1)
        lock02.release()


def print_alpha():
    for i in range(65, 91):
        lock02.acquire()
        print(chr(i))
        lock01.release()


t1 = Thread(target=print_alpha)
t2 = Thread(target=print_int)
lock02.acquire()
t2.start()
t1.start()

