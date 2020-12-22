"""
event 线程同步互斥方法
"""
from threading import Thread,Event

# 消息传递
msg = None
e = Event()

def 杨子荣():
    print("杨子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set() # 解除阻塞

t = Thread(target=杨子荣)
t.start()

print("说对口令才是自己人")
# 主线程去验证
e.wait() # 阻塞等待
if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神你是对的人")
else:
    print("打死他。。。无情啊。。")

t.join()


