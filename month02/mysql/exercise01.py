"""
编写一个程序，输入一个学生的姓名，将该学生的成绩改为100分
"""
import pymysql

book_name = input("请输入书名")

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
try:
    sql = "update book set price = 100 where name = '%s';" % book_name  # 必须加一个引号
    cur.execute(sql)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭数据库连接
cur.close()
db.close()
