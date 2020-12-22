"""
练习3：上传头像的练习
假设客户端需要将自己的头像上传给服务端
请编写程序完成该工作，在服务端以当前日期
保存为jpg格式   2020-12-10.jpg

客户端： 读文件   发送文件内容
服务端： 接收文件内容   写入本地
"""
from socket import *
from time import localtime


# 接收文件 (具体事件)
def recv_image(connfd):
    # 组织文件名
    filename = "%s-%s-%s" % localtime()[:3] + ".jpg"
    file = open(filename, "wb")
    while True:
        # 边收边写
        data = connfd.recv(1024)
        if data == b"##":
            break
        file.write(data)
    file.close()
    connfd.send("图片上传完毕".encode())
    connfd.close()


def main():
    # 创建tcp套接字
    tcp_socket = socket()
    tcp_socket.bind(("0.0.0.0", 8889))
    tcp_socket.listen(5)

    while True:
        connfd, addr = tcp_socket.accept()
        print("Connect from", addr)
        # 调用函数接收图片
        recv_image(connfd)


if __name__ == '__main__':
    main()
