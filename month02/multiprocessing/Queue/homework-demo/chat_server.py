"""
Author: Levi
Email: lvze@tedu.cn
Time : 2020-12-15
Env : Python3.6

socket and process exercise
"""
from socket import *
from multiprocessing import Process

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 存储用户信息的结构 {name:address}
user = {}


def do_login(sock, name, address):
    if name in user or "管理" in name:
        sock.sendto(b"FAIL", address)
    else:
        sock.sendto(b"OK", address)
        # 先通知其他人
        msg = "欢迎 %s 进入聊天室" % name
        for key, value in user.items():
            sock.sendto(msg.encode(), value)
        # 加入用户
        user[name] = address


def do_chat(sock, name, content):
    msg = "%s : %s" % (name, content)
    for key, value in user.items():
        # 不是本人
        if key != name:
            sock.sendto(msg.encode(), value)


def do_exit(sock, name):
    del user[name]  # 从字典删除
    msg = "%s 退出了聊天" % name
    # 通知其他人
    for key, value in user.items():
        sock.sendto(msg.encode(), value)


def handle(sock):
    # 循环接收用户请求
    while True:
        data, addr = sock.recvfrom(1024)
        tmp = data.decode().split(' ', 2)
        # 根据请求，分情况讨论
        if tmp[0] == "LOGIN":
            # tmp->[LOGIN,name]
            do_login(sock, tmp[1], addr)
        elif tmp[0] == "CHAT":
            # tmp->[CHAT,name,xxxx]
            do_chat(sock, tmp[1], tmp[2])
        elif tmp[0] == "EXIT":
            # tmp->[EXIT,name]
            do_exit(sock, tmp[1])


# 搭建总体逻辑结构
def main():
    # 创建udp套接字
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)

    p = Process(target=handle, args=(sock,), daemon=True)
    p.start()

    # 父进程发送管理员消息
    while True:
        content = input("管理员消息：")
        if content == "exit":
            break
        msg = "CHAT 管理员消息 "+content
        #　发送给子进程
        sock.sendto(msg.encode(),ADDR)


if __name__ == '__main__':
    main()  # 启动
