"""
 画出下列代码内存图
    map = [
        [2, 2, 8, 16],
        [4, 2, 0, 2],
        [2, 4, 2, 4],
        [0, 4, 0, 4],
    ]
    list_merge = map[0]
    list_merge[0] = 0
    print(map[0][0])# ?

    list_merge = map[1][::-1]
    list_merge[0] = 0
    map[1][::-1] = list_merge
    print(map[1]) # ?

"""

map = [
    [2, 2, 8, 16],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]
list_merge = map[0]
list_merge[0] = 0
print(map[0][0])  # 0

list_merge = map[1][::-1]
list_merge[0] = 0
map[1][::-1] = list_merge
print(map[1])  # 4200