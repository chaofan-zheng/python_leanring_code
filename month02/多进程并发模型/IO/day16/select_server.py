"""
IO并发模型 基于select方法 tcp
重点代码 ！！！
"""
from socket import *
from select import select

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 创建tcp套接字连接客户端，处理请求
tcp_socket = socket()
tcp_socket.bind(ADDR)
tcp_socket.listen(5)

# 设置为非阻塞IO
tcp_socket.setblocking(False)

# 设置监控列表
rlist = [tcp_socket]
wlist = []
xlist = []

# 循环的监控发生的IO事件
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    # 遍历就绪的IO对象
    for r in rs:
        # 分情况处理
        if r is tcp_socket:
            # 处理客户端连接
            connfd, addr = r.accept()
            print("Connect from", addr)
            # 添加客户端连接套接字到监控列表
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            # 处理一个客户端的消息
            data = r.recv(1024)
            # 客户端退出
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            # r.send(b"OK")
            wlist.append(r)

    for w in ws:
        w.send(b"OK")
        # 如果不移除会一直让发送
        wlist.remove(w)














