"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if len(str_x) == 1:
            return True
        for i in range((len(str_x) // 2)):
            if str_x[i] != str_x[len(str_x) - i - 1]:
                return False
        return True  # 这个return True要在循环外面
