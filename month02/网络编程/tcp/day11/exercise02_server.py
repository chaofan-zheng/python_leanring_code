"""
练习4： 自动对话
客户端可以向服务端发送问题
服务端扮演机器客服角色，根据客户端的提问
回复相应的答案
要求可以同时多个客户端提问
"""
from socket import *

# 对话字典
chat = {
    "你好":"你好啊",
    "叫什么":"我叫小美",
    "男生女生":"我是机器人啊",
    "几岁":"我2岁啦"
}

# 回答问题
def response(connfd):
    q = connfd.recv(1024).decode()
    # 遍历字典，查看关键词是否在问题中
    for key in chat:
        if key in q:
            connfd.send(chat[key].encode())
            break
    else:
        connfd.send("人家还小，不知道啊".encode())
    connfd.close()

def main():
    # 创建tcp套接字
    tcp_socket = socket()
    tcp_socket.bind(("0.0.0.0", 8888))
    tcp_socket.listen(5)
    # 循环处理客户端对话
    while True:
        connfd,addr = tcp_socket.accept()
        response(connfd) # 回答问题

if __name__ == '__main__':
    main()