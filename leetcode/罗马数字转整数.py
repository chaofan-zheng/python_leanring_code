"""
    罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer

"""


class Solution:
    def romanToInt(self, s):
        d = {'I': 1, 'IV': -2, 'V': 5, 'IX': -2, 'X': 10, 'XL': -20, 'L': 50, 'XC': -20, 'C': 100, 'CD': -200, 'D': 500,
             'CM': -200, 'M': 1000}
        result = 0
        for i, n in enumerate(s):
            if d.get(s[max(i - 1, 0):i + 1]):
                result_a = d.get(s[max(i - 1, 0):i + 1])
                result += result_a
            result_b = d[n]
            result += result_b
        result -= d[s[0]]
        # 减去第一个重复的情况
        return result

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300,
#              'D': 500, 'CM': 800, 'M': 1000}
#         return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))
        # return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))  # max是为了防止发生(-1，0)的情况
    # 第一个是两个两个一起循环，如果有那种数字的话就返回值
    # 第二个就是返回单个罗马数字对应的值
    # 两个一加正好是真实值


solution = Solution()
print(solution.romanToInt("IV"))
print(solution.romanToInt("MCMXCIV"))  # 1994
