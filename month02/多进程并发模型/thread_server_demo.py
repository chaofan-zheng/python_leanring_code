from socket import *
from threading import Thread


# 具体处理客户端事物
class Handle:
    def __init__(self):
        pass

    def request(self, data):
        print(data.decode())


# 为每一个客户端创建线程类
class ClientThread(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        self.handle = Handle()  # 直接实例化类
        super().__init__(daemon=True)

    def run(self):
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break
            self.handle.request(data)  # 调用具体处理的方法
        self.connfd.close()


# 并发服务类
class ConcurrentServer:

    def __init__(self, host="", port=0):
        self.sock = self.create_sokect()
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)

    def create_sokect(self):
        tcp_socket = socket()
        tcp_socket.bind(self.addr)
        return tcp_socket

    def serve_forever(self):
        print("Listen the port %d" % self.port)
        self.sock.listen(5)
        while True:
            connfd, addr = self.sock.accept()
            print("Connect from ")
            thread = ClientThread(connfd)
            thread.start()


if __name__ == '__main__':
    server = ConcurrentServer("0.0.0.0", 8888)
    server.serve_forever()
