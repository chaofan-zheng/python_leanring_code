import redis

r = redis.Redis(password='417355570')
# 任务信息：任务类别——发送者——接受者——内容
task = '%s_%s_%s_%s'%('sendMail','123@qq.com','456@qq.com','hello world')
# 添加任务
r.lpush('pylk1',task)
