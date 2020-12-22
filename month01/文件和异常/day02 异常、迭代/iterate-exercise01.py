"""
    创建列表，使用迭代思想，打印每个元素
"""


# for item in list01:
#     print(item)
# 原理

# list01 = [1, 2, 3, 4, 5, 6]
# list_iterator = list01.__iter__()  # 这个iter函数返回这个list_iterator
# while True:
#     try:
#         item = list_iterator.__next__()
#         print(item)
#     except StopIteration:
#         break


class ListIterator:
    def __init__(self, list01):
        self.list01 = list01
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index > len(self.list01) - 1:
            raise StopIteration
        return self.list01[self.index]


class ListIterable:
    def __init__(self, list01):
        self.list01 = list01

    def __iter__(self):
        return ListIterator(self.list01)


list_iterable = ListIterable([1, 2, 3, 4, 5, 6])
for item in list_iterable:
    print(item)

"""
    练习二 面试题：创建字典，使用迭代思想，打印每一个键值对
"""
dict01 = {"a": 1, "b": 2, "c": 3}
dict01_iterator = dict01.__iter__()
while True:
    try:
        key = dict01_iterator.__next__()
        value = dict01[key]
        print(key, value)
    except StopIteration:
        break
