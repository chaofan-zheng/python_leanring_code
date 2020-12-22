"""
客户端可以向服务端发送问题
服务器扮演机器客服角色，根据客户端的提问，回复相应的答案
要求可以同时多个客户端提问
{key：value}

我：你多大了
mm：我两岁了
我：你男生女生啊
mm：我是机器人
我：今天股票怎么样
mm：我还小不太懂
"""

from socket import *

reply_dict = {"多大了": "我两岁啦", "几岁": "我两岁啦", "男生女生": "我是机器人"}

tcp_socket = socket()
tcp_socket.bind(("0.0.0.0", 6666))
tcp_socket.listen(5)
while True:
    connfd, addr = tcp_socket.accept()
    data = connfd.recv(1024)
    for key in reply_dict:
        if str(key) in str(data.decode()):
            reply = reply_dict[key]
            break
    else:
        reply = "我还小不太懂"

    connfd.send(reply.encode())
    connfd.close()
