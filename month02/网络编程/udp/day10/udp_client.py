"""
udp 客户端示例
重点代码  ！！！
"""
from socket import *

# 记录服务端地址
ADDR = ("127.0.0.1", 8888)

# 与服务端相同套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    # 将输入的内容发送给服务端
    msg = input(">>")
    # 客户端直接退出
    if not msg:
        break
    udp_socket.sendto(msg.encode(), ADDR)
    # 通过## 让服务端退出
    if msg == '##':
        break
    data, addr = udp_socket.recvfrom(1024)
    print("From server:", data.decode())

udp_socket.close()
