"""
    给你一个长度为n的数组，其中只有一个数字出现了1次，其他均出现2次，问如何快速的找到这个数字。
"""
nums = [6, 4, 7, 6, 7, 4, 5]


def solution(nums):
    nums.sort()
    # lenth = range(len(nums) - 1)
    i = 0
    while True:
        if nums[i] == nums[i + 1]:
            i += 2
        else:
            return nums[i]


print(solution(nums))
nums.sort()
print(nums)
