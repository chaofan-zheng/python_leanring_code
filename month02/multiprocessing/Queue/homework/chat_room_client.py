"""
聊天室
1. 有人进入聊天室需要输入姓名，姓名不能重复
2. 有人进入聊天室时，其他人会收到通知: xxx进入了聊天室
3. 一个人发消息，其他人会收到: XXX:xxxxx
4. 有人退出聊天室，则其他人也会收到同志:XXX退出了聊天室
5. 扩展功能：服务器可以向所有用户发送公告：管理员消息：xxxxxx

技术分析
功能拆分和封装结构的决定
网络通讯协议设定
分功能逻辑讨论
架构 --> 框架 --> 逻辑结构模型
"""
from socket import *
from multiprocessing import *
import sys


class Client:
    ADDR = ("127.0.0.1", 8888)

    def __init__(self):
        self.__udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.name = ""

    def __login(self):
        while True:
            self.name = input("请输入昵称（不能重复）")
            self.__udp_socket.sendto(self.name.encode(), Client.ADDR)
            data, addr = self.__udp_socket.recvfrom(1024)
            if data.decode() == "失败":
                continue
            else:
                break
        self.__udp_socket.sendto(f"{self.name}进入聊天室".encode(), Client.ADDR)

    # 一直循环，回车控制退出
    def __send_message(self):
        while True:
            content = input(">>")
            msg = self.name + ": " + content
            if not content:
                self.__client_quit()
                break  # 使用回车退出
            self.__udp_socket.sendto(msg.encode(), Client.ADDR)

    def __client_quit(self):
        self.__udp_socket.sendto(f"{self.name}退出聊天室".encode(), Client.ADDR)
        self.__udp_socket.close()
        sys.exit()

    # 接受消息作为子进程
    # 一直循环，父进程退出才退出
    def __receive_message(self):
        while True:
            data, addr = self.__udp_socket.recvfrom(1024)
            print(data.decode())

    def main(self):
        self.__login()
        p = Process(target=self.__receive_message, daemon=True)
        p.start()
        self.__send_message()


client = Client()
client.main()
