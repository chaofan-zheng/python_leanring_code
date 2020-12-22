import pymysql

# alter table cls add image Mediumblob default null;

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
cur = db.cursor()

# 插入图片
with open("timg.jpeg", "rb") as f:
    data = f.read()
try:
    sql = "update cls set image = %s where id=2"
    cur.executemany(sql, [data])
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# # 获取图片
# try:
#     sql = "select image from cls where id =2;"
#     cur.execute(sql)
#     data = cur.fetchone()[0]  # 因为fetchone返回的是元组
#     with open("kb.jpg", "wb") as f:
#         f.write(data)
# except Exception as e:
#     print(e)
#     db.rollback()
# 关闭数据库连接

cur.close()
db.close()


