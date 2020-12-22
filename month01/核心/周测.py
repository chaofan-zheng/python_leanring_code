# 斐波那契数列，从第三项开始，每一项都等于前两项之和
list_original = [1, 1]


def fibonacci_generator(list01, lenth):
    if lenth > 2:
        for i in range(2, lenth):
            num = list01[i - 1] + list01[i - 2]
            list_original.append(num)
    else:
        print("数列长度必须大于2")


lenth = int(input("请输入数列长度"))
fibonacci_generator(list_original, lenth)
print(list_original)


# 删除列表中所有重复的元素（重复元素只保留一个）
# 方法一
def del_repeat_item(list01):
    set01 = set(list01)
    return list(set01)


list01 = [4, 35, 7, 425, 66, 66, 77, 7, 4, 5, 6, 6, 7, 234]
print(del_repeat_item(list01))


# 方法二    列表去重，面试题
def del_repeat_item02(list02):
    for r in range(len(list02) - 1, 0, -1):
        for c in range(r - 1, -1, -1):
            if list02[r] == list02[c]:
                del list02[c]


list02 = [4, 35, 7, 425, 66, 66, 77, 7, 4, 5, 6, 6, 7, 234]
del_repeat_item02(list02)
print(list02)

# 方法三 ：
list03 = [4, 35, 7, 425, 66, 66, 77, 7, 4, 5, 6, 6, 7, 234]
list_result = []
for item in list03:
    if item not in list_result:
        list_result.append(item)
print(list_result)

# 判断二维列表中是否存在某个数字

list_two_dimension = [
    [22, 44, 66],
    [11, 33, 55, 324],
    [345, 6356, 765, 34, 5]
]


def judge_num_in_2dimension_list(num):
    """
    判断数字是不是在二维列表中
    :param num: 需要判断的数字
    :return: Ture or False
    """
    for list_r in list_two_dimension:
        for c in range(len(list_r)):
            if num == list_r[c]:
                return True
    return False  # 注意缩进的位置


result = judge_num_in_2dimension_list(11)
print(result)

# 返回字符串中第一个不重复的字符
# 方法一
str03 = "ABCACDBEFD"


def find_the_first_single(str03):
    for item in str03:
        new_str = str03.replace(item, "", 1)  # 不能少了这一步，这一步少了，item 就必在容器里面
        if item not in new_str:
            return item


print(find_the_first_single(str03))

# 方法二  更简单

for item in str03:
    count = str03.count(item)
    if count == 1:
        print(item)
        break


# 获取指定范围内的所有质数。（大于一的整数，除了1和它本身以外不能再被其他数字整除）
# 输入 2，20
# 输出[2,3,5,7,11,13,17,19]
def find_prime_num(begin, end):
    prime_result = []
    for num in range(begin, end + 1):
        list_residents = []
        for test_num in range(2, num):
            resident = num % test_num
            list_residents.append(resident)  # 把余数整理成数列
        multiple_resident = 1
        for num_resident in list_residents:
            multiple_resident *= num_resident  # 把余数进行累乘
        if multiple_resident != 0:  # 如果余数里面没有0 —> 不会被其他数字整除，就是质数
            prime_result.append(num)
    return prime_result


begin = int(input("请输入需要找质数范围的开始值"))
end = int(input("请输入需要找质数范围的结束值"))
print(find_prime_num(begin, end))


def is_prime(start, stop):
    res = []
    for number in range(start, stop + 1):
        for i in range(2,number):
            if number % i == 0:
                break
        else:                    # else在循环外面的话，就是如果这个程序执行完了，同时没有满足if语句，就会执行else语句
            res.append(number)
    return res


res = is_prime(2, 20)
print(res)
