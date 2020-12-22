import time
from multiprocessing import Process, Queue

all_result = []


def time_calculator(func):
    def wrapper(*args, **kwargs):
        begin_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"运行结果为{result}运行时间为{end_time - begin_time}")
        return result

    return wrapper


q = Queue()


class MyProcess(Process):
    def __init__(self, start_num, end):
        self.start_num = start_num
        self.end = end
        super().__init__()

    @staticmethod
    def get_prime(start, end):
        for num in range(start, end):
            if num == 1 or num == 4:
                continue
            for divider in range(2, int(num / 2)):
                if num % divider == 0:
                    break
            else:
                yield num

    @staticmethod
    def sum_result(start, end):
        out = 0
        for num in MyProcess.get_prime(start, end):  # 用类名去点静态方法
            out += num
        all_result.append(out)
        return out

    def run(self):
        result = MyProcess.sum_result(self.start_num, self.end)
        q.put(result)
        return result


@time_calculator
def process04():
    jobs = []
    for i in range(1, 100000, 25000):
        my_process = MyProcess(start_num=i, end=i + 25000)
        jobs.append(my_process)
        my_process.start()
    [job.join() for job in jobs]
    result = 0
    while not q.empty():
        result += q.get()
    return result

@time_calculator
def process08():
    jobs = []
    for i in range(1, 100000, 12500):
        my_process = MyProcess(start_num=i, end=i + 12500)
        jobs.append(my_process)
        my_process.start()
    [job.join() for job in jobs]
    result = 0
    while not q.empty():
        result += q.get()
    return result


process04()
process08()
