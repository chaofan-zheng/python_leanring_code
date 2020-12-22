"""
event 线程同步互斥方法
"""
from threading import Thread, Event

# msg = None
#
#
# def hello():
#     print("拜见山头")
#     global msg
#     msg = "天王盖地虎"
#
#
# t = Thread(target=hello)
# t.start()
#
# # 主进程去验证
# if msg == "天王盖地虎":
#     print("宝塔镇河妖")
# else:
#     print("杀了他")
# 这样子会不确定

msg = None
e = Event()


def hello():
    print("拜见山头")
    global msg
    msg = "天王盖地虎"
    e.set()  # 解除阻塞


t = Thread(target=hello)
t.start()

e.wait()
# 主进程去验证
if msg == "天王盖地虎":
    print("宝塔镇河妖")
else:
    print("杀了他")
