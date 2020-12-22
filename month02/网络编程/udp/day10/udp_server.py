"""
udp套接字服务端模型
重点代码！！！
"""
from socket import *

# 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0", 8888))

while True:
    # 接收 发送消息 data-->bytes
    data, addr = udp_socket.recvfrom(1024)
    if data == b"##":
        break
    print("From", addr, ":", data.decode())
    n = udp_socket.sendto(b"Thanks", addr)
    print("发送了%dbytes" % n)

# 关闭套接字
udp_socket.close()
