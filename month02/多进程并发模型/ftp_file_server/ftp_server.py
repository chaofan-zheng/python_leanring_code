"""
ftp文件服务器
重要代码
1。分为服务端和客户端，要求可以有多个客户端同时操作
2。客户端可以查看服务器中有什么文件
3。客户端可以从文件库中下载文件到本地 文件存在，文件不存在
4。客户端可以上传一个本地文件到文件库 文件已经存在
5。使用print在客户端打印命令输入提示

所以如果请求是一种协议的话，
响应也是一种协议
响应码（HTTP协议也有这种响应码）
"""

from socket import *
from multiprocessing import Process
import os
from time import *


# 具体处理客户端事务
class Handle:
    def __init__(self, connfd):
        self.connfd = connfd
        self.files_list = os.listdir("dic01")

    def request(self, command, content):
        if command == "SH":
            self.show_files()
        elif command == "DL":
            self.download_files(content)
        elif command == "UP":
            self.upload_files(content)
        elif command == "Q":
            pass

    def show_files(self):
        if self.files_list:
            for filename in self.files_list:
                self.connfd.send(f"\n{filename}".encode())
            sleep(0.1)
            self.connfd.send(b"##")
        else:
            msg = "文件列表为空"  # 这个作为响应码
            self.connfd.send(msg.encode())
        # 留意沾包的情况

    def download_files(self, content):  # filename需要是utf8
        filename = content
        if filename in self.files_list:
            self.connfd.send("1".encode())  # 1代表成功
            file = open(f"dic01/{filename}", "rb")
            while True:
                msg = file.read(1024 * 1024)  # msg是二进制码
                if not msg:
                    sleep(0.1)  # 下面不sleep的话，会欠在缓存区里面
                    self.connfd.send(b"##")
                    file.close()
                    break
                else:
                    self.connfd.send(msg)
                    sleep(0.05)
        else:
            self.connfd.send("0".encode())  # 0代表失败

    def upload_files(self, content):
        filename = content
        if content in self.files_list:
            self.connfd.send("0".encode())  # 0代表文件已经存在
        else:
            self.connfd.send("1".encode())
            new_file = open(f"./dic01/{filename}","wb")
            while True:
                data = self.connfd.recv(1024*1024)
                if data ==b"##":
                    new_file.close()
                    break
                else:
                    new_file.write(data)


# 为多个客户端创建多进程
class ClientProcess(Process):
    def __init__(self, connfd):
        super().__init__(daemon=True)
        self.connfd = connfd
        self.handle = Handle(connfd)

    def run(self):
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break  # 实现退出的功能
            command = data.decode().split("_MYNCP_")[0]# 通信协议
            content = data.decode().split("_MYNCP_")[1]
            self.handle.request(command, content)
        self.connfd.close()


# 并发服务类
class ConcurrentServer:
    def __init__(self, host="", port=0):
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.sock = self.create_socket()

    def create_socket(self):
        tcp_socket = socket()
        tcp_socket.bind(self.addr)
        return tcp_socket

    def server_forever(self):
        print("Listen the port %d" % self.port)
        self.sock.listen(5)
        while True:
            connfd, addr = self.sock.accept()
            print("Connect from ", addr)
            process = ClientProcess(connfd)
            process.start()


if __name__ == '__main__':
    server = ConcurrentServer("0.0.0.0", 6955)
    server.server_forever()
