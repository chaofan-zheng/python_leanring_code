"""
创建tcp套接字
等待客户端连接
客户端连接，则创建子进程
"""
from socket import *
from multiprocessing import Process
import sys

HOST = "0.0.0.0"
PORT = 6955
ADDR = (HOST, PORT)


def main():
    tcp_socket = socket()
    tcp_socket.bind(ADDR)
    tcp_socket.listen(5)
    # 循环链接客户端
    while True:
        try:
            connfd, addr = tcp_socket.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            tcp_socket.close()
            sys.exit()
        p = Process(target=handle, args=(connfd,), daemon=True)
        p.start()


# 子进程的统一处理方案
def handle(connfd):
    # 测试与客户端的配合
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
    connfd.close()


if __name__ == '__main__':
    main()
