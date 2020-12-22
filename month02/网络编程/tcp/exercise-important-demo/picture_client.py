from socket import *


def read_picture(picture):
    """

    :param picture:
    :return: 返回迭代器，读出来是byte
    """
    file = open(picture,"rb")
    file_lines = file.readlines()
    for line in file_lines:
        yield line
    file.close()

def upload_picture():
    ADDR = ("127.0.0.1", 6955)

    # 创建tcp套接字
    tcp_socket = socket()

    tcp_socket.connect(ADDR)

    # 先发送再接受，不再需要新的套接字去管理
    while True:
        for msg in read_picture("timg-2.jpeg"):
            if msg == "":
                break
            tcp_socket.send(msg)
        break
    tcp_socket.close()

upload_picture()