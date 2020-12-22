"""
udp套接字服务端模型
重点代码！！！！
"""
from socket import *

# 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0", 8888))

# 接受 发送消息
data, addr = udp_socket.recvfrom(1024)
print("from", addr, ":", data.decode())  # 因为data是字节串，所以要decode()

# 回发一个消息
n = udp_socket.sendto("感谢老铁送的666".encode(), addr)  # b"Thanks"
print("发送了%dbytes" % n)

# 关闭套接字
udp_socket.close()
