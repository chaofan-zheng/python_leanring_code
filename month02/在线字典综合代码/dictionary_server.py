"""
    在线字典服务端
"""
from socket import *
from select import *
from multiprocessing import Process
import pymysql
from time import *


# 用于数据库的交互
class Database:
    database_args = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "417355570",
        "database": "dict",
        "charset": "utf8"
    }

    def __init__(self):
        self.db = pymysql.connect(**Database.database_args)

    def close(self):
        self.db.close()

    # 查询单词解释方法
    def find_word(self, word):
        self.cur = self.db.cursor()
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        mean = self.cur.fetchone()
        if mean:
            self.cur.close()
            return mean[0]
        else:
            self.cur.close()
            return "Not Found"

    def name_not_exist(self, name):
        self.cur = self.db.cursor()  # 防止游标的数据产生变化 因为游标会操作硬盘
        sql = "select name from users"
        self.cur.execute(sql)
        name_tuple = self.cur.fetchall()
        for tuple in name_tuple:
            if tuple == (name,):
                self.cur.close()
                return False
        else:
            self.cur.close()
            return True

    def register(self, name, passwd, birthday):
        self.cur = self.db.cursor()
        if not birthday:  # birthday 为空，就不插入
            sql = "insert into users(name,passwd) values(%s,%s)"
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            print("没有插入birthday")
        else:
            sql = "insert into users(name,passwd,birthday) values(%s,%s,%s)"
            try:
                self.cur.execute(sql, [name, passwd, birthday])
            except Exception as e:
                return False
            else:
                self.db.commit()
                print("插入了birthday")
        self.cur.close()
        return True

    def password_same(self, name, passwd):
        self.cur = self.db.cursor()
        sql = "select passwd from users where name =%s"
        self.cur.execute(sql, [name])
        passwd_test = self.cur.fetchone()[0]
        if passwd_test == passwd:
            self.cur.close()
            return True
        else:
            self.cur.close()
            return False

    def query(self, name, word):
        self.cur = self.db.cursor()
        sql02 = "select id from users where name=%s"
        self.cur.execute(sql02, [name])
        user_id = self.cur.fetchone()[0]
        sql03 = "insert into history(user_id,word) values(%s,%s)"
        self.cur.execute(sql03, [user_id, word])
        self.db.commit()
        sql01 = "select mean from words where word = %s"
        self.cur.execute(sql01, [word])
        mean = self.cur.fetchone()
        if mean:
            self.cur.close()
            return mean[0]
        else:
            self.cur.close()
            return "Not Found"

    def history(self, name):
        """

        :return: ((name,word,query_time),(name,word,query_time))
        """
        self.cur = self.db.cursor()
        sql = "select name,word,query_time from history left join users on history.user_id=users.id where name =%s;"
        self.cur.execute(sql, [name])
        history_tuple = self.cur.fetchall()
        print(history_tuple)
        return history_tuple


class ClientConnector:
    def __init__(self):
        self.sock = self.connect_client()
        self.handle = Handle()

    def connect_client(self):
        HOST = '0.0.0.0'
        PORT = 9999
        ADDR = (HOST, PORT)
        tcp_socket = socket()
        tcp_socket.bind(ADDR)
        tcp_socket.listen(5)
        return tcp_socket

    def io_listener(self):
        MAP = {self.sock.fileno(): self.sock}
        p = poll()
        p.register(self.sock, POLLIN)
        # 循环监控发生的IO事件
        while True:
            events = p.poll()
            print("开始监控")
            for fd, event in events:
                if fd is self.sock.fileno() and event is POLLIN:
                    connfd, addr = MAP[fd].accept()
                    print("Connect from", addr)
                    p.register(connfd, POLLIN)
                    MAP[connfd.fileno()] = connfd
                else:
                    data = MAP[fd].recv(1024)
                    if not data:
                        print("客户端异常退出")
                        p.unregister(MAP[fd])
                        MAP[fd].close()
                        del MAP[fd]
                        continue
                    head = data.decode().split("##")
                    print(head)
                    command = head[0]
                    if command == "QUIT":
                        p.unregister(MAP[fd])
                        MAP[fd].close()
                        del MAP[fd]
                        continue
                    content = head[1]
                    self.handle.handle(MAP[fd], command, content)



class Handle:
    def __init__(self):
        self.database = Database()

    def handle(self, connfd, command, content):
        if command == "R":
            name = content.split(" ")[0]
            passwd = content.split(" ")[1]
            if content.split(" ")[2]:
                birthday = content.split(" ")[2]
            else:
                birthday = ""
            self.register(connfd, name, passwd, birthday)
        elif command == "L":
            name = content.split(" ")[0]
            passwd = content.split(" ")[1]
            self.login(connfd, name, passwd)
        elif command == "Q":
            name = content.split(" ")[0]
            word = content.split(" ")[1]
            self.query(connfd, name, word)
        elif command == "H":
            self.history(connfd, content)
        elif command == "QUIT":
            self.quit(connfd)

    def register(self, connfd, name, passwd, birthday):
        if self.database.name_not_exist(name):  # 判断name是不是在数据库里
            out = self.database.register(name, passwd, birthday)
            if out:
                connfd.send(b"1")
            else:
                connfd.send(b"2")  # 2说明格式不对
        else:
            connfd.send(b"0")

    def login(self, connfd, name, passwd):
        if self.database.name_not_exist(name):
            connfd.send(b"0")
        else:
            if self.database.password_same(name, passwd):
                connfd.send(b"1")
            else:
                connfd.send(b"0")

    def query(self, connfd, name, word):
        mean = self.database.query(name, word)
        connfd.send(mean.encode())

    def history(self, connfd, name):
        history_tuple = self.database.history(name)
        for tuple in history_tuple:
            msg = f"用户名：{tuple[0]},查询单词:{tuple[1]},查询时间{tuple[2]}"
            connfd.send(msg.encode())
            sleep(0.05)
        connfd.send(b"END")

    def quit(self, connfd):
        pass


if __name__ == '__main__':
    client_connector = ClientConnector()
    # p = Process(target=client_process.io_listener(), daemon=True)
    # p.start()
    client_connector.io_listener()
