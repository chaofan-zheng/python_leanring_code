from socket import *

ADDR = ("127.0.0.1", 6956)

# 创建tcp套接字
tcp_socket = socket()

tcp_socket.connect(ADDR)

# 先发送再接受，不再需要新的套接字去管理
while True:
    msg = input(">>")
    # 方案二
    if msg == "##":
        break
    tcp_socket.send(msg.encode())
    # 方案一
    # if msg == "##":
    #     break
    data = tcp_socket.recv(1024)
    print("From server:", data.decode())


tcp_socket.close()
