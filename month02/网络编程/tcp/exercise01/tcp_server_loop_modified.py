"""
'同时'连接客户端
需要付出惨痛的代价，每次发送消息，都要进行三次握手，四次挥手，资源消耗比较多
"""
from socket import *

tcp_socket = socket()
tcp_socket.bind(("0.0.0.0", 6955))
tcp_socket.listen(5)

while True:
    connfd, addr = tcp_socket.accept()  # 创建新的套接字
    data = connfd.recv(1024)
    print("Recv:", data.decode(), "from", addr)
    n = connfd.send(b"OK")
    connfd.close()
