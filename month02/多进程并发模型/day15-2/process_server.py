"""
基于多进程的网络并发模型
重点代码 ！！

创建tcp网络套接字
等待客户端连接
客户端连接，则创建新的进程具体处理客户端请求
主进程继续等待其他客户端连接
如果客户端退出，则销毁对应的进程
"""
from socket import *
from multiprocessing import Process
import sys

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


# 子进程处理客户端请求 入口
def handle(connfd):
    # 测试与客户端配合
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
    connfd.close()


def main():
    # 创建套接字
    tcp_socket = socket()
    tcp_socket.bind(ADDR)
    tcp_socket.listen(5)

    # 循环连接客户端
    while True:
        try:
            connfd, addr = tcp_socket.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            tcp_socket.close()
            sys.exit("服务结束")

        # 创建子进程
        p = Process(target=handle, args=(connfd,), daemon=True)
        p.start()  # 启动进程


if __name__ == '__main__':
    main()
