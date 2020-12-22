from socket import *
from time import *

# 创建套接字
sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)
file = open("mylog.txt", "w")
# 设置套接字为非阻塞
# sockfd.setblocking(False)
sockfd.settimeout(2)
while True:
    print("Waiting for connect")
    # 阻塞位置
    try:
        connfd, addr = sockfd.accept()  # 如果没有人连接，就不阻塞了，直接报错
        msg = "%s:%s\n" % (ctime(), f"Connect from {addr}")
        file.write(msg)
        print("Connect from ", addr)
    except BlockingIOError as e:
        sleep(2)
        msg = "%s:%s\n" % (ctime(), e)
        file.write(msg)
    except timeout as e:
        msg = "%s:%s\n" % (ctime(), e)
        file.write(msg)
    else:
        data = connfd.recv(1024)
        print(data.decode())
