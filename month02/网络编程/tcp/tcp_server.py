"""
简单的tcp服务端示例
"""
from socket import *

# 默认 socket里面什么都不写，就是tcp套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0", 6955))

# 设置监听
tcp_socket.listen(5)

# 连接客户端
print("等待客户端链接")
connfd, addr = tcp_socket.accept()  # 创建新的套接字
print("连接上客户端：", addr)

#
data = connfd.recv(1024)
print("Recv:", data.decode())
n = connfd.send(b"OK")

# 关闭套接字
connfd.close()
tcp_socket.close()
