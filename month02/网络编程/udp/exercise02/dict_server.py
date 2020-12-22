"""
基于udp循环收发完成

在客户端输入单词，从服务端哪里得到单词解释，并打印出来，要求多个客户端可以一起查询

服务端利用数据库帮助客户端完成单词查询，将解释发送给客户端
"""
from socket import *
import pymysql


class Database:
    # 连接数据库
    args = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "417355570",
        "database": "dict",
        "charset": "utf8"
    }

    def __init__(self):
        self.db = pymysql.connect(**Database.args)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def get_mean_from_sql(self, word):
        # 方法一
        # try:
        #     sql = f"select mean from words where word = '{word}';"
        #     self.cur.execute(sql)
        #     mean = self.cur.fetchone()[0]
        # except Exception as e:
        #     print(e)
        #     mean = "所要查询的单词不存在"
        # self.close()
        # return mean

        # 方法二
        sql = "select mean from words where word = %s;"
        self.cur.execute(sql, [word])
        mean = self.cur.fetchone()
        if mean:
            self.close()
            return mean[0]
        else:
            self.close()
            return "not find this word."


class QueryWord:
    def __init__(self, host="", port=7777):
        self.host = host
        self.port = port
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.bind()  # 在创建类的时候自动调用
        self.db = Database()  # 数据库处理

    def bind(self):
        self.address = (self.host, self.port)  # 从设计思想上来说，address与绑定的联系会更加紧密
        self.udp_socket.bind(self.address)

    def query_word(self):
        mark = True
        while mark:
            word, addr = self.udp_socket.recvfrom(1024)
            mean = self.db.get_mean_from_sql(word.decode())
            self.udp_socket.sendto(mean.encode(), addr)

    def close(self):
        self.udp_socket.close()


if __name__ == '__main__':
    query_word = QueryWord(host='0.0.0.0', port=7777)
    query_word.query_word()
