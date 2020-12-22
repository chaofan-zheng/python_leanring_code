"""
练习 1：将列表中所有奇数设置为 None
练习 2：将列表中所有偶数自增 1

"""
list01 = [1, 2, 3, 4, 5, 6, 7]
for i, item in enumerate(list01):
    if item % 2 == 1:
        list01[i] = None
print(list01)

list01 = [1, 2, 3, 4, 5, 6, 7]
for i, item in enumerate(list01):
    if item % 2 == 0:
        list01[i] += 1
print(list01)

