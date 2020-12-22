from socket import *


ADDR = ("127.0.0.1",6955)

tcp_socket = socket()
tcp_socket.connect(ADDR)

while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())

# 关闭
tcp_socket.close()