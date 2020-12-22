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

list_game = [
    [2, 2, 0, 0],
    [0, 4, 2, 0],
    [4, 0, 4, 0],
    [4, 0, 8, 0],
]


def move_zero_to_end(list01):
    """
    把零元素向左移到末尾
    :param list01:输入的list
    :return: 输出的list
    """
    for i in range(len(list01) - 1, -1, -1):
        if list01[i] == 0:
            del list01[i]
            list01.append(0)
    return list01


def merge_adjacent_identical_items_left(list01):
    list_sorted = move_zero_to_end(list01)
    for i in range(len(list_sorted) - 1, 0, -1):
        if list_sorted[i] == list_sorted[i - 1]:
            list_sorted[i] += list_sorted[i - 1]
            del list_sorted[i - 1]
            list_sorted.append(0)
    return list_sorted


# def merge():
#     """
#         合并数据
#           核心思想：零元素后移，判断是否相邻相同。如果是则合并.
#     """
#     zero_to_end()
#     # len() - 1 : 因为最后一个元素不用与下一个比较
#     #             所以-1去掉最后一个元素
#     for i in range(len(list_merge) - 1):
#         if list_merge[i] == list_merge[i + 1]:
#             list_merge[i] += list_merge[i + 1]
#             del list_merge[i + 1]

def merge_adjacent_identical_items_right(list01):
    list_result = merge_adjacent_identical_items_left(list01[::-1])
    return list_result[::-1]


def left_slide(list_game):
    for item_list in list_game:
        item_list = merge_adjacent_identical_items_left(item_list)
    return list_game


def transpose(list_game):
    for r in range(1, len(list_game)):
        for c in range(r, len(list_game)):
            list_game[r - 1][c], list_game[c][r - 1] = list_game[c][r - 1], list_game[r - 1][c]
    return list_game


def up_slide(list01):
    list03 = transpose(left_slide(transpose(list01)))
    return list03


print(up_slide(list_game))
