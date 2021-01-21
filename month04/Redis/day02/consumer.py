import redis

r = redis.Redis(password='417355570')

while True:
    task = r.brpop('pylk1',5)
    print(task)
    if task:
        # 处理任务（耗时操作)
        task_str = task[1].decode()
        task_list = task_str.split('_')
        print(f'-receive task, task is {task_list[0]}-')
        if task_list[0] == 'sendMail':
            print('call send mail function!')
        else:
            pass

    else:
        print('-no task-')
    # (b'pylk1', b'sendMail_123@qq.com_456@qq.com_hello world')
    # None
    # -no task-   # 隔五秒打印一次
    # None
    # -no task-