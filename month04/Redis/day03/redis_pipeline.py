# 创建连接池并连接到redis
import time

import redis

pool = redis.ConnectionPool(host='127.0.0.1', db=0, port=6379, password='417355570')
r = redis.Redis(connection_pool=pool)


def withpipeline(r):
    p = r.pipeline()
    for i in range(1000):
        key = 'test1' + str(i)
        value = i + 1
        p.set(key, value)
    p.execute()


def withoutpipeline(r):
    for i in range(1000):
        key = 'test2' + str(i)
        value = i + 1
        r.set(key, value)


def test(r):
    p = r.pipeline()
    p.set('fans', 50)
    p.incrby('fans', 100)
    res1 = p.get('fans')
    p.lpop('fans')
    p.set('b', 100)
    res2 = p.get('b')
    p.execute()
    print(res1, res2)


if __name__ == '__main__':
    r.flushdb()
    t1 = time.time()
    withpipeline(r)
    t2 = time.time()
    print(t2 - t1)
    t1 = time.time()
    withoutpipeline(r)
    t2 = time.time()
    print(t2 - t1)
    test(r)

# 0.016157865524291992
# 0.0647728443145752
