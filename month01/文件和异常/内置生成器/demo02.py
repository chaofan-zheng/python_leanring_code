"""

"""
# dict01 = {"a": 1, "b": 2, "c": 3}
list01 = [1, 2, 3, 4]
list02 = [5, 6, 7, 8]
for item in zip(list01, list02):
    print(item)

# 2048里面的转置函数，简化
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

# list_new = []
# for item in zip(*list01):
#     list_new.append(list(item))
# print(list_new)

list_new = [list(item) for item in zip(*list01)]
print(list_new)