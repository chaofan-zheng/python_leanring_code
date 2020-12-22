from socket import *
from multiprocessing import Process
import sys

ADDR = ("127.0.0.1", 8888)
udp_socket = socket(AF_INET, SOCK_DGRAM)
# udp_socket.bind(("0.0.0.0",6955)) # udp套接字在一段时间不链接后，会自动重新分配端口，所以需要绑定


def login():
    while True:
        name = input("请输入昵称（不能重复）")
        msg = "LOGIN" + "##" + name
        udp_socket.sendto(msg.encode(), ADDR)
        data, addr = udp_socket.recvfrom(1024)
        if data.decode() == "0":
            print("昵称已存在，请重新输入")
            continue
        else:
            print("你已进入聊天室")
            return name


def chat(name):
    p = Process(target=receive, daemon=True)
    p.start()
    while True:
        try:
            content = input(">>>>")
        except KeyboardInterrupt:
            print("程序退出")
            content = ""  # 如果阻塞在input ctrl c 退出的话，调用my_exit函数
        if not content:
            my_exit(name)
        msg = "CHAT" + "##" + f"{name}:" + content
        udp_socket.sendto(msg.encode(), ADDR)
        print("你发送了一条消息")


def my_exit(name):
    msg = "EXIT" + "##" + name
    print("您已退出聊天室")
    udp_socket.sendto(msg.encode(), ADDR)
    sys.exit()


def receive():  # 作为子进程，收到消息然后打印出收到的内容
    while True:
        data, addr = udp_socket.recvfrom(1024)
        print("\n" + data.decode() + "\n>>>", end="")


def main():
    name = login()
    chat(name)


if __name__ == '__main__':
    main()
