import redis

# r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='417355570')
r = redis.Redis(password='417355570')  # 可以只有password，其他都是默认值
if __name__ == '__main__':
    print(r.keys('*'))
    r.flushdb()
    r.rpush('spider:urls', '01_baidu.com', '02_taobao.com', '03_sina.com', '04_jd.com', '05_xxx.com')

