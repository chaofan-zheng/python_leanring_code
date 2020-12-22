"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
True
"""


class Solution:
    def find(self, target, array):
        for r in range(len(array)):
            for c in range(len(array)):
                if array[r][c] == target:
                    return True


list01 = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
print(Solution().find(7, list01))
