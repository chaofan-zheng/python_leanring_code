"""
简单的tcp服务端示例
"""
from socket import *

# 创建tcp套接字 默认就是tcp
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听
tcp_socket.listen(5)

# 连接客户端
print("等待客户端连接..")
connfd,addr = tcp_socket.accept()
print("连接:",addr)

# 先收后发
data = connfd.recv(1024)
print("Recv:",data.decode())
connfd.send(b"OK")

# 关闭套接字
connfd.close()
tcp_socket.close()