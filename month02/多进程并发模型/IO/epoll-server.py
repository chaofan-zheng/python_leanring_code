"""
IO并发模型 基于epoll方法 tcp

1.在生成对象地方改成epoll
2.把事件改成EPOLLIN,EPOLLOUT
3.生成事件的poll不用改，就是poll

"""
from socket import *
from select import *

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

tcp_socket = socket()
tcp_socket.bind(ADDR)
tcp_socket.listen(5)

tcp_socket.setblocking(False)

ep = epoll()  # 要改
ep.register(tcp_socket, EPOLLIN)  # 要改

map = {tcp_socket.fileno(): tcp_socket}

while True:
    events = ep.poll()  # 这就是poll，不用改
    for fd, event in events:
        if fd is tcp_socket.fileno():
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            connfd.setblocking(False)
            map[connfd.fileno()] = connfd
            ep.register(connfd, EPOLLIN)
        else:
            data = map[fd].recv(1024)
            if not data:
                ep.unregister(fd)
                map[fd].close()
                del map[fd]
                continue
            print(data.decode())
            map[fd].send(b"OK")
