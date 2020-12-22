

class MyRange:
    def __init__(self, begin_num=0, end_num=0, step=1):
        self.begin_num = begin_num
        self.end_num = end_num
        self.step = step
        self.my_range = (self.begin_num, self.end_num, self.step)

    def __iter__(self):
        return MyRangeIterator(self.my_range)


class MyRangeIterator:
    def __init__(self, my_range):
        self.my_range = my_range
        self.num = self.my_range[0] - 1

    def __next__(self):
        self.num += self.my_range[2]
        if self.num >= self.my_range[1]:
            raise StopIteration
        return self.num


for number in MyRange(0, 5, 2):
    print(number)
