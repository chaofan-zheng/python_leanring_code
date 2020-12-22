"""
让客户端退出后，服务端不退出，继续可以连接下一个客户端
但是无法连接多个客户端
"""
from socket import *
from time import sleep

tcp_socket = socket()
tcp_socket.bind(("0.0.0.0", 6956))
tcp_socket.listen(5)

while True:
    print("等待客户端链接")
    connfd, addr = tcp_socket.accept()  # 创建新的套接字
    print("连接上客户端：", addr)
    while True:
        data = connfd.recv(5)
        if data.decode() == "##" or data == "":  #
            connfd.close()
            break
        print("Recv:", data.decode())
        n = connfd.send(b"OK")
        sleep(1)
# 关闭套接字
tcp_socket.close()
