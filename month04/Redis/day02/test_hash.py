import redis

r = redis.Redis(password='417355570')

if __name__ == '__main__':
    # 测试之前清一下库
    r.flushdb()  # 项目上线之后这个东西少用
    # 操作hash
    r.hset('pyhk1', 'name', 'aid2010')
    print(r.hget('pyhk1', 'name'))
    r.hmset('pyhk1', {'age': 18, 'city': '北京'})
    print(r.hgetall('pyhk1'))
    print(r.hvals('pyhk1'))
    print(r.hkeys('pyhk1'))
# b'aid2010'
# {b'name': b'aid2010', b'age': b'18', b'city': b'\xe5\x8c\x97\xe4\xba\xac'}
# [b'aid2010', b'18', b'\xe5\x8c\x97\xe4\xba\xac']
# [b'name', b'age', b'city']

