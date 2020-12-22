from socket import *

#　服务器地址
ADDR = ("127.0.0.1",8888)

# 使用套接字收发消息
def chat(msg):
    # 重新创建套接字才能连接
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    tcp_socket.close()
    return data.decode()

def main():
    #　先发送再接收
    while True:
        msg = input("我：")
        #  输入空退出
        if not msg:
            break
        msg = chat(msg) # 消息收发
        print("mm：",msg)

if __name__ == '__main__':
    main()