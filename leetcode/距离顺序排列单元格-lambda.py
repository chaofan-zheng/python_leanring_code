"""
给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。

另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。

返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。）

 

示例 1：

输入：R = 1, C = 2, r0 = 0, c0 = 0
输出：[[0,0],[0,1]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1]
示例 2：

输入：R = 2, C = 2, r0 = 0, c0 = 1
输出：[[0,1],[0,0],[1,1],[1,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
[[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
示例 3：

输入：R = 2, C = 3, r0 = 1, c0 = 2
输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。
 

提示：

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-cells-in-distance-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# class Solution:
#     def __init__(self, R, C, r0, c0):
#         self.R = R
#         self.C = C
#         self.c0 = c0
#         self.r0 = r0
#
#
#     def sort_by_distance(self):
#         distance_list = []
#         for r in range(self.R):
#             for c in range(self.C):
#                 distance = abs(r - self.r0) + abs(c - self.c0)
#                 distance_list.append(distance)
#         distance_list.sort()
#         return distance_list
#
#
# solution = Solution(2, 2, 0, 1)
# print(solution.sort_by_distance())

class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        distance_list = []
        point_list = []
        for r in range(R):
            for c in range(C):
                distance = abs(r - r0) + abs(c - c0)
                distance_list.append(distance)
                point_list.append((r, c))

        for x in range(len(distance_list) - 1):
            for y in range(x + 1, len(distance_list)):
                if distance_list[x] > distance_list[y]:
                    distance_list[x], distance_list[y] = distance_list[y], distance_list[x]
                    point_list[x], point_list[y] = point_list[y], point_list[x]

        return point_list


print(Solution().allCellsDistOrder(2, 3, 1, 2))

"""
答案

"""


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        ret = [(i, j) for i in range(R) for j in range(C)]
        ret.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return ret
    # lambda 的意思是 按照自定义方法排序，x表示元素，x按照 两个绝对值相加的大小排序
    # people.sort(key=lambda x: (x[0], -x[1])) 元素按照元素的第一个元素升序排列，第二个元素的降序排序。


list01 = [(1, 2), (3, 6), (2, 2), (3, 4)]
list01.sort(key=lambda x: x[0] + x[1])
print(list01)

list02 = [(1, 2), (3, 6), (2, 2), (3, 4)]
list02.sort(key=lambda x: x[1])
print(list02)
