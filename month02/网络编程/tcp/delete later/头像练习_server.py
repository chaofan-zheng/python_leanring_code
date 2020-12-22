from socket import *
import time


class Server:
    def __init__(self):
        self.tcp_socket = socket()
        self.tcp_socket.bind(("0.0.0.0", 7777))
        self.tcp_socket.listen(5)


    def save_message(self):
        self.confd, self.addr = self.tcp_socket.accept()
        print("connect from:",self.addr)
        year = time.localtime()[0]
        month = time.localtime()[1]
        day = time.localtime()[2]
        file = open(f"{year}-{month}-{day}.jpg", "wb")
        while True:
            data = self.confd.recv(1024)
            if not data:
                break
            file.write(data)

        file.close()
        self.confd.close()
        self.tcp_socket.close()

if __name__ == '__main__':
    server = Server()
    server.save_message()