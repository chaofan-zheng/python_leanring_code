from socket import *

ADDR = ("127.0.0.1", 6666)
while True:
    text = input("我:")
    if not text:
        break  # 如果输入回车，直接退出程序
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    tcp_socket.send(text.encode())
    data = tcp_socket.recv(1024)
    print("mm:", data.decode())
    tcp_socket.close()
