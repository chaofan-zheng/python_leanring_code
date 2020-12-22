"""
    练习1：定义函数,在列表中找出所有偶数
[43,43,54,56,76,87,98]

练习2. 定义函数,在列表中找出所有数字
 [43,"悟空",True,56,"八戒",87.5,98]
"""


# def func01(list01):
#     for item in list01:
#         if item % 2 == 0:
#             yield item
#
#
# list01 = [43, 43, 54, 56, 76, 87, 98]
# result = func01(list01)
# for item in result:
#     print(item)

def func01(list01):
    for item in list01:
        if type(item) == int or type(item) == float:
            yield item


list02 = [43,"悟空",True,56,"八戒",87.5,98]
result = func01(list02)
for item in result:
    print(item)
