"""
使用http协议，将一个文件的内容作为响应体发送给浏览器显示
（文本可以是文本也可以是图片）
Content-Type:image/jpeg
"""
from socket import *
from select import *
import re


class Handle:
    def __init__(self, connfd, html):
        self.connfd = connfd
        self.html = html
        self.handle()

    def handle(self):
        # 解决一下客户端异常断开的情况
        data = self.connfd.recv(1024 * 10).decode()
        pattern = r"[A-Z]+\s+(?P<info>/\S*)"
        result = re.match(pattern, data)
        if result:
            info = result.group("info")
            print("请求内容：", info)
            self.send_html(info)

    def send_html(self, info):
        if info == "/":
            filename = self.html + "/index.html"
        else:
            filename = self.html + info
        try:
            file = open(f"{filename}", "rb")
        except:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response = response.encode() + b"Sorry"
        else:
            content = file.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response = response.encode() + content

        finally:
            self.connfd.send(response)  # 最后一定要把它转化成字节串


class WebServer:
    def __init__(self, host="0.0.0.0", port=8888, html=""):
        self.html = html
        self.port = port
        self.host = host
        self.sock = self.create_socket()
        self.rlist = []
        self.wlist = []
        self.xlist = []

    def create_socket(self):
        sock = socket()
        self.address = (self.host, self.port)
        sock.bind(self.address)
        sock.setblocking(False)
        return sock

    # 处理浏览器连接这个IO事件
    def connect(self):
        connfd, addr = self.sock.accept()
        print("成功连接客户端", connfd)
        connfd.setblocking(False)
        self.rlist.append(connfd)
        # 添加浏览器到关注列表

    # def handle(self, connfd):
    #     # 解决一下客户端异常断开的情况
    #     data = connfd.recv(1024 * 10)
    #     head = data.decode().split("\r\n")[0]
    #     request = head.split(" ")[0]
    #     url = head.split(" ")[1]
    #     if request == "GET":
    #         self.do_get(connfd)
    #
    # def do_get(self, connfd):
    #     with open(f"{self.html}", "rb") as file:
    #         content = file.read()
    #         msg = "HTTP/1.1 200 OK\r\n"
    #         msg += "Content-Type:text/html\r\n"
    #         msg += "\r\n"
    #         msg = msg.encode()+content
    #         connfd.send(msg)

    def start(self):
        self.sock.listen(5)
        print(f"Listen the port {self.port}")
        self.rlist.append(self.sock)
        # IO 多路复用模型
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sock:
                    self.connect()
                else:
                    # self.handle(r)
                    self.handle = Handle(r, self.html)
                    self.rlist.remove(r)
                    r.close()


"""
思考如何使用封装接口
socket()
    实例化对象  --> 通过方法的组合，来实现不同的功能

process()
    实例化对象  --> 按照步骤完成事件（一个入口函数，通过入口函数调用内部函数）

我们要去思考的就是，需要让用户去决定什么事情，然后通过传参的形式传入
要用户决定的事情很多的时候，还可以做出一个配置文件
"""
if __name__ == '__main__':
    # 用户如何去使用
    # 用户需要决定什么
    # 地址，网页
    httpd = WebServer(host="0.0.0.0", port=8889, html="./info/static")
    httpd.start()  # 入口 启动服务
    # 用户如何去使用
