"""
tcp客户端 与服务端配合测试服务端功能
"""
from socket import *

#　服务器地址
ADDR = ("127.0.0.1",8888)

# 默认就是tcp
tcp_socket = socket()
tcp_socket.connect(ADDR)

while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())

# 关闭
tcp_socket.close()