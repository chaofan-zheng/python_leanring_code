"""
tcp 套接字 客户端示例
"""
from socket import *

ADDR = ("127.0.0.1", 6955)

# 创建tcp套接字
tcp_socket = socket()

tcp_socket.connect(ADDR)

# 先发送再接受，不再需要新的套接字去管理
msg = input(">>")
tcp_socket.send(msg.encode())
data = tcp_socket.recv(1024)
print("From server:", data.decode())

tcp_socket.close()
