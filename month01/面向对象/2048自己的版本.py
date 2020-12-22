"""
(选做)面向过程 2048游戏核心算法
list_merge = [2,0,0,2]
(1). 定义函数,零元素移动到末尾
     [2,0,0,2]  -->   [2,2,0,0]
     [2,0,2,0]  -->   [2,2,0,0]
     [2,0,4,2]  -->   [2,4,2,0]
(2). 定义函数,相邻相同数字合并
     [2,0,0,2]-调用函数1->[2,2,0,0]->[4,0,0,0]
     [2,0,2,0]-调用函数1->[2,2,0,0]->[4,0,0,0]
     [8,8,8,8]        -->           [16,16,0,0]
     [8,8,8,0]        -->           [16,8,0,0]
"""

from random import randint


def move_zero_to_end_left(list01):
    """
    把零元素向左移到末尾
    :param list01:输入的list
    :return: 输出的list
    """
    list_out = []
    list_zero = []
    for i in range(len(list01)):
        if list01[i] == 0:
            list_zero.append(list01[i])
        else:
            list_out.append(list01[i])
    list_out.extend(list_zero)
    return list_out


# 方法二
# def move_zero_to_end(list01):
#     for i in range(len(list01) - 1, -1, -1):
#         if list01[i] == 0:
#             del list01[i]
#             list01.append(0)
#     return list01


def move_zero_to_end_right(list01):
    """
    把零元素向右移到末尾
    :param list01:
    :return:
    """
    list_out = []
    list_zero = []
    for i in range(len(list01)):
        if list01[i] == 0:
            list_zero.append(list01[i])
        else:
            list_out.append(list01[i])
    for i in range(len(list_zero)):
        list_out.insert(0, list_zero[i])
    return list_out


# list01 = [2, 0, 0, 2]
# list01 = [2, 0, 2, 0]
# print(move_zero_to_end(list01))

def add_adjacent_same_numbers_left(original_list):
    """
    把左边相邻相同的元素加到一起
    :param original_list:  列表
    :return:  整好的列表
    """
    list_sorted = move_zero_to_end_left(original_list)
    for i in range(len(list_sorted) - 1):
        if list_sorted[i] == list_sorted[i + 1]:
            list_sorted[i] += list_sorted[i + 1]
            list_sorted[i + 1] = 0
    list_out = move_zero_to_end_left(list_sorted)
    return list_out


def add_adjacent_same_numbers_right(original_list):
    """
    把右边相邻相同的元素加到一起
    :param original_list:  列表
    :return:  整好的列表
    """
    list_sorted = move_zero_to_end_right(original_list)
    for i in range(len(list_sorted) - 1, 0, -1):
        if list_sorted[i] == list_sorted[i - 1]:
            list_sorted[i] += list_sorted[i - 1]
            list_sorted[i - 1] = 0
    list_out = move_zero_to_end_right(list_sorted)
    return list_out


# 也可以 先取出反向切片，在赋值给左移，在反向切片

list_game = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


def left_slide():
    """
    实现向左划的变化
    :return: list_game
    """
    for r in range(4):
        list_original = list_game[r]
        list_game[r] = add_adjacent_same_numbers_left(list_original)
    return list_game


def right_slide():
    """
    实现向右划的变化
    :return:
    """
    for r in range(4):
        list_original = list_game[r]
        list_game[r] = add_adjacent_same_numbers_right(list_original)
    return list_game


def up_slide():
    """
    向上划
    :return:
    """
    for r in range(4):
        list_original = []
        for c in range(4):
            list_original.append(list_game[c][r])
        list_result = add_adjacent_same_numbers_left(list_original)
        for i in range(4):
            list_game[i][r] = list_result[i]
    return list_game


def down_slide():
    """
    向下划
    :return:
    """
    for r in range(4):
        list_original = []
        for c in range(4):
            list_original.append(list_game[c][r])
        list_result = add_adjacent_same_numbers_right(list_original)
        for i in range(4):
            list_game[i][r] = list_result[i]
    return list_game


def two_generator():
    """
    随机在一个没有2的位置生成2,
    :return: none
    """
    while True:
        r = randint(0, 3)
        c = randint(0, 3)
        if list_game[r][c] == 0:
            list_game[r][c] = 2
            break


def game_begin():
    """
    用w,a,s,d控制滑动方向，""退出
    :return:
    """
    two_generator()
    for item in list_game:
        print(item, end="\n")
    game_continue = True
    while game_continue:
        manipulate = input("请输入滑动方向")
        if manipulate == "w":
            up_slide()
        elif manipulate == "a":
            left_slide()
        elif manipulate == "s":
            down_slide()
        elif manipulate == "d":
            right_slide()
        elif manipulate == "":
            game_continue = False
        else:
            print("请输入wasd之间的字母，如果要退出，请按回车")
        two_generator()
        for item in list_game:
            print(item, end="\n")


game_begin()

# bug 1 在产生randint之前需要先判断能不能动，如果不能动，就不能够产生.
# 修复办法。需要增加判断能不能进行左右上下移动，不能移动进行提示。
# 还可以zen jia

