from socket import *

ADDR = ("127.0.0.1", 7777)


class QueryWord:
    def __init__(self):
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)

    def find_word(self, msg):
        self.udp_socket.sendto(msg.encode(), ADDR)
        print(f"你要查询的单词为{msg}")
        data, addr = self.udp_socket.recvfrom(2048)
        return data.decode()

    def query_word(self):
        mark = True
        while mark:
            msg = input("please input the word that you want to query")
            if msg == "##":
                print("会话结束")
                mark = False
            else:
                mean = self.find_word(msg)
                print("单词的释义为", mean)

    def close(self):
        self.udp_socket.close()


if __name__ == '__main__':
    query = QueryWord()
    query.query_word()
    query.close()
