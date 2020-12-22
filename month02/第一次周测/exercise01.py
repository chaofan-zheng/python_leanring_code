"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。（至少使用两种方法求解）
示例：给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""


# 方法一
def solution01(nums, target):
    for r in range(len(nums) - 1):
        for c in range(r + 1, len(nums)):
            if nums[c] + nums[r] == target:
                return (r, c)


print(solution01([2, 7, 11, 15], 9))


# 方法二
def solution02(nums, target):
    num_dict = {}
    for i in range(len(nums)):
        target_num = target - nums[i]
        if target_num not in num_dict:
            num_dict[nums[i]] = i
        else:
            return i, num_dict[target - nums[i]]


print(solution02([2, 7, 11, 15], 9))
