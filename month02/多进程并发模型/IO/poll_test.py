"""
IO并发模型 基于select方法 tcp
与tcp test 一起使用
"""
from socket import *
from select import *

# 创建tcp套接字连接客户端，处理请求
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 创建tcp套接字连接客户端，处理请求
tcp_socket = socket()
tcp_socket.bind(ADDR)
tcp_socket.listen(5)

# 需要提前建立查找字典
map = {tcp_socket.fileno(): tcp_socket, 1: POLLIN}  # 这个POLLIN不在map里也没关系

tcp_socket.setblocking(False)  # 把tcp套接字设置为非阻塞

p = poll()
p.register(tcp_socket, POLLIN)

# print(POLLIN)
# 循环的监控发生的IO事件
while True:
    events = p.poll()  # 开始监控
    print("开始监控")
    for fd, event in events:
        if fd is tcp_socket.fileno() and event is 1:
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            connfd.setblocking(False)
            p.register(connfd, POLLIN)
            map[connfd.fileno()] = connfd  # 字典要时刻与关注的IO保持一致
        else:
            data = map[fd].recv(1024)
            if not data:
                p.unregister(map[fd])
                map[fd].close()
                del map[fd]  # 要随时的维护字典
                continue
            print(data.decode())
            map[fd].send(b"ok")
