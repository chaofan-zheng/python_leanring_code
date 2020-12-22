"""
tcp服务端 循环示例2
重点代码 ！！！

* 可以“同时”处理多个客户端，但是每次收发消息
都需要重新建立连接，资源消耗比较多
"""
from socket import *

# 创建tcp套接字 默认就是tcp
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听
tcp_socket.listen(5)

# 循环连接客户端
while True:
    connfd,addr = tcp_socket.accept()
    # 收发一次消息
    data = connfd.recv(1024)
    print("从",addr,"收到:",data.decode())
    connfd.send(b"OK")

    connfd.close()

# 关闭套接字
tcp_socket.close()