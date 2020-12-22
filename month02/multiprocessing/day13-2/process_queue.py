"""
进程间通信示例
"""
from multiprocessing import Process,Queue

q = Queue() # 消息队列

# 解决问题 分之任务解决器
def handle():
    while True:
        res = q.get()
        try:
            # 将res作为语句执行
            eval(res)
        except:
            print("语法有误")

p = Process(target=handle,daemon=True)
p.start()

# 任务主线，随时提取问题需要解决
while True:
    print("父进程一直干活")
    res = input("发布任务:")
    if res == "exit":
        break
    q.put(res) # 存入队列
