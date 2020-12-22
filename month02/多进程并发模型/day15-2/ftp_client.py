"""
文件服务器 客户端
"""
from socket import *


class FTPHandle:
    server_address = ('127.0.0.1', 8888)

    def __init__(self):
        self.sock = self.connect_server()

    def connect_server(self):
        sockfd = socket()
        sockfd.connect(FTPHandle.server_address)
        return sockfd

    def do_list(self):
        # 发送请求
        self.sock.send(b"LIST")
        # 等待响应
        result = self.sock.recv(128).decode()
        if result == "OK":
            # 接收文件列表
            files = self.sock.recv(1024*1024)
            print(files.decode())
        else:
            print("文件库为空")


# 图形展示 输入
class FTPView:
    def __init__(self):
        self.__ftp = FTPHandle()

    def __display_menu(self):
        print("1) 查看文件")
        print("2) 下载文件")
        print("3) 上传文件")
        print("4) 退   出")
        print("")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == '1':
            self.__ftp.do_list()
        elif item == '2':
            pass
        elif item == '3':
            pass
        elif item == '4':
            pass
        else:
            print("请输入正确选项！")

    # 入口程序启动
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()


if __name__ == '__main__':
    ftpview = FTPView()
    ftpview.main()  # 启动
