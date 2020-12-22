"""
2. 给你一个 n*m 的二维数组，每个元素保证递增，每列元素保证递增，试问如何找到某个数字，或者判断这个数字不存在。
"""

# 在这一行里，就要大于等于这一行的最小值，小于等于这一行的最大值
list01 = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 5, 6, 8]
]


def solution01(list01, target):
    n = len(list01[0])
    m = len(list01)
    list_zuobiao = []
    for r in range(m):
        if list01[r][0] <= target <= list01[r][n-1]:
            for c in range(n):
                if list01[r][c] == target:
                    list_zuobiao.append((c+1,r+1))
    return list_zuobiao


print(solution01(list01, 4))


