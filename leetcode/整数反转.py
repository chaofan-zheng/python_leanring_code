"""

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""


def reverse_force(x):
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] != "-":    # 增加负数判断
        str_x = str_x[::-1]
        x = int(str_x)
    else:
        str_x = str_x[:0:-1]
        x = int(str_x)
        x = -x
    return x if -2147483648 < x < 2147483647 else 0  # 32 位 看有没有溢出


x = -1234
print(reverse_force(x))
