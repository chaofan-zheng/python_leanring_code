from socket import *


class Client:
    ADDR = ("127.0.0.1", 8877)

    def __init__(self):
        self.tcp_socket = socket()
        self.tcp_socket.connect(Client.ADDR)

    def main(self):
        while True:
            try:
                content = input(">>>")
            except KeyboardInterrupt:
                content = ""
            if not content:
                break
            self.tcp_socket.send(content.encode())
        self.tcp_socket.close()


if __name__ == '__main__':
    client = Client()
    client.main()
