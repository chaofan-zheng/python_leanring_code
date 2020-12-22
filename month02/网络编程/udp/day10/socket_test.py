"""
套接字 基础函数示例
"""
import socket

# 创建udp套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 本地地址 127.0.0.1  localhost
# 要求另外一端必须也在该计算机上才能访问
# udp_socket.bind(("127.0.0.1",8888))

# 网络地址 172.40.0.54
# 另外一段通过网络IP访问，可以在其他计算机上
udp_socket.bind(("172.40.0.54",8888))

# 0.0.0.0
# 等同于 127.0.0.1 + 172.40.0.54
# udp_socket.bind(("0.0.0.0",8888))
