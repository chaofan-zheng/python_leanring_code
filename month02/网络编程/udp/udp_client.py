"""
udp 客户端
重点代码
"""
from socket import *

# 记录服务端地址，大写为常量
ADDR = ("127.0.0.1", 8888)

# 与服务端相同套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 客户端不需要绑定端口，由操作系统自动分配
# 理论上可以绑定，但是绑定了就死了，微信和其他程序一个端口的话就不能同时运行

msg = input(">>")
udp_socket.sendto(msg.encode(), ADDR)  # encode()转化为字节串

data, addr = udp_socket.recvfrom(1024)
print("From server:", data.decode())

udp_socket.close()
