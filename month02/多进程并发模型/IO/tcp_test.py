
from socket import *

#　服务器地址
ADDR = ("127.0.0.1",8888)

# 默认就是tcp
tcp_socket = socket()

# 连接服务器
tcp_socket.connect(ADDR)

#　先发送再接收
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("From server:",data.decode())

tcp_socket.close()