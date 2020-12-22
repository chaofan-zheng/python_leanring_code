"""
套接字 基础函数示例
"""
import socket

# 创建udp套接字
dir(socket)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 本地地址 127.0.0.1  localhost
# 程序必须要和当前计算机在同一台计算机上，因为这是一个测试地址
udp_socket.bind(("127.0.0.1", 8888))

# 绑定网络地址 176.17.12.166
# 另外一段通过网络ip访问，可以在其他计算机上访问
udp_socket.bind(("172.20.10.10", 8888))

# 0.0.0.0
# 等同于 127.0.0.1 + 网络地址的功效
udp_socket.bind(("0.0.0.0", 8888))

# 除此之外，绑定任何一个地址都是错误的
