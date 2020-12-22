"""
数据库写操作示例
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

# 操作写数据
# Engine 为 InnoDB
# sql = "update book set price = 88 where id = 1;"
# cur.execute(sql)
# db.commit()
# 引擎为 MyISAM

# try:
#     sql = "update book set price = 88 where id = 1;"
#     cur.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
try:
    sql = "update book set price =%s where name = %s;"  # 无脑%s 即可
    cur.execute(sql, [99, "《骆驼祥子》"])
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# sql = "update student set name = 'Aiden' where id =1;"
# cur.execute(sql)
# 关闭数据库连接
cur.close()
db.close()
