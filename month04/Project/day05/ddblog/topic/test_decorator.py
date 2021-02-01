import time


def func():
    print('--- function begin---')
    time.sleep(3)
    print('--- function end---')


# 拓展新功能，打印函数执行的时间消耗


def func_ex(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return None

    return wrapper()


# 与上面的区别是，返回新的函数，【函数编写嵌套，闭包】

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return None

    return wrapper


# 装饰器不能调用


@time_decorator
def func02(a, b, c, d):
    print('--- function begin---')
    time.sleep(3)
    print('--- function end---')
    print(f'a+b={a + b},c+d={c + d}')


def func03():
    x = 1
    print(x)

    def func04():
        x = 1
        print(x)
        return func03

    return func04


# 带参数的装饰器【装饰器带参数，需要定义三层装饰器】
def deco_param(expire, a):
    print(f'在这里的a{a}')

    def _deco_param(func):
        def wrapper():
            start_time = time.time()
            print(f'expire is {expire}')
            func()
            end_time = time.time()
            print(start_time - end_time)

        return wrapper

    return _deco_param


@deco_param(10,'a')
def func06():
    print('--- function begin---')
    time.sleep(1)
    print('--- function end---')


if __name__ == '__main__':
    # func()
    # func_ex(func)
    # res = func02(1, 2, c=3, d=4)  # 使用字典传参
    func06()
    print(f'---content :()---')
    # func03()()()  # 三个1
