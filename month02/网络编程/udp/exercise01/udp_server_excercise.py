"""
练习1 客户端可以循环的输入消息发送给服务端，服务端接受后回发Thanks，当客户端输入为##是，两端均结束
循环首发消息服务端
"""
from socket import *

# 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

udp_socket.bind(("0.0.0.0", 9999))

mark = True
while mark:
    data,addr = udp_socket.recvfrom(2048)
    if data.decode() == "##":
        print("会话结束")
        udp_socket.close()
        mark = False
    else:
        print(f"从{addr}接收到消息{data.decode()}")
        n = udp_socket.sendto("感谢老铁送的火箭".encode(),addr)