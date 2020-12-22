"""

"""
message = "我是齐天大圣孙悟空"
# for item in message:
#     print(item)


# for 循环的原理
iterator = message.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break