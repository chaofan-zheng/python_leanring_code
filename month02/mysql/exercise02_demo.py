import re
import pymysql


def get_content(filename):
    file = open(filename)
    data = []
    for line in file:
        word_and_mean = re.findall(r"(\w+)\s+(.*)", line)
        data.append(word_and_mean[0])
    file.close()
    return data


def main(filename):
    args = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "417355570",
        "database": "dict",
        "charset": "utf8"
    }
    db = pymysql.connect(**args)
    cur = db.cursor()
    try:
        sql = "insert into words(word,mean) values(%s,%s)"  # 无脑%s 即可
        cur.executemany(sql, get_content(filename))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    cur.close()
    db.close()


main("../day03 data/dict.txt")
