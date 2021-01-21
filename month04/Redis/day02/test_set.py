import redis

r = redis.Redis(password='417355570')

r.flushdb()
r.sadd('武将', '张飞', '赵云', '马超', '周瑜')
r.sadd('文臣', '周瑜', '诸葛亮', '司马懿', '郭嘉')
pure_violence = {item.decode() for item in r.sdiff('武将','文臣')}
pure_intelligence = {item.decode() for item in  r.sdiff('文臣','武将')}
violence_intell = {item.decode() for item in r.sinter('文臣','武将')}
all_items = {item.decode() for item in r.sunion('文臣','武将')}
print(pure_violence)
print(pure_intelligence)
print(violence_intell)
print(all_items)