def func01(points):
    if not points:
        return 0
    count = 1
    points.sort(key=lambda x: x[1])
    pos = points[0][1]
    for balloon in points:
        if balloon[0] > pos:
            pos = balloon[1]
            count += 1
    return count
# 如果能一箭射爆多个气球，那么就一定存在一种最优解：这个箭刚好经过此气球群的右边索引最小的那个，所以如果左边最小的右边小，就能够射爆，不能的话就count+1
# 然后经过了这个能一箭射爆多个气球的气球群之后，要重新更新pos

list01 = [[1, 3], [4, 6], [7, 9], [8, 10], [11, 13]]
print(func01(list01))

# 贪心算法