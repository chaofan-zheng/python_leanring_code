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
sql = "select name,score from cls where score>%s;"
cur.execute(sql, 90)
all = cur.fetchall()
print(all)
# print(all)
# # 三种获取查询结果的函数
# one = cur.fetchone()
# print(one)
# # ('张三', 91.0)
#
# many = cur.fetchmany(2)  # 获取前三个记录
# print(many)
# # (('李四', 99.0), ('老王', 88.0))
#
# all = cur.fetchall()
# print(all)
# # ()

# 关闭数据库连接
cur.close()
db.close()
