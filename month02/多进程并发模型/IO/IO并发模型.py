"""
IO并发模型 基于select方法 tcp
与tcp test 一起使用
"""
from socket import *
from select import select

# 创建tcp套接字连接客户端，处理请求
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 创建tcp套接字连接客户端，处理请求
tcp_socket = socket()
tcp_socket.bind(ADDR)
tcp_socket.listen(5)

tcp_socket.setblocking(False) # 把tcp套接字设置为非阻塞

rlist = [tcp_socket]
wlist = []
xlist = []

# 循环的监控发生的IO事件
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    # 分情况处理就绪的IO对象
    for r in rs:
        if r is tcp_socket:
            #处理客户端连接
            connfd, addr = rs[0].accept()
            print("Connect from", addr)
            # 添加客户端连接套接字到监控列表
            # 这个客户端套接字也必须为非阻塞
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            r.send(b"ok")
            wlist.append(r)

    for w in ws:
        w.send(b"ok")
        # wlist.remove(w)
