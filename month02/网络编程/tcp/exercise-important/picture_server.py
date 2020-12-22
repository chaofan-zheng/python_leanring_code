"""
上传头像的练习
客户端需要将自己的头像上传给服务端
在服务端以当前日期保存为jpg格式
提示：图片如果大的话，需要一条一条读取发送
"""
from socket import *
import time

tcp_socket = socket()
tcp_socket.bind(("0.0.0.0", 6955))
tcp_socket.listen(5)

while True:
    print("等待客户端链接")
    connfd, addr = tcp_socket.accept()  # 创建新的套接字
    print("连接上客户端：", addr)
    file_name = time.time()
    file = open("%s.jpeg" % file_name, "ab+")
    while True:
        data = connfd.recv(1024)
        if not data:  #
            connfd.close()
            file.close()
            break
        file.write(data)

# 关闭套接字
