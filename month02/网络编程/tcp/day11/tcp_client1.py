"""
tcp客户端 循环示例1
重点代码 ！！！
"""
from socket import *

#　服务器地址
ADDR = ("127.0.0.1",8889)

# 默认就是tcp
tcp_socket = socket()

# 连接服务器
tcp_socket.connect(ADDR)

#　先发送再接收
while True:
    msg = input(">>")
    # 不通知服务端直接退出
    if not msg:
        break
    tcp_socket.send(msg.encode())
    # 结束退出
    # if msg == "##":
    #     break
    data = tcp_socket.recv(1024)
    print("From server:",data.decode())

# 关闭
tcp_socket.close()