"""
chat room 客户端程序
"""
from socket import *
from multiprocessing import Process
import sys

# 服务器地址
SERVER_ADDR = ("117.78.6.6", 8888)


#  子进程接收
def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024 * 10)
        # 整理打印内容
        msg = "\n" + data.decode() + "\n发言："
        print(msg, end="")


# 父进程
def send_msg(sock, name):
    while True:
        try:
            content = input("发言：")
        except KeyboardInterrupt:
            content = "exit"
        # 退出
        if content == 'exit':
            msg = "EXIT " + name
            sock.sendto(msg.encode(), SERVER_ADDR)
            sys.exit("您已退出聊天")
        # 发送请求
        msg = "CHAT %s %s" % (name, content)
        sock.sendto(msg.encode(), SERVER_ADDR)


def do_chat(sock, name):
    p = Process(target=recv_msg, args=(sock,), daemon=True)
    p.start()
    send_msg(sock, name)  # 发送消息


def do_login(sock):
    while True:
        name = input("请输入昵称:")
        msg = "LOGIN " + name
        sock.sendto(msg.encode(), SERVER_ADDR)
        # 等待服务端结果
        result, addr = sock.recvfrom(128)
        if result == b'OK':
            print("您已进入聊天室")
            return name
        else:
            print("该昵称已存在")


# 启动函数
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("0.0.0.0",55660))

    # 进入聊天室 得到登陆者
    name = do_login(sock)

    # 聊天
    do_chat(sock, name)


if __name__ == '__main__':
    main()
