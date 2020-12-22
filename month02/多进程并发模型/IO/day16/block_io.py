"""
非阻塞IO演示
"""

from socket import *
from time import sleep,ctime

# 创建tcp套接字
sockfd = socket()
sockfd.bind(("0.0.0.0",8888))
sockfd.listen(5)

file = open("my.log",'a') # 日志文件

# 设置套接字为非阻塞
# sockfd.setblocking(False)

# 设置超时检测
sockfd.settimeout(3)

while True:
    print("Waiting for connect")
    # 阻塞位置
    try:
        connfd,addr = sockfd.accept()
        print("Connect from",addr)
    except BlockingIOError as e:
        # 没有客户端连接
        sleep(2)
        msg = "%s: %s\n"%(ctime(),e)
        file.write(msg)
    except timeout as e:
        msg = "%s: %s\n" % (ctime(), e)
        file.write(msg)
    else:
        data = connfd.recv(1024)
        print(data.decode())
