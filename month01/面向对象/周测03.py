"""
3，猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
"""


def find_x(day):
    x = 3*(2**(day-1))-2
    return x


print(find_x(10))


# a10=1
# a9=(a10+1)*2
# a8=(a9+1)*2
# ....
# 数学思想，正常人的思想
# res = 1
# for i in range(9):
#     res += 1
#     res *= 2
# print(res)
# 计算机的思想
res01 = 1
while True:
    res = res01
    for i in range(9):
        res /= 2
        res -= 1
    if res == 1:
        print(res01)
        break
    res01 += 1
