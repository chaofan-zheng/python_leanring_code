from socket import *
from multiprocessing import Process

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 存储用户信息的结构 {name:address}
user = {}


def sent_all(udp_socket, content, addr):
    for key, value in user.items():
        if value == addr:
            continue
        else:
            udp_socket.sendto(content.encode(), value)


def login(udp_socket, name, addr):
    if name in user:
        udp_socket.sendto(b"0", addr)  # 0代表失败

    else:
        udp_socket.sendto(b"1", addr)  # 1代表成功
        user[name] = addr  # 先发，再增加，这样登录进来的人就不会收到
        sent_all(udp_socket, f"欢迎{name}进入聊天室", addr)


# def chat(udp_socket, content, addr):
#     sent_all_except(udp_socket, content, addr)

def my_exit(udp_socket, name, addr):
    del user[name]
    content = f"{name}退出了聊天"
    sent_all(udp_socket, content, addr)


def handle(udp_socket):
    while True:
        data, addr = udp_socket.recvfrom(1024)
        msg = data.decode()
        head, content = msg.split("##")[0], msg.split("##")[1]
        if head == "LOGIN":
            login(udp_socket, content, addr)
            continue
        if head == "CHAT":
            sent_all(udp_socket, content, addr)
            continue
        if head == "EXIT":
            my_exit(udp_socket, content, addr)


def manager(udp_socket):
    while True:
        content = input("请发布管理员通告")
        msg = "CHAT##管理员消息：" + content  # 加上CHAT
        udp_socket.sendto(msg.encode(), ADDR)  # 应该给子进程发


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(ADDR)
    p = Process(target=handle, args=(udp_socket,))
    p.start()
    manager(udp_socket)


if __name__ == '__main__':
    main()
