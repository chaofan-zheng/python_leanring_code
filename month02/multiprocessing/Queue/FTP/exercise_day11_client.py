"""
图片上传客户端
"""
from socket import *
from time import sleep

ADDR = ("127.0.0.1", 8889)


def send_image(tcp_socket, filename):
    file = open(filename, 'rb')
    # 边读边发送
    while True:
        data = file.read(1024)
        # 文件结尾退出
        if not data:
            break
        tcp_socket.send(data)
    sleep(0.1) # 防止##与文件内容粘包
    tcp_socket.send(b"##") # 结束标志
    file.close()


def main(filename):
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    # 调用函数发送文件
    send_image(tcp_socket, filename)

    msg = tcp_socket.recv(1024)
    print(msg.decode())

    tcp_socket.close()


if __name__ == '__main__':
    main("timg.jfif")
