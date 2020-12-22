"""
练习3：上传头像的练习
假设客户端需要将自己的头像上传给服务端
请编写程序完成该工作，在服务端以当前日期
保存为jpg格式   2020-12-10.jpg
"""
from socket import *


class Client:
    def __init__(self):
        self.tcp_socket = socket()
        self.ADDR = ("127.0.0.1", 7777)

    def send_imag(self, picture_addr):
        self.tcp_socket.connect(self.ADDR)
        file = open(f"{picture_addr}", "rb")
        while True:
            content = file.read(1024)
            if not content:
                break
            self.tcp_socket.send(content)
        file.close()
        self.tcp_socket.close()

if __name__ == '__main__':
    msg = input("请输入要拷贝的文件名加路径")
    client = Client()
    client.send_imag(msg)