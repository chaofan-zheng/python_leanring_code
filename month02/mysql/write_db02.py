import pymysql

args = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "417355570",
    "database": "tedu",
    "charset": "utf8"
}

# 连接数据库
db = pymysql.connect(**args)

# 创建游标 游标对象：执行sql得到执行结果的对象
cur = db.cursor()

# 批量写操作数据
stu_list = [
    ("张三", 12, "f", 91),
    ("李四", 19, "m", 99),
    ("老王", 20, "o", 88)
]
try:
    sql = "insert into cls(name,age,sex,score) values(%s,%s,%s,%s)"
    cur.executemany(sql, stu_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭数据库连接
cur.close()
db.close()


