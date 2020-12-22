"""
创建数据库dict
在其中创建一个数据表 words
id word mean

编写一个程序将dict.text（day03 data中）文本的内容传到数据表
"""
# create table words(
# 	id int primary key auto_increment,
#   word varchar(30) not null,
#   mean text
# );

import pymysql

file_name = "../day03 data/dict.txt"
vocabulary_lines = open(file_name).readlines()
list01 = []
for line in vocabulary_lines:
    line_split = line.split(" ")
    word = line_split[0]
    line_split.remove(word)
    mean = " ".join(line_split).strip()
    list01.append((word,mean))


args = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "417355570",
    "database": "dict",
    "charset": "utf8"
}

# 连接数据库
db = pymysql.connect(**args)

# 创建游标 游标对象：执行sql得到执行结果的对象
cur = db.cursor()

# 操作数据
try:
    sql = "insert into words(word,mean) values(%s,%s)"  # 无脑%s 即可
    cur.executemany(sql, list01)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭数据库连接
cur.close()
db.close()
