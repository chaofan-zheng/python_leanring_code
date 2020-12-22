"""
    在线字典客户端
"""
from socket import *
import sys


class Interface:
    def __init__(self):
        self.handle = Handle()

    def interface01(self):
        while True:
            print("=====首页====")
            print("1) 登 录")
            print("2) 注 册")
            print("3) 退 出")
            print("===========")
            self.select01()

    def interface02(self):
        while True:
            print("===========")
            print("1) 查单词")
            print("2) 历史记录")
            print("3) 注销")
            print("===========")
            self.select02()

    def select01(self):
        item = input("请输入选项:")
        if item == '1':
            name = input("请输入用户名")
            passwd = input("请输入密码")
            out = self.handle.login(name, passwd)
            if out:
                self.interface02()
            else:
                self.interface01()
        elif item == '2':
            while True:
                name = input("*请输入用户名")  # *表示必填
                passwd = input("*请输入密码")
                if " " in name or "##" in name or " " in passwd or "##" in passwd:
                    print("用户名和密码不能有空格和'##'")
                    continue
                birthday = input("请输入生日YY-MM-DD")
                out = self.handle.register(name, passwd, birthday)
                if out == 1:
                    break
                elif out == 0:
                    print("用户名已经被使用")
                elif out == 2:
                    print("生日请符合格式YYYY-MM-DD")

        elif item == '3':
            self.handle.quit()
        else:
            print("请输入正确选项！")

    def select02(self):
        item = input("请输入选项:")
        if item == '1':
            word = input("请输入要查询的单词")
            mean = self.handle.query(word)
            print(mean)
        elif item == '2':
            self.handle.history()
        elif item == '3':
            self.handle.logout()
            self.interface01()
        else:
            print("请输入正确选项！")


class Handle:
    def __init__(self):
        self.sock = self.connect_server()
        self.name = ""

    def connect_server(self):
        ADDR = ("127.0.0.1", 9999)
        tcp_socket = socket()
        tcp_socket.connect(ADDR)
        return tcp_socket

    def login(self, name, passwd):
        msg = f"L##{name} {passwd}"
        self.sock.send(msg.encode())
        response = self.sock.recv(1024)
        if response == b"1":
            self.name = name
            print("登录成功")
            return True
        else:
            print("登录失败")
            return False

    def register(self, name, passwd, birthday):
        msg = f"R##{name} {passwd} {birthday}"
        self.sock.send(msg.encode())
        response = self.sock.recv(1024)
        if response == b"1":
            print("注册成功")
            return 1
        elif response == b"2":
            print("注册失败")
            return 2
        else:
            print("注册失败")
            return 0

    def query(self, word):
        msg = f"Q##{self.name} {word}"
        self.sock.send(msg.encode())
        mean = self.sock.recv(1024 * 10)
        return mean.decode()

    def history(self):
        msg = f"H##{self.name}"
        self.sock.send(msg.encode())
        print("查询历史记录如下")
        while True:
            data = self.sock.recv(1024)
            if data == b"END":
                return
            else:
                content = data.decode()
                print(content)

    def logout(self):
        self.name = ""

    def quit(self):
        msg = f"QUIT## "
        self.sock.send(msg.encode())
        print("bye")
        sys.exit()


if __name__ == '__main__':
    interface = Interface()
    interface.interface01()
