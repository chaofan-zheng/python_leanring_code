"""
    复习列表推导式
    学习生成器表达式
        生成器函数-制作后给其他程序员反复使用
        生成器表达式-制作后给自己使用
"""
#  复习列表推导式
list01 = [4, 4, 5, 6, 7, 8, 9, 90]
# list02 = []
# for item in list01:
#     if item > 5:
#         list02.append(item)
list02 = [item for item in list01 if item > 5]
print(list02)

# def find01():
#     for item in list01:
#         if item > 5:
#             yield item
#
# result = find01()
# for item in result:
#     print(item)

result = (item for item in list01 if item > 5)
for item in result:
    print(item)

for item in result:
    print(item)
# 这一次不会执行
