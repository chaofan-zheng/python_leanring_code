import redis

# 创建redis数据库的连接对象
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='417355570')

# 1. 单反有命令的，在python里面就有对应的方法
# byte 字节，返回的键的类型都是字节串
print(r.keys('*'))
# [b'10', b'trill:username', b'trill:gender', b'lk2', b'trill:password', b'lk1', b'trill:fansnumber']
# 判断键是否存在
print(r.exists('lk1'), r.exists('lk4'))
# 1 0   # 存在就是1，不存在是0
print(r.type('lk1'))
# b'list'

# 2. 字符串类型的操作
r.set('name', 'aid2010')
print(r.get('name'))  # b'aid2010'
print(r.get('name').decode())  # aid2010

r.set('test', 'test_num', 200, nx=True)  # 不存在时再进行设置
print(r.mset({'x': 100, 'y': 200, 'z': 300}))  # 有返回值，返回值为True
print(r.mget(['x', 'y', 'z']))  # [b'100', b'200', b'300']
# mget传参数用字典 mget拿参数用列表

# 练习
# 查看所有的键
# 没有这个的话，每次运行都会往原先的列表里面添加东西，要用这个遍历删除一遍的
while r.llen('spider:urls'):
    r.rpop('spider:urls')

print(r.keys('*'))
print(r.rpush('spider:urls', '01_baidu.com', '02_taobao.com', '03_sina.com', '04_jd.com', '05_xxx.com'))  # 返回值是列表长度5
print(r.lrange('spider:urls', 0, -1))
print(r.llen('spider:urls'))
print(r.lpop('spider:urls'))
print(r.lpush('spider:urls', '01_tmall.com'))
print(r.lrange('spider:urls', 0, -1))
print(r.rpop('spider:urls'))
print(r.lrange('spider:urls', 0, -1))
print(r.lrem('spider:urls', 0, '02_taobao.com'))
print(r.ltrim('spider:urls', 0, 2))
print(r.lrange('spider:urls', 0, -1))
