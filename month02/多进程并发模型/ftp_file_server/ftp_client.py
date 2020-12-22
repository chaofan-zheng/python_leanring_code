from socket import *
import os
import sys
from time import *


class FTPView:
    def __init__(self):
        self.__ftp = FTPHandle()

    def display_menu(self):
        print("===========")
        print("1) 查看文件")
        print("2) 下载文件")
        print("3) 上传文件")
        print("4) 退出网盘")
        print("===========")

    def select_menu(self):
        while True:
            choice = input(">>")
            if choice == "1":
                self.__ftp.show_files()
            elif choice == "2":
                self.__ftp.download_file()
            elif choice == "3":
                self.__ftp.upload_file()
            elif choice == "4":
                self.__ftp.my_quit()
            else:
                print("输入指令有误，请重新输入")
                continue

    # 入口程序启动方法
    def main(self):
        while True:
            self.display_menu()
            self.select_menu()


class FTPHandle:
    SERVERADDR = ("127.0.0.1", 6955)

    def __init__(self):
        self.sock = self.connect_socket()

    def connect_socket(self):
        tcp_socket = socket()
        tcp_socket.connect(FTPHandle.SERVERADDR)
        return tcp_socket

    def show_files(self):
        msg = "SH_MYNCP_  "  # 加空格防止报错 split后索引超出范畴
        self.sock.send(msg.encode())
        while True:
            data = self.sock.recv(1024)
            if data == b"##":
                break
            elif data.decode() == "文件列表为空":
                print(data.decode())
                break
            print(data.decode())

    def download_file(self):
        while True:
            filename = input("请输入你要下载的文件名")
            path = input("请输入你的下载路径(以当前文件夹为起点）")  # ./download 当前为.
            # 判断要下载的文件是不是已经在目录里了,同时判断文件路径是不是写错了
            try:
                filelist = os.listdir(f"{path}")
            except Exception:
                print("路径错误")
                continue
            else:
                if filename in filelist:
                    print("该文件已经存在于目标路径中")
                    continue
                else:
                    new_file = open(f"{path}/{filename}", "wb")
                    name_message = "DL_MYNCP_" + filename
                    self.sock.send(name_message.encode())
                    data = self.sock.recv(1024)
                    if data.decode() == "0":
                        print("该文件不存在")
                    else:
                        while True:
                            data = self.sock.recv(1024 * 1024)
                            if data == b"##":
                                print("下载完成")
                                new_file.close()  # 不要忘了close 不然下载完成了也开不见
                                break
                            else:
                                new_file.write(data)

                break

    def upload_file(self):
        pass
        path = input("请输入要上传的本地文件路径")
        filename = input("请输入要上传的本地文件")
        try:
            file = open(f"{path}/{filename}", "rb")
        except Exception:
            print("指定的文件不存在")
        else:
            msg = "UP_MYNCP_" + filename
            self.sock.send(msg.encode())
            data = self.sock.recv(1024)
            if data.decode() == b"0":
                print("文件已经存在")
            else:
                while True:
                    msg = file.read(1024 * 1024)  # msg是二进制码
                    if not msg:
                        sleep(0.1)  # 下面不sleep的话，会欠在缓存区里面
                        self.sock.send(b"##")
                        print("上传成功")
                        file.close()
                        break
                    else:
                        self.sock.send(msg)
                        sleep(0.05)

    def my_quit(self):
        msg = "Q_MYNCP_  "  # 加空格防止报错 split后索引超出范畴
        self.sock.send(msg.encode())
        self.sock.close()
        sys.exit("谢谢使用my网盘，我们的目标是打倒百度网盘")


if __name__ == '__main__':
    view = FTPView()
    view.main()
