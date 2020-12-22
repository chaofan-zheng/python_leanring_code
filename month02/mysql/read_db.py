"""
mysql 操作数据库模版
"""
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

# 操作数据
sql = "select name,score from cls;"
cur.execute(sql)

# 迭代获取查询结果
for row in cur:
    print(row)

one = cur.fetchone()
print(one)  # none
# 是none是因为 查询出来的东西存储在cur游标里面，查找一个就会少一个

# 关闭数据库连接
cur.close()
db.close()
