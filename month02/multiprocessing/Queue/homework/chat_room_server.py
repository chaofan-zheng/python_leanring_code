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


class Server:
    def __init__(self):
        self.__udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.__list_name = []
        self.__addr_list = []
        self.__udp_socket.bind(("0.0.0.0", 8888))  # 自动创建套接字

    def __login(self, data, addr):
        """
        进行登录验证
        :param data:
        :param addr:
        :return:
        """
        if data.decode() in self.__list_name:
            self.__udp_socket.sendto("失败".encode(), addr)
        else:
            self.__list_name.append(data.decode())
            self.__addr_list.append(addr)
            self.__udp_socket.sendto("1".encode(), addr)

    #  封装发送消息给所有人的函数
    def __sent_all(self, data):
        for addr in self.__addr_list:
            self.__udp_socket.sendto(data, addr)

    def main(self):
        while True:
            data, addr = self.__udp_socket.recvfrom(1024)
            if addr in self.__addr_list:
                self.__sent_all(data)
            else:
                self.__login(data, addr)


server = Server()
server.main()
