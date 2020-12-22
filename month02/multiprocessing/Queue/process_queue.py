"""
进程间通信示例
"""
from multiprocessing import Queue, Process
q = Queue()


# 解决问题 分支任务解决器
def handle():
    while True:
        res = q.get()
        try:

            eval(f"{res}")  # 执行这个语句
        except Exception:
            print("程序有误")


p = Process(target=handle, daemon=True)
p.start()

# 任务主线，随时提出任务，等待解决
while True:
    res = input("请输入语句：")
    if not res:
        break
    q.put(res)
